
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
#from antispam import AntiSpamHandler, Options
from collections import Counter
import collections
import schedule
import time
from PIL import Image, ImageDraw, ImageFont
from discord.ext.commands import MemberNotFound
# from AntiSpamTrackerSubclass import MyCustomTracker


#os.chdir("/home/pi/Desktop/PC_Creator_2")
client = commands.Bot(command_prefix=",", intents=discord.Intents.all(), case_insensitive=True)
client.remove_command('help')



@client.event
async def on_ready():
    print("PC_Creator_2 Bot is online")
    await client.change_presence(activity=discord.Streaming(name="Playing PC Creator 2", url="https://www.youtube.com/watch?v=o9qoiH0Am7o"))
    client.start_time = datetime.now()
    


    @tasks.loop(seconds = 30) # repeat after every 10 seconds
    async def myLoop():
        await asyncio.sleep(30)
        spammers.clear() 


    myLoop.start()

    

    while True:
        schedule.run_pending()
        await asyncio.sleep(1) 

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

    filtered_words = ["fuck", "idiot", "shit"] 
    topleveldomain = ["https://", "http://", "com", "org", "net"]

    for word in topleveldomain:
         if word in message.content:
             print("Domain True")

    if "@everyone" in message.content:
         print("Everyone True")        

    if len(message.content) > 32:
         print("Größer 32")
        
    for word in topleveldomain:
        #and ("@everyone" in message.content or "@here" in message.content or "everyone" in message.content or "here" in message.content))
        if word in message.content and len(message.content) > 32 and not (".jpg" in message.content or ".png" in message.content):
            spammers.append(message.author.id)   

    if Counter(spammers)[message.author.id] == 3:
        await message.channel.send(f"{message.author.mention} stop spamming that message. If you continue spamming, you will be **banned**. In case there are problems and you are not a scamer, send a DM to ¥£$#7660 (695229647021015040)", delete_after=10)       

    if Counter(spammers)[message.author.id] >= 4:
        channel = client.get_channel(933768368970932254)
        try:
            
            await message.author.send(f"You were softbanned on the PC Creater server")
            await message.author.send(f"reason: Scam")
        except:
            return
        embed = discord.Embed(title="Softbanned", color=13565696)
        embed.add_field(name="Softbanned:", value=f"{message.author.mention}")
        embed.add_field(name="Moderator", value=f"<@884402383923339295>")
        embed.add_field(name="Reason:", value="Scam", inline=False)

        await channel.send(embed=embed)    
        await message.channel.send(f"Softbanned {message.author.mention}", delete_after=10)
        await message.author.ban(reason="Scam")  
        await message.author.unban(reason="Scam")    

    member = message.author
    for word in filtered_words:
        if word in message.content and not get(member.roles, id=589435378147262464):
            await message.delete()
            await message.channel.send("This word is banned here" ,delete_after=5.0)

    if message.channel.id == 572541644755435520:
        if not message.content.startswith(",suggest"):
            await message.delete()
            await message.channel.send(f"{message.author.mention} Please use the **,suggest** command to suggest things here", delete_after=10)        

    if message.channel.id == 940691696918880326:
        if not message.content.startswith(",,suggest"):
            await message.delete()
            await message.channel.send(f"{message.author.mention} Please use the **,,suggest** command to suggest things here", delete_after=10)             

    if not message.content.startswith(",") and not message.channel.id == 572673322891083776:    
            await new_member(message.author)

            user = message.author

            users = await get_messages()  

            messag_e = int(1)

            users[str(user.id)] += messag_e

            with open("userLevels.json", "w") as f:
                json.dump(users,f)  

            with open ("counter-file.txt", "r") as cf:
                data = cf.readlines()
                cf.close
            daily_messages = data[64]
            daily_messages_2 = int(daily_messages)
            test =  int(1)
            daily_messages_2 += test
            daily_messages_3 = str(daily_messages_2)
            data[64] = daily_messages_3
            with open ("counter-file.txt", "w") as cf:
                cf.writelines(data)
                cf.close             

    await client.process_commands(message)  
    

@client.command()
async def testo(ctx):
    await ctx.send(spammers)
    await ctx.send(collections.Counter(spammers))  

async def get_messages():
    with open("userLevels.json", "r") as f:
        users = json.load(f)
    return users   

async def new_member(user):

    users = await get_messages()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)] = 0        

    with open("userLevels.json", "w") as f:
        json.dump(users,f)
    return True     


#@client.command()
#async def restrict(ctx):

   # with open("channel_restrictions.json", "r"):

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)}')     
                              
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, MemberNotFound):
        await ctx.send("Can't find this member")
        return
    raise error    


initial_extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)    

