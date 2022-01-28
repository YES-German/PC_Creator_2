import discord
from discord.ext import commands
from datetime import datetime
from datetime import timedelta
from datetime import date

class whois(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def whois(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author

        role_ids = [571032502181822506, 632674518317531137, 697728131003580537]    

        member_created = member.created_at.strftime("%m-%d-%Y")   
        date_now = date.today()
        create_date = member.created_at.date()
        delta = date_now - create_date
        delta_int = int(delta.days) 
        years = "days"

        member_joined = member.joined_at.strftime("%m-%d-%Y")   
        join_date = member.joined_at.date()
        delta_join = date_now - join_date
        delta_join_int = int(delta_join.days) 
        months = "days"

        if delta_int >= 7:
            delta_weeks = float(delta.days/7)
            delta_int = int(delta.days/7)
            years = "weeks"
            if delta_weeks >= float(4.3):
                delta_month = int(delta_weeks/4.3)
                delta_int = int(delta_month)
                years = "months"
                if delta_month >= 12:
                    delta_years = int(delta_month/12)
                    delta_int = int(delta_years)
                    years = "years"

        if delta_join_int >= 7:
            delta_weeks2 = float(delta_join.days/7)
            delta_join_int = int(delta_join.days/7)
            months = "weeks"
            if delta_weeks2 >= float(4.3):
                delta_month2 = int(delta_weeks2/4.3)
                delta_join_int = int(delta_month2)
                months = "months"
                if delta_month2 >= 12:
                    delta_years2 = int(delta_month/12)
                    delta_join_int = int(delta_years2)
                    months = "years"            
        
        roles = [role.id for role in member.roles]
        rr = (['<@&{}> '.format(role) for role in roles][1:])
        rr2 = "\n".join([str(elem) for elem in rr])  



        embed = discord.Embed(title=f"{member.name}'s user info", color=member.color)
        embed.add_field(name=":small_blue_diamond: Account creation date", value=f"{member_created} (MM-DD-YYYY), {delta_int} {years} ago")
        embed.add_field(name=":small_blue_diamond: Join date", value=f"{member_joined} (MM-DD-YYY), {delta_join_int} {months} ago", inline=False)
        embed.add_field(name=":small_blue_diamond: ID, Nickname, and Mention", value=f"ID: {member.id} \nNickname: {member.display_name} \nMention: {member.mention}", inline = False)
        embed.add_field(name=":small_blue_diamond: Roles", value=f"{rr2}", inline=False)
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)

        


def setup(client):
    client.add_cog(whois(client))