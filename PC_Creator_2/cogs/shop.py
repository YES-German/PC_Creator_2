import discord
from discord.ext import commands
from discord.ui import Button, View
import json
from discord import Option
from discord.commands import permissions


class Shop_Select(discord.ui.View):

    with open("shop.json", "r") as f:
            items = json.load(f)

    options = []

    for item_list in items:
        name = item_list["item_name"]
        price = item_list["price"]
        emoji = item_list["emoji"]

        options.append(discord.SelectOption(label=name, description=f"Price: {price} coins"))

    async def get_coins(self):
            with open("usercoins.json", "r") as f:
                users_coins = json.load(f)
            return users_coins

    async def get_useritems(self):
                with open("useritems.json", "r") as f:
                    users_items = json.load(f)
                return users_items

    async def sub_coins(self, user, subprice):

        with open("usercoins.json", "r") as f:
                users_coins = json.load(f)
        user = str(user)
        if user in users_coins:
            purse = users_coins[user]
            if purse >= subprice:
                successpurchase = 'successpurchase'
                return successpurchase
            else:
                failpurchase = 'failpurchase'
                return failpurchase
        else:
            users_coins[str(user)] = {}
            users_coins[str(user)] = 0
            nocoins = 'nocoins'
        return nocoins

    @discord.ui.select(placeholder="Choose the item you want to buy", min_values=1, max_values=1, options=options)
    async def callback(self, select, interaction : discord.Interaction):


        with open("shop.json", "r") as f:
            items = json.load(f)
        responder = str(interaction.user.id)
        item_name = select.values[0]
        for item in items:
            if item["item_name"] == item_name:
                subprice = item["price"]
        status = await self.sub_coins(responder, subprice)
        with open("usercoins.json", "r") as f:
                users_coins = json.load(f)
        if responder in users_coins:
            purse = users_coins[str(responder)]
            if status == 'successpurchase':
                with open("useritems.json", "r") as f:
                        users_items = json.load(f)
                twoitem = False
                if responder in users_items:
                    for testitem in users_items[str(responder)]:
                        if testitem == item_name:
                            twoitem = True

                async def newuseritem_member(self):
                    with open("useritems.json", "r") as f:
                        users_items = json.load(f)
                    if str(responder) in users_items:
                        currentitem = users_items[str(responder)]
                        currentitem = currentitem + [item_name]
                        users_items[str(responder)] = currentitem
                        with open("useritems.json", "w") as f:
                            json.dump(users_items, f)
                        return True
                    else:
                        users_items[str(responder)] = [f"{item_name}"]
                        with open("useritems.json", "w") as f:
                            json.dump(users_items, f)
                    return False

                await newuseritem_member(self)
                if twoitem != True:
                    subcoins = int(subprice)
                    purse -= subcoins
                    users_coins[str(responder)] = purse
                    with open("usercoins.json", "w") as f:
                        json.dump(users_coins,f)
                    await interaction.message.edit(content=f"You bought a {item_name} for **{subprice}** and have **{purse}** remaining.", view=None)
                else:
                    await interaction.message.edit(content=f"You can't buy a {item_name} for **{subprice}** because you already have it", view=None)
            elif status == 'failpurchase':
                await interaction.message.edit(content=f"You do not have enough money for **{item_name}**. It costs **{subprice}** and you only have **{purse}**.", view=None)
            elif status == 'nocoins':
                await interaction.message.edit(content=f"Something went completely wrong and the Bot is now broken and has probably crashed, or all of the coin-data has been lost", view=None)
        else:
            await interaction.message.edit(content=f"You somehow don't have any coins yet.", view=None)



class shop(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def get_items(self):
        with open("shop.json", "r") as f:
            items = json.load(f)
        return items

    async def get_coins(self):
            with open("usercoins.json", "r") as f:
                users_coins = json.load(f)
            return users_coins

    async def get_useritems(self):
                with open("useritems.json", "r") as f:
                    users_items = json.load(f)
                return users_items

    @commands.slash_command(name='shop', description='Buy items')
    async def shop(self, ctx):
        view = Shop_Select()
        await ctx.respond("Choose the item you want to buy", view=view)

    @commands.slash_command(name="inventory", description="What do you have?")
    async def bal_slash_command(self, ctx, member: Option(discord.Member, required = True)):
        send = ctx.respond
        user = member
        items = await self.get_useritems()
        coins = await self.get_coins()
        embed = discord.Embed(title=f"{member}'s inventory", color=1356569)
        if str(user.id) in items:
            items_str = items[str(user.id)]
            items_str = '\n'.join(items_str)
            coins = coins[str(user.id)]
            embed.add_field(name="Items", value=f"{items_str}")
        else:
            if str(user.id) in coins:
                coins = coins[str(user.id)]
                embed.add_field(name="Coins", value=f"{coins}")
            else:
                embed.add_field(name="Coins", value="none")
            embed.add_field(name="Items", value="none")
        try:
            embed.set_thumbnail(url=member.avatar.url)
        except:
            pass
        #await ctx.respond('This command is currently out of order. Use /balance or ,bal to see your Money.')
        await send(embed=embed)


    @commands.slash_command(name="new_item")
    @permissions.is_user(695229647021015040)
    async def new_item(self, ctx, item_name : Option(str, 'Item Name', required=True), price: Option(int, 'Price (only numbers)', required=True), emoji: Option(str, required=False)):
        shopjson = open("shop.json", "r")
        items = json.load(shopjson)
        if type(items) is dict:
            items = [items]

        if item_name in items:
            return False
        else:
            items.append({
                'item_name': item_name,
                'price': price,
                'emoji': emoji
            })


        with open("shop.json", "w") as outshopjson:
            json.dump(items,outshopjson)

            await ctx.respond(f"Added {item_name} \nprice: {price} \nemoji: {emoji}")




def setup(client):
    client.add_cog(shop(client))