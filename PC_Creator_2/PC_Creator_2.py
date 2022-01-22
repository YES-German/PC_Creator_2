import discord
from discord.ext import commands
import asyncio
import random
from discord.ext import tasks
from discord.ext.commands import BucketType
from datetime import datetime
import json
from discord.ext.commands import CommandNotFound
from discord.ui import Button, View
from discord import Option
from datetime import timedelta
from datetime import date
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

    await client.process_commands(message)              


@client.command()
async def scores(ctx, reason = None):
    try:
        if reason.lower() == "cpu":
            await ctx.send("https://cdn.discordapp.com/attachments/802512035224223774/906284061830549565/CPU-Scores_Super_Dark_Mode_2.jpg") 
        if reason.lower() == "gpu":
            await ctx.send("https://cdn.discordapp.com/attachments/838857610358292532/906193805324218388/GPU_Scores_Super_Dark_Mode_4.jpg")  
        if reason.lower() == "ram":
            await ctx.send("https://cdn.discordapp.com/attachments/838857610358292532/905926830081577000/RAM_scores_Super_Dark_Mode_3.jpg")

    except:
        button_cpu = Button(label="CPU", style=discord.ButtonStyle.primary)
        button_gpu = Button(label="GPU", style=discord.ButtonStyle.primary)
        button_ram = Button(label="RAM", style=discord.ButtonStyle.primary)
        button_all = Button(label="All", style=discord.ButtonStyle.primary)

        view = View()
        view.add_item(button_cpu)
        view.add_item(button_gpu)
        view.add_item(button_ram)
        view.add_item(button_all)

        message = await ctx.send('Which component chart would you like to view? Respond with "CPU", "GPU", "RAM" or "all" (20s)', view=view)

        async def button_cpu_callback(interaction):
            await message.edit(content="https://cdn.discordapp.com/attachments/802512035224223774/906284061830549565/CPU-Scores_Super_Dark_Mode_2.jpg", view=None)

        async def button_gpu_callback(interaction):
            await message.edit(content="https://cdn.discordapp.com/attachments/838857610358292532/906193805324218388/GPU_Scores_Super_Dark_Mode_4.jpg", view=None)

        async def button_ram_callback(interaction):
            await message.edit(content="https://cdn.discordapp.com/attachments/838857610358292532/905926830081577000/RAM_scores_Super_Dark_Mode_3.jpg", view=None)

        async def button_all_callback(interaction):
            await message.edit(content="https://cdn.discordapp.com/attachments/802512035224223774/906284061830549565/CPU-Scores_Super_Dark_Mode_2.jpg", view=None)            
            await ctx.send("https://cdn.discordapp.com/attachments/838857610358292532/906193805324218388/GPU_Scores_Super_Dark_Mode_4.jpg")
            await ctx.send("https://cdn.discordapp.com/attachments/838857610358292532/905926830081577000/RAM_scores_Super_Dark_Mode_3.jpg")

        button_cpu.callback = button_cpu_callback
        button_gpu.callback = button_gpu_callback
        button_ram.callback = button_ram_callback
        button_all.callback = button_all_callback



@client.command()
async def levels(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/748122380383027210/883432420567834754/Levels.jpg")


@client.command()
async def optimize(ctx):
    await ctx.send("The goal of this requirement is to make the PC get the specified FPS in the specified game, meaning you must test hardware and play the game on the PC till you find something that meets or beats the requirement. Parts that affect FPS are CPUs, RAM, and GPUs.")    
    await ctx.send("https://images-ext-2.discordapp.net/external/N_KGsUc6ROD1TTOPEKAd558ih_r9WA8pjJvZgJ5yEio/https/media.discordapp.net/attachments/778848112588095559/904718105740210216/unknown.png?width=930&height=335")


@client.command(name="bitcoinpc", aliases=["miner", "bitcoinminer", "btcpc"])
async def bitcoinpc(ctx):
    await ctx.send("https://media.discordapp.net/attachments/838857610358292532/919200191628849172/Bitcoin_PC_3.jpg")


@client.command()
async def main(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/838857610358292532/912455051182755880/main.png")


@client.command()
async def quantum(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/571031705109135361/933764379319619614/Quantum_items.jpg") 


@client.command()
async def cost(ctx):
    embed = discord.Embed(title="PCC2", description="PC Creator 2 is a paid game and costs **7,99€/7.99$**", color=13565696)
    embed.set_image(url="https://cdn.discordapp.com/attachments/802512035224223774/933806701080088576/IMG_3709.jpg")
    await ctx.send(embed=embed)


@client.command(aliases=["cc"])
async def customcpu(ctx):
    embed = discord.Embed(title="This is how custom CPUs where made", color=13565696)
    embed.set_image(url="https://images-ext-2.discordapp.net/external/uADQCXXNQ6xx3QHW8_cPLJ8w0kGUg1oiQDmxSVAvjGQ/https/media.discordapp.net/attachments/571031705109135361/809885303119675482/Screenshot_2021-02-12-17-34-34-411_com.ultraandre.pccreator.jpg?width=930&height=441")
    embed.set_footer(text="You cannot make custom CPUs anymore. The feature to manufacture them was removed in an update")
    await ctx.send(embed=embed)    


@client.command()
async def staff(ctx):
    helper_role = discord.utils.get(ctx.channel.guild.roles, id=697728131003580537)
    embed = discord.Embed(title="Staff", color=13565696)
    embed.add_field(name="Administrator", value="<@387088097374109698>, \n<@695229647021015040>", inline=False)
    embed.add_field(name="Moderator", value="<@491620401810767881>, \n<@438760488965242883>", inline=False)
    embed.add_field(name="Trial-Mod", value="None", inline=False)
    embed.add_field(name="Helper", value=f"<@695229647021015040>, \n<@402885493320318977>, \n<@713696771188195368> \n\nIf you have a question with the game, you are open to ping or message a {helper_role.mention} to receive help.")
    embed.set_footer(text="Some users are not displayed here because their activity on Discord is not moderation-oriented.")

    await ctx.send(embed=embed)


@client.command(name="credits")
async def credit(ctx):
    embed = discord.Embed(title="Credits", color=13565696)
    embed.add_field(name="Bot Owner/Developer", value="<@695229647021015040>", inline=False)
    embed.add_field(name="Bot Developer", value="<@713696771188195368>", inline=False)
    embed.add_field(name=",scores sheets", value="<@695229647021015040>, \n<@713696771188195368>")

    await ctx.send(embed=embed)


@client.command()
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - client.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    print(f"Der Bot ist seid **{days} Tagen**, **{hours} Stunden** und **{minutes} Minuten** online")
    await ctx.send(f"Der Bot ist seid **{days} Tagen**, **{hours} Stunden** und **{minutes} Minuten** online")


@client.command(name="ping")
async def ping(ctx):
  await ctx.send(f'ping: **{client.latency*1000:,.0f}ms**')


@client.slash_command(name="kick")
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason= "No reason ..."):
    channel = client.get_channel(850085134622261308)
    try:
        await member.send(f"You were kicked on the PC Creater server")
        await member.send(f"reason: {reason}")
        embed = discord.Embed(title="Kicked", color=13565696)
        embed.add_field(name="Kicked:", value=f"{member.mention}")
        embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
        embed.add_field(name="Reason:", value=reason, inline=False)

        await channel.send(embed=embed)
        await ctx.respond(f"Kicked {member.mention}")
        await member.kick(reason=reason)
    except:
        embed = discord.Embed(title="Kicked", color=13565696)
        embed.add_field(name="Kicked:", value=f"{member.mention}")
        embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
        embed.add_field(name="Reason:", value=reason, inline=False)

        await channel.send(embed=embed)
        await ctx.respond(f"Kicked {member.mention}")
        await member.kick(reason=reason)


@client.slash_command(name="ban", description="For moderation")
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason= "No reason ..."):
    channel = client.get_channel(850085134622261308)
    try:
        await member.send(f"You were banned on the PC Creater server")
        await member.send(f"reason: {reason}")
        embed = discord.Embed(title="Banned", color=13565696)
        embed.add_field(name="Banned:", value=f"{member.mention}")
        embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
        embed.add_field(name="Reason:", value=reason, inline=False)

        await channel.send(embed=embed)    
        await ctx.respond(f"Banned {member.mention}")
        await member.ban(reason=reason)   
    except:
        embed = discord.Embed(title="Banned", color=13565696)
        embed.add_field(name="Banned:", value=f"{member.mention}")
        embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
        embed.add_field(name="Reason:", value=reason, inline=False)

        await channel.send(embed=embed)    
        await ctx.respond(f"Banned {member.mention}")
        await member.ban(reason=reason)    


@client.command(name="unban")
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name, member_disc):

            await ctx.guild.unban(user)
            await ctx.send(f"Unbanned {member_name}")
            return

    await ctx.send(f"Can't find {member}")     



@client.slash_command(name = 'timeout', description = "mutes/timeouts a member")
@commands.has_permissions(moderate_members = True)
async def timeout(ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False), days: Option(int, max_value = 27, required = False), hours: Option(int, required = False), minutes: Option(int, required = False), seconds: Option(int, required = False)):
    if member.id == ctx.author.id:
        await ctx.respond("You can't timeout yourself!")
        return
    if member.guild_permissions.moderate_members:
        await ctx.respond("You can't do this, this person is a moderator!")
        return
    if days == None:
        days = 0
    if hours == None:
        hours = 0
    if minutes == None:
        minutes = 0
    if seconds == None:
        seconds = 0
    duration = timedelta(days = days, hours = hours, minutes = minutes, seconds = seconds)
    if duration >= timedelta(days = 28): #added to check if time exceeds 28 days
        await ctx.respond("You can't mute someone for more than 28 days!", ephemeral = True) #responds, but only the author can see the response
        return
    if reason == None:
        await member.timeout_for(duration)
        await ctx.respond(f"<@{member.id}> has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds by <@{ctx.author.id}>.")
    else:
        await member.timeout_for(duration, reason = reason)
        await ctx.respond(f"<@{member.id}> has been timed out for {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds by <@{ctx.author.id}> for '{reason}'.")

@timeout.error
async def timeouterror(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond("You can't do this! You need to have moderate members permissions!")
    else:
        raise error

@client.slash_command(name = 'unmute', description = "unmutes/untimeouts a member")
@commands.has_permissions(moderate_members = True)
async def unmute(ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False)):
    if reason == None:
        await member.remove_timeout()
        await ctx.respond(f"<@{member.id}> has been untimed out by <@{ctx.author.id}>.")
    else:
        await member.remove_timeout(reason = reason)
        await ctx.respond(f"<@{member.id}> has been untimed out by <@{ctx.author.id}> for '{reason}'.")

@unmute.error
async def unmuteerror(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.respond("You can't do this! You need to have moderate members permissions!")
    else:
        raise error


         

initial_extensions = []
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)    

client.run("TOKEN")    
