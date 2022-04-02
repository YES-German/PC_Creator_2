
from datetime import datetime, timedelta
from discord import Embed, client
from discord.ext import commands


class serverinfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="serverinfo")
    async def server_info(self, ctx):
        send = ctx.send
        await self.serverinfo(ctx, send)


    @commands.slash_command(name="serverinfo", description="Some infos about the server")
    async def serverinfo_slash(self, ctx):
        send = ctx.respond
        await self.serverinfo(ctx, send)


    async def serverinfo(self, ctx, send):
        embed = Embed(title="Server Info", colour=ctx.guild.owner.colour, timestamp=datetime.now())
        embed.set_thumbnail(url=ctx.guild.icon)
        statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

        fields = [("Owner:", ctx.guild.owner, True),
            ("Region:", ctx.guild.region, True),
            ("Server ID:", ctx.guild.id, True),
            ("Created at:", ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S"), False),
            ("Members:", len(ctx.guild.members), True),
            ("Humans:", len(list(filter(lambda m: not m.bot, ctx.guild.members))), True),
            ("Bots:", len(list(filter(lambda m: m.bot, ctx.guild.members))), True),
            ("Banned members:", len(await ctx.guild.bans()), True),
            ("Members Statuses:", f"🟢 {statuses[0]}\n🟠 {statuses[1]}\n🔴 {statuses[2]}\n⚪ {statuses[3]}", False),
            ("Categories:", len(ctx.guild.categories), True),
            ("Text channels:", len(ctx.guild.text_channels), True),
            ("Voice channels:", len(ctx.guild.voice_channels), True),
            ("Roles:", len(ctx.guild.roles), False),
            ("Valid Invites:", len(await ctx.guild.invites()), True),
            ("\u200b", "\u200b", True)]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await send(embed=embed)

def setup(bot):
    bot.add_cog(serverinfo(bot))