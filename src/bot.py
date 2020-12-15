# bot.py
print("[Dash] Loading dependancies...")
import os
import discord
from discord.ext import commands
import dotenv
print("[Dash] Dependancies loaded!")

print("[Dash] Loading config from '.env'...")
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
prefix = os.getenv('DISCORD_PREFIX')

client = discord.Client()

from discord.ext import commands
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("[Dash] Core Dash functionality is online")
    print("[Dash] Setting status")
    await bot.change_presence(activity=discord.Playing(name="_help"))
    print("[Dash] Status set")


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


bot.run(TOKEN)
