import discord
from discord.ext import commands

class record(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def record(self, ctx): 
        embed = discord.Embed(title="__World Record__", description="This is the current World Record PC", color=13565696)
        embed.add_field(name=f":small_blue_diamond: Archieved by", value="<@695229647021015040> ¥£$#7660 (695229647021015040)", inline=False)
        embed.add_field(name=f":small_blue_diamond: Deatils", value="Overclocks are needed to get the highest score \n**CPU**: 153 Base 22 Boost \n**RAM**: 4680 \n**GPU**: 7840 and 40300 \n• ZALMVN ZMX55 Thermal Paste is required and needs to cover \n100% of the CPU \n• Max overclocking skill is required.", inline=False)
        embed.add_field(name=f":small_blue_diamond: Score archieved", value="`207,231`", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/838857610358292532/905766073557729290/record.jpg")

        await ctx.send(embed=embed)   


def setup(client):
    client.add_cog(record(client))