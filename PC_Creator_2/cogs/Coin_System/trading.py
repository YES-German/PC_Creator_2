import discord
from discord.ext import commands
from discord import Option
from discord.ui import Button, View
import json




class trading(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="trading", description="Trade parts")
    async def trading_slash(self, ctx, trading_partner : Option(discord.Member, required=True)):
        trading_guy = ctx.author
        global id
        id = ctx.author.id
        view = Own_trading_part()
        await ctx.respond("Choose the case", view=view)

"""
class Own_trading_part(discord.ui.View):

    with open("useritems.json", "r") as f:
            useritems = json.load(f)

    users_id = user_id()
    options = []
    global id
    items = useritems[str(id)]
    print(items)
    for case_name, Form_Factor_dict in cases.items():
        case_form_factor = Form_Factor_dict["Form_Factor"]


        options.append(discord.SelectOption(label=case_name, description=", ".join(case_form_factor)))
    @discord.ui.select(placeholder="Choose one option", min_values=1, max_values=1, options=options)
    async def callback(self, select, interaction : discord.Interaction):
       
        await interaction.message.edit(content=f"**{case_name}**", view=None)
"""

def setup(client):
    client.add_cog(trading(client))