import discord
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="ban", description="For moderation")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason= "No reason ..."):
        channel = self.client.get_channel(850085134622261308)
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