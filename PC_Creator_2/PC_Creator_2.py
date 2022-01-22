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

os.chdir("C:\\Users\\zockerbande\\Desktop\\Neuer Ordner\\PC_Creator_2")
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


@client.event
async def on_message(message):

    filtered_words = ["fuck", "idiot", "shit"]  

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