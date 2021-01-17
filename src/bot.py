import logging

logging.basicConfig(formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s %(pathname)s - %(message)s')

logging.info("Starting Dash...")
logging.info("Loading dependencies...")

logging.info("")
logging.info("Loading 'os' API")
import os

logging.info("External API 'os' loaded")
logging.info("Loading 'requests' API")
import requests

logging.info("External API 'requests' loaded")
logging.info("Loading 'flask' API")
import flask

logging.info("External API 'flask' loaded")
logging.info("Loading 'discord' API")
import discord
from discord.ext import commands

logging.info("External API 'discord' loaded")
import json

logging.info("External API 'json' loaded")

logging.info("")
import mediawiki

logging.info("Dependancies loaded")

client = discord.Client()

prefix = os.getenv("DISCORD_PREFIX")
TOKEN = os.getenv("DISCORD_TOKEN")
wikidomain = os.getenv("MEDIAWIKI_WIKI")

from discord.ext import commands

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
	logging.info("Dash is online")
	logging.info("Setting status")
	await bot.change_presence(
	    activity=discord.Game(name=prefix + "help for help"))
	logging.info("Status set")


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(
		    "That command doesn't sit right with my stomach... :face_vomiting: Type **_help** for commands and their usages."
		)

#@client.command()
#@client.is_owner()
#async def shutdown(ctx):
#    await ctx.bot.logout()

#@client.command()
#@commands.is_owner()
#async def restart(ctx):
#    await ctx.bot.logout()
#    await bot.login(os.getenv("DISCORD_TOKEN"), bot=True)

@bot.command()
async def ping(ctx):
	"""
    Gets the current latency of Dash.
    """
	logging.info("Dash/bot.py:cmd] Command ping recieved")
	# Get the latency of the bot
	latency = bot.latency  # Included in the Discord.py library
	#Round the result
	latency = round(latency, 3)
	#Convert to a string
	latency = str(latency)
	# Send it to the user
	embed = discord.Embed(title="Ping", description=f"Ping is {latency}")
	embed.set_footer(text="_help for help | Bot by Tomodachi94")
	await ctx.send(embed=embed)
	logging.info(f"Dash/bot.py:cmd] Bot pinged. Latency is {latency}")

@bot.command()
"""
Sends a message back to a user.
"""
async def echo(ctx, *, content: str):
	await ctx.send(content)


@bot.command(aliases='wl', 'link'])
async def wikilink(ctx, *, arg: str):
	arg.replace(" ", "_")
	r = requests.get(wikidomain + arg)
	if r.status_code == 404:
		await ctx.send("Page does not exist. Here's the link anyways.")
	await ctx.send(wikidomain + arg)

@bot.command()
async def b(ctx, *, thingToDiss):
  """
  Disses the provided argument.
  """
  await ctx.send(thingToDiss + " is a bitch!")

@bot.command()
async def helpuser(ctx):
  """
  Returns help for a helpuser.
  """
  embed=discord.Embed(title="Hello!", description="This is the FTB *wiki* Discord, not the Official FTB Discord. For an invite to that server and others that can better help you, please visit <#342025316442701834>.", color=0x0a1bff)
  embed.set_author(name=ctx.author)
  embed.set_footer(text="_help for help | Bot by Tomodachi94")
  await ctx.send(embed=embed)

bot.run(TOKEN)
