import discord
from discord.ext import commands

class cost(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def cost(self, ctx):
        embed = discord.Embed(title="PCC2", description="PC Creator 2 is a paid game and costs **7,99€/7.99$**", color=13565696)
        embed.set_image(url="https://cdn.discordapp.com/attachments/802512035224223774/933806701080088576/IMG_3709.jpg")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(cost(client))