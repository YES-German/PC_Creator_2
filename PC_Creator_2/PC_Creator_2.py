import discord
from discord.ext import commands
import asyncio
import random
from discord.ext import tasks
from discord.ext.commands import BucketType
from datetime import datetime
from datetime import timedelta
from datetime import date
import json
from discord.ext.commands import CommandNotFound
from discord.ui import Button, View
from discord import Option
from discord.ext.commands import MissingPermissions
import os
from discord.utils import get
from antispam import AntiSpamHandler, Options
from collections import Counter
import collections
# from AntiSpamTrackerSubclass import MyCustomTracker


#os.chdir("C:\\Users\\zockerbande\\Desktop\\Neuer Ordner\\PC_Creator_2")
client = commands.Bot(command_prefix=",", intents=discord.Intents.all(), case_insensitive=True)

# client.handler = AntiSpamHandler(client, options=Options(ignore_bots=False, no_punish=True))
# client.tracker = MyCustomTracker(client.handler, 3)
# client.handler.register_plugin(client.tracker)

@client.event
async def on_ready():
    print("PC_Creator_2 Bot is online")
    await client.change_presence(activity=discord.Streaming(name="Playing PC Creator 2", url="https://www.youtube.com/watch?v=o9qoiH0Am7o"))

    while True:
        await asyncio.sleep(30)
        spammers.clear()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error  

spammers = []


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # await client.handler.propagate(message)
    # await client.tracker.do_punishment(message)
    # await client.process_commands(message)

    filtered_words = ["fuck", "idiot", "shit"] 
    everyone_mention = "<@571031703661969430>" 
    everyone2_mention = "<@708218806928932896>"
    topleveldomain = ["com", "ru", "org", "net"]

    for word in topleveldomain:
        if (word in message.content and ("@everyone" in message.content or "@here" in message.content)) and len(message.content) > 32:
            print("OKKKK")
            spammers.append(message.author.id)   

    if Counter(spammers)[message.author.id] > 4:
        channel = client.get_channel(933768368970932254)
        try:
            await message.author.send(f"You were softbanned on the PC Creater server")
            await message.author.send(f"reason: Scam")
            embed = discord.Embed(title="Softbanned", color=13565696)
            embed.add_field(name="Softbanned:", value=f"{message.author.mention}")
            embed.add_field(name="Moderator", value=f"<@884402383923339295>")
            embed.add_field(name="Reason:", value="Scam", inline=False)

            await channel.send(embed=embed)    
            await message.channel.send(f"Softbanned {message.author.mention}")
            await message.author.ban(reason="Scam")
            await message.author.unban(reason="Scam")
        except:
            embed = discord.Embed(title="Softbanned", color=13565696)
            embed.add_field(name="Softbanned:", value=f"{message.author.mention}")
            embed.add_field(name="Moderator", value=f"<@884402383923339295>")
            embed.add_field(name="Reason:", value="Scam", inline=False)

            await channel.send(embed=embed)    
            await message.channel.send(f"Softbanned {message.author.mention}")
            await message.author.ban(reason="Scam")  
            await message.author.unban(reason="Scam")

    for word in filtered_words:
        if word in message.content:
            await message.delete()
            await message.channel.send("This word is banned here" ,delete_after=5.0)

    if not message.content.startswith(","):    
            await new_member(message.author)

            user = message.author

            users = await get_messages()  

            messag_e = int(1)

            users[str(user.id)]["messages"] += messag_e

            with open("levelroles.json", "w") as f:
                json.dump(users,f)           

    await client.process_commands(message)  
    

@client.command()
async def testo(ctx):
    await ctx.send(spammers)
    await ctx.send(collections.Counter(spammers))   
    

async def get_messages():
    with open("levelroles.json", "r") as f:
        users = json.load(f)
    return users   

async def new_member(user):

    users = await get_messages()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["messages"] = 0        

    with open("levelroles.json", "w") as f:
        json.dump(users,f)
    return True     










initial_extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)    

client.run("TOKEN")    