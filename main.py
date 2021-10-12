import os
import discord
import time
import discord.ext
import logging
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check


logger = logging.getLogger('Discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

client = commands.Bot(command_prefix = '$')
client.author_id = 487258918465306634

@client.event
async def on_ready():
    print(f"{client.user} is online")

@client.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(name="echo")
async def echo(ctx, *, arg):
	await ctx.send(arg)

@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://github.com/1rom11/-udbsh.discord.py", description="Code fot UDBSH", color=discord.Color.white())
    await ctx.send(embed=embed)


async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send(f"{client.user} has kicked "+member.mention)
    except:
        await ctx.send(f"{client.user} does not have the kick members permission! or user role is higher than {client.user}")
	#token setup
token = os.environ['token']
os.environ.get("token")
client.run(token)

#https://discordpy.readthedocs.io/en/master/