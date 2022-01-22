import discord
from discord.ext import commands

class bitcoinpc(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(name="bitcoinpc", aliases=["miner", "bitcoinminer", "btcpc"])
    async def bitcoinpc(self, ctx):
        await ctx.send("https://media.discordapp.net/attachments/838857610358292532/919200191628849172/Bitcoin_PC_3.jpg")


def setup(client):
    client.add_cog(bitcoinpc(client))