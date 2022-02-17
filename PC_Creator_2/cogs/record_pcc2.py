import discord
from discord.ext import commands

class record_pcc2(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(name="record_pcc2", description="Shows the best PC in PCC2")
    async def record_pcc2(self, ctx): 
        embed = discord.Embed(title="__PCC2 World Record__", description="This is the current PCC2 World Record PC", color=13565696)
        embed.add_field(name=f":small_blue_diamond: Achieved by", value="<@634860829132455937> Harrison#3680 (634860829132455937)", inline=False)
        embed.add_field(name=f":small_blue_diamond: Details", value="Max overclocks are needed to get the highest score \n• MX-4 45 Thermal Paste is required and needs to cover \n100% of the CPU \n• Max overclocking skill is required.", inline=False)
        embed.add_field(name=f":small_blue_diamond: Score achieved", value="`2.879.107`", inline=False)
        embed.set_image(url="https://media.discordapp.net/attachments/940786924740837436/941685857595838484/Screenshot_20220211-072209_PC_Creator_2.jpg")

        await ctx.respond(embed=embed)   

def setup(client):
    client.add_cog(record_pcc2(client))