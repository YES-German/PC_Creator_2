import discord
from discord.ext import commands

class main(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def main(ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/838857610358292532/912455051182755880/main.png")


def setup(client):
    client.add_cog(main(client))