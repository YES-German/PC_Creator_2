import discord
from discord.ext import commands

class softban(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="softban", description="For moderation")
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason= "No reason ..."):
        channel = self.client.get_channel(933768368970932254)
        try:
            await member.send(f"You were softbanned on the PC Creater server")
            await member.send(f"reason: {reason}")
            embed = discord.Embed(title="Softbanned", color=13565696)
            embed.add_field(name="Softbanned:", value=f"{member.mention}")
            embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
            embed.add_field(name="Reason:", value=reason, inline=False)

            await channel.send(embed=embed)    
            await ctx.respond(f"Softbanned {member.mention}")
            await member.ban(reason=reason)
            await member.unban(reason=reason)
        except:
            embed = discord.Embed(title="Softbanned", color=13565696)
            embed.add_field(name="Softbanned:", value=f"{member.mention}")
            embed.add_field(name="Moderator", value=f"{ctx.author.mention}")
            embed.add_field(name="Reason:", value=reason, inline=False)

            await channel.send(embed=embed)    
            await ctx.respond(f"Softbanned {member.mention}")
            await member.ban(reason=reason)  
            await member.unban(reason=reason)


def setup(client):
    client.add_cog(softban(client))