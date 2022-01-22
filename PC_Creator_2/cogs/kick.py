import discord
from discord.ext import commands

class kick(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.slash_command(name="kick")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason= "No reason ..."):
        channel = self.client.get_channel(850085134622261308)
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


def setup(client):
    client.add_cog(kick(client))