import discord
from discord.ext import commands
from discord import Option
from discord.ext.commands import MissingPermissions

class unmute(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name = 'unmute', description = "unmutes/untimeouts a member")
    @commands.has_permissions(moderate_members = True)
    async def unmute(self, ctx, member: Option(discord.Member, required = True), reason: Option(str, required = False)):
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


def setup(client):
    client.add_cog(unmute(client))