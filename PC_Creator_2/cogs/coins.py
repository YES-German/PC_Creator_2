from http import server
from xmlrpc.client import Server
import discord
from discord.ext import commands
from datetime import datetime
import json
from discord.utils import get
from discord.ext import tasks
from discord import Option
import random
from discord.commands import permissions


class messagecoins(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["balance", "bal", "coins"])
    async def bal_normal_command(self, ctx, member:discord.Member = None):
        send = ctx.send
        await self.bal(ctx, send, member)


    @commands.slash_command(name="balance", description="Displays how much money you own")
    async def bal_slash_command(self, ctx, member: Option(discord.Member, required = True)):
        send = ctx.respond
        await self.bal(ctx, send, member)



    async def bal(self, ctx, send, member):
        await self.new_member(ctx.author)
        user = member
        users_coins = await self.get_coins()
        messages_amt_str = users_coins[str(user.id)]
        messages_amt = int(messages_amt_str)
        embed = discord.Embed(title=f"{member.display_name}'s Money", color=1356569)
        embed.add_field(name="Coins:", value=f"{messages_amt}<:bot_icon:950876206956433503>")
        try:
            embed.set_thumbnail(url=member.avatar.url)
        except:
            pass
        await send(embed=embed)


    async def get_coins(self):
        with open("usercoins.json", "r") as f:
            users_coins = json.load(f)
        return users_coins

    async def new_member(self, user):

        users_coins = await self.get_coins()

        if str(user.id) in users_coins:
            return False
        else:
            users_coins[str(user.id)] = {}
            users_coins[str(user.id)] = 0

        with open("usercoins.json", "w") as f:
            json.dump(users_coins,f)
        return True


    @commands.slash_command(name="givecoins", description="Lmao you're poor")
    @permissions.is_user(695229647021015040)
    async def givecoins(self, ctx, member: Option(discord.Member, required=True), amount: Option(int, required=True)):
        await self.new_member(member)
        user = member
        users_coins = await self.get_coins()
        messag_e = int(amount)
        users_coins[str(user.id)] += messag_e

        with open("usercoins.json", "w") as f:
            json.dump(users_coins,f)
        await ctx.respond(f"Gave {member} {amount} Coins")

    @commands.slash_command(name="setzero", description="Zero coins :-(")
    @permissions.is_user(695229647021015040)
    async def setzero(self, ctx, member: Option(discord.Member, required=True)):
        await self.new_member(member)
        user = member
        users_coins = await self.get_coins()
        messages_amt_str = users_coins[str(user.id)]
        messages_amt = int(messages_amt_str)
        users_coins[str(user.id)] += -1*messages_amt

        with open("usercoins.json", "w") as f:
             json.dump(users_coins,f)
        await ctx.respond(f"Set {member}'s Coins to 0")


    @commands.slash_command(name="setcoins", description="How much money do you want?")
    @permissions.is_user(695229647021015040)
    async def setcoins(self, ctx, member: Option(discord.Member, required=True), amount: Option(int, required=True)):
        await self.new_member(member)

        user = member
        users_coins = await self.get_coins()
        messages_amt_str = users_coins[str(user.id)]
        messages_amt = int(messages_amt_str)
        users_coins[str(user.id)] += -1*messages_amt
        messag_e = int(amount)
        users_coins[str(user.id)] += messag_e
        with open("usercoins.json", "w") as f:
            json.dump(users_coins,f)
        await ctx.respond(f"Set {member} messages to {amount}")


    @commands.command(aliases=["bank"])
    async def rich_command(self, ctx):
        send = ctx.send
        url=ctx.guild.icon.url
        await self.lead(send, url)

    @commands.slash_command(name="richlist", description="Who is the richest")
    async def rich_slash(self, ctx):
        send = ctx.respond
        url=ctx.guild.icon.url
        await self.lead(send, url)

    async def lead(self, send, url):
        with open("usercoins.json", "r") as f:
            data = json.load(f)

            leaderboard = sorted(data.items(), key= lambda x: x[1], reverse=True)[:5]
            embed= discord.Embed(title="Bank", color=1356569)
            if len(leaderboard) >= 5:
                user_id_1st, msg_count_1st = leaderboard[0]
                user_id_2nd, msg_count_2nd = leaderboard[1]
                user_id_3rd, msg_count_3rd = leaderboard[2]
                user_id_4th, msg_count_4th = leaderboard[3]
                user_id_5th, msg_count_5th = leaderboard[4]
                embed.add_field(name="Richest users", value=f"`1.` <@{user_id_1st}>: {msg_count_1st}<:bot_icon:950876206956433503> \n`2.` <@{user_id_2nd}>: {msg_count_2nd}<:bot_icon:950876206956433503> \n`3.` <@{user_id_3rd}>: {msg_count_3rd}<:bot_icon:950876206956433503> \n`4.` <@{user_id_4th}>: {msg_count_4th}<:bot_icon:950876206956433503> \n`5.` <@{user_id_5th}>: {msg_count_5th}<:bot_icon:950876206956433503>")
            else:
                embed.add_field(name="How can you see this?", value="There have been less than 5 people sending a message since the data was reset")
            try:
                embed.set_thumbnail(url=url)
            except:
                pass
            await send(embed=embed)

    @commands.slash_command(name="cscredits", description="Credits for the coin system")
    async def credits_slash(self, ctx):
        embed= discord.Embed(title="Credits", color=discord.Color.from_rgb(255, 0, 255))
        embed.add_field(name="Programming", value="<@443769343138856961>\n<@695229647021015040>")
        embed.add_field(name="Idea", value="<@695229647021015040>")
        embed.add_field(name="Help", value="<@713696771188195368>\n<@689861643865554964>")
        try:
                embed.set_thumbnail(url=ctx.guild.icon.url)
        except:
            pass
        await ctx.respond(embed=embed)

    @commands.slash_command(name="luckywheel", description="Win something...")
    async def luckywheel_slash(self, ctx, amount:Option(int, required=True)):
        member = ctx.author
        user = member
        users_coins = await self.get_coins()
        coins_amt_str = users_coins[str(user.id)]
        coins_amt = int(coins_amt_str)

        if amount > coins_amt:
            await ctx.respond("You don't have that much coins")
            return

        if amount == 0:
            await ctx.respond("You can't use 0<:bot_icon:950876206956433503>")
            return    

        win = random.randrange(0,3)   
        money_before = users_coins[str(user.id)]

        if win == 0:
            money_after = money_before + 2*amount
            win_state =  "You won <:Stonksup:712232686441463828> <:Stonksup:712232686441463828>"
            won_word = "won"
            prize = 2*amount
            users_coins[str(user.id)] += prize

        if win == 1 or win == 2:
            money_after = money_before - amount
            win_state = "You lost <:Stonksdown:712232673342390303> <:Stonksdown:712232673342390303>" 
            won_word = "lost"
            prize = amount 
            prize_1 = -1*amount
            users_coins[str(user.id)] += prize_1
            
        with open("usercoins.json", "w") as f:
            json.dump(users_coins,f)
        embed= discord.Embed(title="Lucky wheel", color=member.color)
     
        embed.add_field(name=win_state, value=f"<@{member.id}> {won_word} {prize} \n\nYou had **{money_before}**<:bot_icon:950876206956433503> and now you have **{money_after}**<:bot_icon:950876206956433503>")

        try:
                embed.set_thumbnail(url=member.avatar.url)
        except:
            pass
        await ctx.respond(embed=embed)


    @commands.slash_command(name="guessnumber", description="Guess the number")
    async def guessnumber_slash(self, ctx, amount: Option(int, required=True)):
        await self.new_member(ctx.author)

        member = ctx.author
        user = member
        users_coins = await self.get_coins()
        coins_amt_str = users_coins[str(user.id)]
        coins_amt = int(coins_amt_str)

        if amount > coins_amt:
            await ctx.respond("You dont have that much money")  
            return


        await ctx.respond("Choose a number between 1 and 10")     

        guessnumber = random.randrange(0,11)   

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel 
        
        msg = await self.client.wait_for('message', check=check)  

        if msg.content == guessnumber:
            await ctx.send(f"That's right <:pog:813886729235988541> \nYou wont {2*amount}<:bot_icon:950876206956433503>")
            prize = 2*amount
            users_coins[str(user.id)] += prize
        else:
            await ctx.send(f"I'm sorry but that's wrong. The right answer is {guessnumber} \nYou lost {amount}<:bot_icon:950876206956433503>") 
            prize = -1*amount
            users_coins[str(user.id)] += prize

def setup(client):
    client.add_cog(messagecoins(client))