import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from datetime import datetime
from datetime import timedelta
from datetime import date
from discord import Option

class timeout(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name = 'timeout', description = "mutes/timeouts a member")
    @commands.has_permissions(moderate_members = True)
    async def timeout(self, ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False), days: Option(int, max_value = 27, required = False), hours: Option(int, required = False), minutes: Option(int, required = False), seconds: Option(int, required = False)):
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


def setup(client):
    client.add_cog(timeout(client))