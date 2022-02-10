import discord
from discord.ext import commands
from datetime import datetime
from discord.ui import Button, View

class suggestions(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    #@commands.cooldown(1, 18000, commands.BucketType.user)
    async def suggest(self, ctx, *, reason=None): 
        #count_yes = 0
        #count_no= int(1)
        #count_yes_1 = count_yes + int(1)
        if ctx.channel.id == 572541644755435520 or ctx.channel.id == 933813622952562718:
        
            if reason == None:
                await ctx.send("You have to use ,suggest and then type your suggestion after ,suggest", delete_after=10)
            else:
                #button_yes = Button(label=count_yes, style=discord.ButtonStyle.success, emoji="✅")
                #button_no = Button(label=f"{count_no}", style=discord.ButtonStyle.danger, emoji="❌")

                #view = View()
                #view.add_item(button_yes)
                #view.add_item(button_no)
                await ctx.message.delete()
                embed=discord.Embed(title="Suggestion:", description=reason, color=13565696, timestamp=datetime.utcnow())   
                embed.set_author(name=f"{ctx.author.display_name} ({ctx.author.id})", icon_url=ctx.author.avatar.url)
                message = await ctx.send(embed=embed)
                await message.add_reaction("✅")
                await message.add_reaction("❌")

        else:
            await ctx.send("This command only works in #suggestions", delete_after=10)        


        #async def button_yes_callback(interaction):
        
        #    self.count_yes += 1
        #    button_yes.label = count_yes
        #    await message.edit(view=view)

        #async def button_no_callback(interaction):
        #    await message.edit(content="https://cdn.discordapp.com/attachments/838857610358292532/906193805324218388/GPU_Scores_Super_Dark_Mode_4.jpg", view=None)

        #button_yes.callback = button_yes_callback
        #button_no.callback = button_no_callback    


def setup(client):
    client.add_cog(suggestions(client))