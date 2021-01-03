# bot.py
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'


print("[Dash/bot.py] Starting Dash...")
print("[Dash/bot.py:dep] Loading essential dependencies...")
#Required Deps
print("[Dash/bot.py:dep] Loading 'os' API")
import os
print(bcolors.OKGREEN + "[Dash/bot.py:dep] External API 'os' loaded" +
      bcolors.ENDC)
print("[Dash/bot.py:dep] Loading 'requests' API")
import requests
print(bcolors.OKGREEN + "[Dash/bot.py:dep] External API 'requests' loaded" +
      bcolors.ENDC)
print("[Dash/bot.py:dep] Loading 'flask' API")
import flask
print(bcolors.OKGREEN + "[Dash/bot.py:dep] External API 'flask' loaded" +
      bcolors.ENDC)
print("[Dash/bot.py:dep] Loading 'discord' API")
import discord
from discord.ext import commands
print(bcolors.OKGREEN + "[Dash/bot.py:dep] External API 'discord' loaded" +
      bcolors.ENDC)
print("[Dash/bot.py:dep] Loading 'dotenv' API")
import dotenv
print("[Dash/bot.py:dep] Loading 'load_dotenv' from 'dotenv' API")
from dotenv import load_dotenv
print(bcolors.OKGREEN + "[Dash/bot.py:dep] External API 'dotenv' loaded" +
      bcolors.ENDC)
print("[Dash/bot.py:dep] Loading 'json' API")
import json
print(bcolors.OKGREEN + "[Dash/bot.py:dep] External API 'json' loaded" +
      bcolors.ENDC)
#Slightly Less Required Deps
##None yet
#APIs
import mediawiki
print(bcolors.OKGREEN + "[Dash/bot.py] Dependancies loaded" + bcolors.ENDC)
#KeepAlive
print("[Dash/keepalive.py] Loading KeepAlive")
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
	return "Your Bot Is Ready"


def run():
	app.run(host="0.0.0.0", port=8000)


def keep_alive():
	server = Thread(target=run)
	server.start()


#print("[Dash/keepalive.py] KeepAlive loaded!")

client = discord.Client()

def chlock():
  if ctx.channel.id != 319925398949330945:
    return


print("[Dash/bot.py:dotenv] Reading .env file for config")
#.env variables
load_dotenv()

prefix = os.getenv("DISCORD_PREFIX")
TOKEN = os.getenv("DISCORD_TOKEN")
wikidomain = os.getenv("MEDIAWIKI_WIKI")

from discord.ext import commands

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
	print("[Dash/bot.py] Dash is online")
	print("[Dash/bot.py:Status] Setting status")
	await bot.change_presence(
	    activity=discord.Game(name=prefix + "help for help"))
	print(bcolors.OKGREEN + "[Dash/bot.py:Status] Status set" + bcolors.ENDC)


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send(
		    "That command doesn't sit right with my stomach... :face_vomiting: Type **_help** for commands and their usages."
		)


@bot.command()
async def ping(ctx):
	'''
    Gets the current latency of Dash.
    '''
	print("[Dash/bot.py:cmd] Command ping recieved")
	# Get the latency of the bot
	latency = bot.latency  # Included in the Discord.py library
	#Round the result
	latency = round(latency, 3)
	#Convert to a string
	latency = str(latency)
	# Send it to the user
	embed = discord.Embed(title="Ping", description="Ping is " + latency)
	embed.set_footer(text="_help for help | Bot by Tomodachi94")
	await ctx.send(embed=embed)
	print("[Dash/bot.py:cmd] Bot pinged. Latency is " + latency)


@bot.command()
async def echo(ctx, *, content: str):
	chlock()
	await ctx.send(content)


@bot.command(aliases=['wl', 'link'])
async def wikilink(ctx, arg: str):
	r = requests.get(wikidomain + arg)
	if r.status_code == 404:
		await ctx.send("Page does not exist. Here's the link anyways.")
	await ctx.send(wikidomain + arg)

@bot.command()
async def b(ctx):
  """
  Formerly called an argument a b*@*%*, was later removed at the request of Xbony2.
  """
  await ctx.send("This command was removed at the request of Xbony2.")

@bot.command()
async def helpuser(ctx):
  """
  Returns help for a helpuser.
  """
  embed=discord.Embed(title="Hello helpuser!", description="This is the FTB *wiki* Discord, not the Official FTB Discord. For an invite to that server and others, please visit <#342025316442701834>.", color=0x0a1bff)
  embed.set_author(name=ctx.author)
  embed.set_footer(text="_help for help | Bot by Tomodachi94")
  await ctx.send(embed=embed)

bot.run(TOKEN)
