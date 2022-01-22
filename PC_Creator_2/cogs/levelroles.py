import discord
from discord.ext import commands
from datetime import datetime
import json
from datetime import timedelta
from datetime import date
from discord.utils import get


class levelroles(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):


        if not message.content.startswith(","):    
            await self.new_member(message.author)

            user = message.author

            users = await self.get_messages()  

            messag_e = int(1)

            users[str(user.id)]["messages"] += messag_e

            with open("levelroles.json", "w") as f:
                json.dump(users,f)        


        await self.client.process_commands(message)      

    @commands.command(aliases=["levelroles"])        
    async def lrs(self,ctx, member:discord.Member = None):
        await self.new_member(ctx.author)
      
        if member == None:
            member = ctx.author
            you = "You"
            your = "Your"
            your2 = "your"
            have = "have"

        else:
            you = "He/She"   
            your = "His/Her"
            your2 = "his/her"
            have = "has"

        user = member

        users = await self.get_messages()

        messages_amt_str = users[str(user.id)]["messages"]
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
            if get(member.roles, id=934114613639938168): # Check if this role is in the member's roles
                level = discord.Embed(title=f"{member.name}'s Level", description=f"{you} already {have} the **Level 1** role \n{your} next level role is **Level 2** and here's {your2} progress:", colour=13565696)
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
                    level = discord.Embed(title=f"{member.name}'s Levels", description=f"{you} already {have} the **Level 1** and **Level 2** roles \n{your} next level role is **Level 3** and here's {your2} progress:", colour=13565696)
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
                        level = discord.Embed(title=f"{member.name}'s Levels", description=f"{you} already {have} the **Level 1**, **Level 2** and **Level 3** roles \n{your} next level role is **Level 4** and here's {your2} progress:", colour=13565696)
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
                            level = discord.Embed(title=f"{member.name}'s Levels", description=f"{you} already {have} the **Level 1**, **Level 2**, **Level 3** and **Level 4** roles \n{your} next level role is **Level 5** and here's {your2} progress:", colour=13565696)    
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
                                level = discord.Embed(title=f"{member.name}'s Levels", description=f"{you} already {have} **all** of the level **roles**. Here's {your2} progress:", colour=13565696)  
                                emoji = ":gem:"
                                date_emoji = ":gem:"
            else:
                level = discord.Embed(title=f"{member.name}'s Levels", description=f"{you} don't {have} any level roles yet \n{your} next level role is **Level 1** and here's {your2} progress:", color=13565696)
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
           await ctx.send("Can't find this user")

        embed = level
        embed.add_field(name="Messages", value=f"{emoji} {messages_amt}/{message_field}")
        embed.add_field(name="Days", value=f"{date_emoji} {delta_int}/{date_field}")
        embed.set_thumbnail(url=member.avatar.url)
        await ctx.send(embed=embed)

        if reached_level_2 == True:
            role = ctx.guild.get_role(934116232628674562)
            await ctx.send("You've received the **Level 2** role")
            await member.add_roles(role)

        if reached_level_3 == True:
            role = ctx.guild.get_role(934116557951475783)
            await ctx.send("You've received the **Level 3** role")
            await member.add_roles(role)  

        if reached_level_4 == True:
            role = ctx.guild.get_role(934116875091189780)  
            await ctx.send("You've received the **Level 4** role")
            await member.add_roles(role)   

        if reached_level_5 == True:
            role = ctx.guild.get_role(934117031668744193)  
            await ctx.send("You've received the **Level 5** role")
            await member.add_roles(role) 

        if reached_level_1 == True:
            role = ctx.guild.get_role(934114613639938168)  
            await ctx.send("You've received the **Level 1** role")
            await member.add_roles(role)          


        

    async def get_messages(self):
        with open("levelroles.json", "r") as f:
            users = json.load(f)
        return users   

    async def new_member(self, user):

        users = await self.get_messages()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["messages"] = 0        

        with open("levelroles.json", "w") as f:
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

            await self.new_member(ctx.author)

            user = member
            users = await self.get_messages()  
            messag_e = int(amount)
            users[str(user.id)]["messages"] += messag_e

            with open("levelroles.json", "w") as f:
                json.dump(users,f)

            await ctx.send(f"Added {amount} messages to {member}")    

        else:
            await ctx.send("You don't have the permissions to use this command")   

    @commands.command()
    async def setzero(self, ctx, member:discord.Member):
        if ctx.author.id == 695229647021015040:

            await self.new_member(ctx.author)

            user = member
            users = await self.get_messages()  
            messages_amt_str = users[str(user.id)]["messages"]
            messages_amt = int(messages_amt_str) 
            users[str(user.id)]["messages"] += -1*messages_amt     

            with open("levelroles.json", "w") as f:
                json.dump(users,f)

            await ctx.send(f"Set {member} messages to 0")     

def setup(client):
    client.add_cog(levelroles(client))            