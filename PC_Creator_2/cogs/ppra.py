import discord
from discord.ext import commands

class ppra(commands.Cog):

    def __init__(self, client):
        self.client = client

 
    @commands.command(aliases=["proplayeraddrole"])
    async def ppra(self, ctx, member:discord.Member):
        role = ctx.guild.get_role(775736993018806322)
        await ctx.send(f"Added role **PRO PLAYER** to **{member}**")
        await member.add_roles(role)


def setup(client):
    client.add_cog(ppra(client)) 