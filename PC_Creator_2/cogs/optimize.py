import discord
from discord.ext import commands

class optimize(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def optimize(self, ctx):
        await ctx.send("The goal of this requirement is to make the PC get the specified FPS in the specified game, meaning you must test hardware and play the game on the PC till you find something that meets or beats the requirement. Parts that affect FPS are CPUs, RAM, and GPUs.")    
        await ctx.send("https://images-ext-2.discordapp.net/external/N_KGsUc6ROD1TTOPEKAd558ih_r9WA8pjJvZgJ5yEio/https/media.discordapp.net/attachments/778848112588095559/904718105740210216/unknown.png?width=930&height=335")


def setup(client):
    client.add_cog(optimize(client)) 