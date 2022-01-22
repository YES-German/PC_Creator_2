import discord
from discord.ext import commands

class ping(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="ping")
    async def ping(self, ctx):
        await ctx.send(f'ping: **{self.client.latency*1000:,.0f}ms**')


def setup(client):
    client.add_cog(ping(client))