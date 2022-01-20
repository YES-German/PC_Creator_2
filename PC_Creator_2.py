import discord
from discord.ext import commands
import asyncio
import random
from discord.ext import tasks
from discord.ext.commands import BucketType
from datetime import datetime as dt
import json
from discord.ext.commands import CommandNotFound
from discord.ui import Button, View
from discord import Option

client = commands.Bot(command_prefix=",", intents=discord.Intents.all(), case_insensitive=True)

@client.event
async def on_ready():
    print("PC_Creator_2 Bot is online")
    await client.change_presence(activity=discord.Streaming(name="Playing PC Creator 2", url="https://youtu.be/o9qoiH0Am7o"))

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error  


@client.command()
async def record(ctx): 
    embed = discord.Embed(title="__World Record__", description="This is the current World Record PC")
    embed.add_field(name=f":small_blue_diamond: Archieved by", value="¥£$#7660 (695229647021015040)", inline=False)
    embed.add_field(name=f":small_blue_diamond: Deatils", value="Overclocks are needed to get the highest score \n **CPU**: 153 Base 22 Boost \n **RAM**: 4680 \n **GPU**: 7840 and 40300 \n • ZALMVN ZMX55 Thermal Paste is required and needs to cover \n 100% of the CPU \n • Max overclocking skill is required.", inline=False)
    embed.add_field(name=f":small_blue_diamond: Score archieved", value="`207,231`", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/838857610358292532/905766073557729290/record.jpg")

    await ctx.send(embed=embed)


client.run("TOKEN")    