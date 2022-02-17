import discord
from discord.ext import commands
from discord.commands import permissions

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="ban", description="For moderation")
    @permissions.has_any_role(589435378147262464, 648546626637398046, 632674518317531137, 571032502181822506)#, guild_id=[571031703661969430])
    async def ban(self, ctx, member : discord.Member, *, reason= "No reason ..."):
        channel = self.client.get_channel(933768368970932254)
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


def setup(client):
    client.add_cog(ban(client))