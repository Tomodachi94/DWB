# https://github.com/Tomodachi94/Dash
# Dash - A Discord bot for the FTB Gamepedia Discord.
# (c) Tomodachi94 2021 MIT License
# A full copy of the license should have been distrubuted with this program.
#  If not, the license can be found here:
# https://mit-license.org/

import logging

logging.info("Starting Dash...")
logging.info("Loading dependencies...")
import os, json, random
import mediawiki, discord, requests
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import badwords

logging.info("Dependancies loaded")

client = discord.Client()

version = "v1.1.0"
embedFooter = f"_help for help | Dash {version}"

bot = commands.Bot(command_prefix=os.getenv("DISCORD_PREFIX"))
logging.info("Dash is online")
logging.info("Setting status")
await bot.change_presence(
  activity=discord.Game(
      name=os.getenv("DISCORD_PREFIX") + "help for help"
logging.info("Status set")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(
            "That command doesn't sit right with my stomach... :face_vomiting: Type **_help** for commands and their usages."
        )


@bot.command()
@commands.has_permissions(kick_members=True) 
async def shutdown(ctx):
    """Shuts down the bot. Owner- and moderator-only.
    No arguments.
    """
    await ctx.send("Shutting down... G'night, Mom!")
    await ctx.bot.logout()


#@bot.command()
#@commands.is_owner()
#async def restart(ctx):
#    await ctx.bot.logout()
#    await bot.login(os.getenv("DISCORD_TOKEN"), bot=True)


@bot.command()
async def ping(ctx):
    """Gets the current latency of Dash.

    No arguments.
    """
    logging.info("Dash/bot.py:cmd] Command ping recieved")
    latency = bot.latency #Get the latency of the bot, courtesy of the Discord.py library
    latency = round(latency, 3) #Round the result
    latency = str(latency) #Convert to a string
    embed = discord.Embed(title="Ping", description=f"Ping is {latency}") # Send it to the user
    embed.set_footer(text="_help for help | Bot by Tomodachi94")
    await ctx.send(embed=embed)
    logging.info(f"Dash/bot.py:cmd] Bot pinged. Latency is {latency}.")


@bot.command()
async def echo(ctx, *, content: str):
    """Repeats something back.

    Args:
        content (str): The string you want repeated.
    """
    await ctx.send(content)


@bot.command(aliases=['wl', 'link'])
async def wikilink(ctx, *, linkToBeConverted: str):
    """Converts a string into a link on your wiki.

    Args:
        linkToBeConverted (str): The link to be converted.
    """
    linkToBeConverted.replace(" ", "_")
    r = requests.get(os.getenv("MEDIAWIKI_WIKI") + linkToBeConverted)
    if r.status_code == 404:
        await ctx.send("Page does not exist. Here's the link anyways.")
    await ctx.send(os.getenv("MEDIAWIKI_WIKI") + linkToBeConverted)


@bot.command(aliases=['b', 'bitch'])
async def diss(ctx, *, thingToDiss: str):
    """Disses the provided argument.

    Args:
        thingToDiss (str): The thing to diss.
    """
    insults = json.load(open('assets/json/insults.json',))
    await ctx.send(f"{thingToDiss} is a {random.choice(insults)} !")

@bot.command()
async def helpuser(ctx):
    """Returns help for a helpuser.
    """
    embed=discord.Embed(title="Hello!", description="This is the FTB *wiki* Discord, not the Official FTB Discord. For an invite to that server and others that can better help you, please visit <#342025316442701834>.", color=0x0a1bff)
    embed.set_author(name=ctx.author)
    embed.set_footer(text=embedFooter)
    await ctx.send(embed=embed)


@bot.command()
async def about(ctx):
    """Gives information about the bot.

    Args:
        None.
    """
    embed = discord.Embed(title="About Dash", description="""__Dash__ is a Discord bot for 
    [the Official FTB wiki](ftb.gamepedia.com)'s 
    [Discord](https://discord.gg/2Pq6Rft)
    inspired by SatanicSanta's [IRC wiki bot](https://github.com/FTB-Gamepedia/SatanicBot).""")
    embed.add_field(name="Source", value="[on GitHub](https://github.com/Tomodachi94/Dash)", inline=True)
    embed.add_field(name="Author", value="[Tomodachi94](https://tomodachi94.github.io)", inline=True)
    embed.add_field(name="Version", value=version, inline=True)
    embed.set_footer(text=embedFooter)
    await ctx.send(embed=embed)

bot.run(os.getenv("DISCORD_TOKEN"))

logging.info("Loading basic 'web server' to keep repl online")
import keepalive

keepalive.keepalive()