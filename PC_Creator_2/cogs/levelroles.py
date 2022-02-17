import discord
from discord.ext import commands
from datetime import datetime
import json
from datetime import timedelta
from datetime import date
from discord.utils import get
import schedule
import time
from PIL import Image, ImageDraw, ImageFont
import asyncio
from discord.ext import tasks
from discord import Option


class levelroles(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        schedule.every().day.at("00:00").do(self.lrs_stats) 
        
     
    @commands.command(aliases=["levelroles", "lrs", "rank"])
    async def lrs_normal_command(self, ctx, member:discord.Member = None):
        send = ctx.send
        await self.lrs(ctx , send, member)


    @commands.slash_command(name="lrs", description="Sends your current levelroles progress")
    async def lrs_slash_command(self, ctx, member: Option(discord.Member, required = False)):
        send = ctx.respond
        await self.lrs(ctx , send, member)    
            
    async def lrs(self, ctx, send, member):
        await self.new_member(ctx.author)

        if member == None:
            member = ctx.author
            you = "You"
            your = "Your"
            your2 = "your"
            have = "have"
            dont = "don't"

        else:
            you = "He/She"   
            your = "His/Her"
            your2 = "his/her"
            have = "has"
            dont = "doesn't"

        user = member

        users = await self.get_messages()



        messages_amt_str = users[str(user.id)]
        messages_amt = int(messages_amt_str)
    

        if member in ctx.guild.members: # checks if the provided member is in the current server
            date_now = date.today()
            join_date = member.joined_at.date()
            delta = date_now - join_date
            delta_int = int(delta.days)
            reached_level_1 = False
            reached_level_2 = False
            reached_level_3 = False
            reached_level_4 = False
            reached_level_5 = False
            member = ctx.guild.get_member(member.id) # Get the member object of the user

            if member == self.client.user:
                level = discord.Embed(title=f"{member.display_name}'s Levels", description=f"{you} {dont} {have} any level roles yet \n{your} next level role is **Level 1** and here's {your2} progress:", color=13565696)
                message_field = int(1000)
                date_field = int(60)
                if messages_amt >= message_field and not get(member.roles, id=934114613639938168):
                    emoji = ":white_check_mark:"
                else:
                    emoji = ":x:"
                if delta_int >= date_field and not get(member.roles, id=934116232628674562):
                    date_emoji = ":white_check_mark:"
                else:
                    date_emoji = ":x:"    
                    
            if get(member.roles, id=934114613639938168): # Check if this role is in the member's roles
                level = discord.Embed(title=f"{member.display_name}'s Level", description=f"{you} already {have} the **Level 1** role \n{your} next level role is **Level 2** and here's {your2} progress:", colour=13565696)
                message_field = int(2000)
                date_field = int(90)
                if messages_amt >= message_field and not get(member.roles, id=934116232628674562):
                    emoji = ":white_check_mark:"
                else:
                    emoji = ":x:" 
                if delta_int >= date_field and not get(member.roles, id=934116232628674562):
                    date_emoji = ":white_check_mark:"
                else:
                   date_emoji = ":x:"    
                if messages_amt >= message_field and delta_int >= date_field and not get(member.roles, id=934116232628674562):
                    reached_level_2 = True    
                if get(member.roles, id=934116232628674562):
                    level = discord.Embed(title=f"{member.display_name}'s Levels", description=f"{you} already {have} the **Level 1** and **Level 2** roles \n{your} next level role is **Level 3** and here's {your2} progress:", colour=13565696)
                    message_field = int(4000)
                    date_field = int(120)
                    if messages_amt >= message_field and not get(member.roles, id=934116557951475783):
                        emoji = ":white_check_mark:"
                    else:
                        emoji = ":x:"
                    if delta_int >= date_field and not get(member.roles, id=934116557951475783):
                        date_emoji = ":white_check_mark:"
                    else:
                        date_emoji = ":x:"    
                    if messages_amt >= message_field and delta_int >= date_field and not get(member.roles, id=934116557951475783):
                        reached_level_3 = True
                    if get(member.roles, id=934116557951475783):
                        level = discord.Embed(title=f"{member.display_name}'s Levels", description=f"{you} already {have} the **Level 1**, **Level 2** and **Level 3** roles \n{your} next level role is **Level 4** and here's {your2} progress:", colour=13565696)
                        message_field = int(8000)
                        date_field = int(150)
                        if messages_amt >= message_field and not get(member.roles, id=934116875091189780):
                            emoji = ":white_check_mark:"
                        else:
                            emoji = ":x:"
                        if delta_int >= date_field and not get(member.roles, id=934116875091189780):
                            date_emoji = ":white_check_mark:"
                        else:
                            date_emoji = ":x:"    
                        if messages_amt >= message_field and delta_int >= date_field and not get(member.roles, id=934116875091189780):
                            reached_level_4 = True
                        if get(member.roles, id=934116875091189780):
                            level = discord.Embed(title=f"{member.display_name}'s Levels", description=f"{you} already {have} the **Level 1**, **Level 2**, **Level 3** and **Level 4** roles \n{your} next level role is **Level 5** and here's {your2} progress:", colour=13565696)    
                            message_field = int(16000)
                            date_field = int(180)
                            if messages_amt >= message_field and not get(member.roles, id=934117031668744193):
                                emoji = ":white_check_mark:"
                            else:
                                emoji = ":x:"
                            if delta_int >= date_field and not get(member.roles, id=934117031668744193):
                                date_emoji = ":white_check_mark:"
                            else:
                               date_emoji = ":x:"    
                            if messages_amt >= message_field and delta_int >= date_field and not get(member.roles, id=934117031668744193):
                                reached_level_5 = True    
                            if get(member.roles, id=934117031668744193):
                                level = discord.Embed(title=f"{member.display_name}'s Levels", description=f"{you} already {have} **all** of the level **roles**. Here's {your2} progress:", colour=13565696)  
                                emoji = ":gem:"
                                date_emoji = ":gem:"
            else:
                level = discord.Embed(title=f"{member.display_name}'s Levels", description=f"{you} {dont} {have} any level roles yet \n{your} next level role is **Level 1** and here's {your2} progress:", color=13565696)
                message_field = int(1000)
                date_field = int(60)
                if messages_amt >= message_field and not get(member.roles, id=934114613639938168):
                    emoji = ":white_check_mark:"
                else:
                    emoji = ":x:"
                if delta_int >= date_field and not get(member.roles, id=934116232628674562):
                    date_emoji = ":white_check_mark:"
                else:
                    date_emoji = ":x:"    
                if messages_amt >= message_field and delta_int >= date_field and not get(member.roles, id=934116232628674562):
                    reached_level_1 = True    
            

        else:
           await send("Can't find this user")

        embed = level
        embed.add_field(name="Messages", value=f"{emoji} {messages_amt}/{message_field}")
        embed.add_field(name="Days", value=f"{date_emoji} {delta_int}/{date_field}")
        embed.set_thumbnail(url=member.avatar.url)
        await send(embed=embed)

        if reached_level_2 == True:
            role = ctx.guild.get_role(934116232628674562)
            await send(f"{you} received the **Level 2** role")
            await member.add_roles(role)

        if reached_level_3 == True:
            role = ctx.guild.get_role(934116557951475783)
            await send(f"{you} received the **Level 3** role")
            await member.add_roles(role)  

        if reached_level_4 == True:
            role = ctx.guild.get_role(934116875091189780)  
            await ctx.send(f"{you} received the **Level 4** role")
            await member.add_roles(role)   

        if reached_level_5 == True:
            role = ctx.guild.get_role(934117031668744193)  
            await send(f"{you} received the **Level 5** role")
            await member.add_roles(role) 

        if reached_level_1 == True:
            role = ctx.guild.get_role(934114613639938168)  
            await send(f"{you} received the **Level 1** role")
            await member.add_roles(role)          


    async def get_messages(self):
        with open("userLevels.json", "r") as f:
            users = json.load(f)
        return users   

    async def new_member(self, user):

        users = await self.get_messages()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)] = 0        

        with open("userLevels.json", "w") as f:
            json.dump(users,f)
        return True     

    @commands.command()
    async def test(self, ctx, member:discord.Member):
        date_now = date.today()
        join_date = member.joined_at.date()
        delta = date_now - join_date
        await ctx.send(delta.days)

    @commands.command()
    async def givelevels(self, ctx, member:discord.Member,*, amount):
        if ctx.author.id == 695229647021015040:

            await self.new_member(member)

            user = member
            users = await self.get_messages()  
            messag_e = int(amount)
            users[str(user.id)] += messag_e

            with open("userLevels.json", "w") as f:
                json.dump(users,f)

            await ctx.send(f"Added {amount} messages to {member}")    

        else:
            await ctx.send("You don't have the permissions to use this command")   

    @commands.command()
    async def setzero(self, ctx, member:discord.Member):
        if ctx.author.id == 695229647021015040:

            await self.new_member(member)

            user = member
            users = await self.get_messages()  
            messages_amt_str = users[str(user.id)]
            messages_amt = int(messages_amt_str) 
            users[str(user.id)] += -1*messages_amt     

            with open("userLevels.json", "w") as f:
                json.dump(users,f)

            await ctx.send(f"Set {member} messages to 0")   

    @commands.command(aliases=["leaderboard"])
    async def lead(self, ctx):
        #self.lrs_stats()
        with open("userLevels.json", "r") as f:
            data = json.load(f)
            f = discord.File("/home/pi/Desktop/PC_Creator_2/dailymsgs.png")

            leaderboard = sorted(data.items(), key= lambda x: x[1], reverse=True)[:5]
            user_id_1st, msg_count_1st = leaderboard[0]
            user_id_2nd, msg_count_2nd = leaderboard[1]
            user_id_3rd, msg_count_3rd = leaderboard[2]
            user_id_4th, msg_count_4th = leaderboard[3]
            user_id_5th, msg_count_5th = leaderboard[4]
            embed= discord.Embed(title="Leaderboard", color=13565696)
            embed.add_field(name="Top users by messages sent", value=f"`1.` <@{user_id_1st}>: {msg_count_1st} \n`2.` <@{user_id_2nd}>: {msg_count_2nd} \n`3.` <@{user_id_3rd}>: {msg_count_3rd} \n`4.` <@{user_id_4th}>: {msg_count_4th} \n`5.` <@{user_id_5th}>: {msg_count_5th}")
            embed.set_image(url="attachment://dailymsgs.png")
            await ctx.send(file=f,embed=embed)   


    def lrs_stats(self):
        with open ("counter-file.txt", "r") as d_m:
            data = d_m.readlines()
            d_m.close
        new_amt = data[64]
        data[0] = f"{new_amt}\n{data[0]}"
        data[59] = ""
        data[64] = "0"
        with open ("counter-file.txt", "w") as cf:
            cf.writelines(data)
            cf.close
        with open ("counter-file.txt", "r") as d_m:
            data = d_m.read().splitlines()
            d_m.close
        data = [string for string in data if string != ""]

        data_2 = list(int(x) for x in data)
        hunderter = round(max(data_2)/100 + .5)
        if hunderter == 0:
            hunderter = 1
        x = 1
        y = 500/hunderter
        line = Image.open("lrs_stats_tabelle.png")
        draw = ImageDraw.Draw(line)
        for i in range(hunderter):
            y_1 = 500-y*x+2
            draw.line((4, y_1, 724, y_1), fill=(45, 48, 52), width=2)
            x += 1
        draw.line((4, 502, 724, 502), fill=(45, 48, 52), width=2)
        x_punkte = 0
        punktn = int(0)
        #print(data)
        #print(data[punktn])
        for i in range(60):
            y_multi = data[punktn]
            y_punkte = int(500/hunderter/100*int(y_multi))
            y_punkte = 500-y_punkte
            xy = [(716-x_punkte, y_punkte-1),(724-x_punkte, y_punkte+7)]
            draw.ellipse(tuple(xy),fill=(88, 101, 242), outline=(88, 101, 242))
            x_punkte += 12
            punktn += 1
        punktn = int(0)
        x_punkte = 5
        punktn = int(0)
        for i in range(59):
            y_multi = data[punktn]
            y_punkte_1 = int(500-(500/hunderter/100*int(y_multi)))
            punktn += 1
            y_multi = data[punktn]
            y_punkte_2 = int(500-(500/hunderter/100*int(y_multi)))
            xy = [(714-x_punkte, y_punkte_2+3),(724-x_punkte, y_punkte_1+3)]
            draw.line(xy, fill=(88, 101, 242), width=3)
            x_punkte += 12
        lrs_picture = Image.open("lrs_stats_fertig.png")
        lrs_picture.paste(line, (5, 46))
        lrs_picture_text = ImageDraw.Draw(lrs_picture)
        lrs_picture_text.fontmode = "1"
        myFont = ImageFont.truetype('/home/pi/Desktop/PC_Creator_2/calibri.ttf', 20)
        x = 0
        y = 500/hunderter
        for i in range(hunderter):
            y_1 = y*x+40
            lrs_picture_text.text((731, y_1), f"{(hunderter-x)*100} msgs/day",font=myFont, fill=(255, 255, 255))
            x += 1
        lrs_picture_text.text((731, 540), "0 msgs/day",font=myFont, fill=(255, 255, 255))
        lrs_picture.save("dailymsgs.png")  

  
    

        

def setup(client):
    client.add_cog(levelroles(client))            