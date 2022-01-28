import discord
from discord.ext import commands

class quantum(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def quantum(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/571031705109135361/933764379319619614/Quantum_items.jpg") 


def setup(client):
    client.add_cog(quantum(client))