import discord
from discord.ext import commands

class record_pcc2(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="record_pcc2", description="Shows the best PC in PCC2")
    async def record_pcc2(self, ctx): 
        embed = discord.Embed(title="__PCC2 World Record__", description="This is the current PCC2 World Record PC", color=13565696)
        embed.add_field(name=f":small_blue_diamond: Achieved by", value="<@713696771188195368> AMPW#5095 (713696771188195368)", inline=False)
        embed.add_field(name=f":small_blue_diamond: Details", value="Max overclocks are needed to get the highest score \n• MX-4 45 Thermal Paste is required and needs to cover \n100% of the CPU \n• Max overclocking skill is required.", inline=False)
        embed.add_field(name=f":small_blue_diamond: Score achieved", value="`3.197.969`", inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/571031705109135361/950463782163984414/Screenshot_20220306_174414_com.ultraandre.pccreator2.jpg")

        await ctx.respond(embed=embed)   

def setup(client):
    client.add_cog(record_pcc2(client))