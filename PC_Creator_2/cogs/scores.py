import discord
from discord.ext import commands
from discord.ui import Button, View

class scores(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.command()
    async def scores(self, ctx, reason = None):
        try:
            if reason.lower() == "cpu":
                await ctx.send("https://media.discordapp.net/attachments/838857610358292532/931919636461654046/CPU-Scores_Super_Dark_Mode_3.jpg") 
            if reason.lower() == "gpu":
                await ctx.send("https://media.discordapp.net/attachments/838857610358292532/931919674134904982/GPU_Scores_Super_Dark_Mode_5.jpg")  
            if reason.lower() == "ram":
                await ctx.send("https://media.discordapp.net/attachments/838857610358292532/931919651070423100/RAM_scores_Super_Dark_Mode_4.jpg")

        except:
            button_cpu = Button(label="CPU", style=discord.ButtonStyle.primary)
            button_gpu = Button(label="GPU", style=discord.ButtonStyle.primary)
            button_ram = Button(label="RAM", style=discord.ButtonStyle.primary)
            button_all = Button(label="All", style=discord.ButtonStyle.primary)

            view = View()
            view.add_item(button_cpu)
            view.add_item(button_gpu)
            view.add_item(button_ram)
            view.add_item(button_all)

            message = await ctx.send('Which component chart would you like to view? Respond with "CPU", "GPU", "RAM" or "all" (20s)', view=view)

            async def button_cpu_callback(interaction):
                await message.edit(content="https://media.discordapp.net/attachments/838857610358292532/931919636461654046/CPU-Scores_Super_Dark_Mode_3.jpg", view=None)

            async def button_gpu_callback(interaction):
                await message.edit(content="https://media.discordapp.net/attachments/838857610358292532/931919674134904982/GPU_Scores_Super_Dark_Mode_5.jpg", view=None)

            async def button_ram_callback(interaction):
                await message.edit(content="https://media.discordapp.net/attachments/838857610358292532/931919651070423100/RAM_scores_Super_Dark_Mode_4.jpg", view=None)

            async def button_all_callback(interaction):
                await message.edit(content="https://media.discordapp.net/attachments/838857610358292532/931919636461654046/CPU-Scores_Super_Dark_Mode_3.jpg", view=None)            
                await ctx.send("https://media.discordapp.net/attachments/838857610358292532/931919674134904982/GPU_Scores_Super_Dark_Mode_5.jpg")
                await ctx.send("https://media.discordapp.net/attachments/838857610358292532/931919651070423100/RAM_scores_Super_Dark_Mode_4.jpg")

            button_cpu.callback = button_cpu_callback
            button_gpu.callback = button_gpu_callback
            button_ram.callback = button_ram_callback
            button_all.callback = button_all_callback

def setup(client):
    client.add_cog(scores(client))            