import os, discord, time, random, asyncio, json, logging
from discord.ext import commands
from dotenv import load_dotenv


logger = logging.getLogger('Discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

def get_prefix(client, message):
	with open ('prefix.json' , 'r') as f:
		prefixes = json.load(f)
	return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix = get_prefix, help_command=None, case_insensitive=True)
client.author_id = 487258918465306634

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='Terminal', url="https://twitch.tv/1rom111"))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

@client.event
async def on_guild_join(guild):
	with open ('prefix.json' , 'r') as f:
		prefixes = json.load(f)
	prefixes[str(guild.id)] = '$'

	with open ('prefix.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
	with open ('prefix.json' , 'r') as f:
		prefixes = json.load(f)

	prefixes.pop(str(guild.id))

	with open ('prefix.json', 'w') as f:
		json.dump(prefixes, f, indent=4)

@client.command(name="help")
async def help(ctx: commands.Context):
	embed=discord.Embed(title="Help", description="All commands", color=0xffffff)
	embed.set_author(name="1rom11")
	embed.add_field(name="Code", value="Shows github code for UDBSH", inline=False)
	embed.add_field(name="Invite", value="Sends invite link for UDBSH", inline=False)
	embed.add_field(name="Echo", value="sends what ever in (arg) back", inline=False)
	embed.add_field(name="Rnt", value="In a random time sends a message", inline=False)
	await ctx.send(embed=embed)

@client.command(name="invite")
async def invite(ctx: commands.Context):
	await ctx.send(f"`The invite link for {client.user} is` ||https://bit.ly/UDBSH-invite||")
@client.command(name="ping")
async def ping(ctx: commands.Context):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(name="echo")
async def echo(ctx, *, arg):
	await ctx.send(f"`{arg}`")

@client.command(name="trello")
async def trello(ctx):
	await ctx.send(f"`Trello page = https://trello.com/b/IiUj4tjb/udbsh`")

@client.command()
async def rnt(ctx):    
    async with ctx.typing():
	
        type_time = random.uniform(0.5, 2)
        await asyncio.sleep(type_time)
    
    await ctx.send('`Type time = {} seconds`'.format(round(type_time, 2)))
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send(f"{client.user} has kicked "+member.mention)
    except:
        await ctx.send(f"{client.user} does not have the kick members permission! or user role is higher than {client.user} or {ctx.author}")
	#token setup
token = os.environ['token']
os.environ.get("token")
client.run(token)

#https://discordpy.readthedocs.io/en/master/
#https://cog-creators.github.io/discord-embed-sandbox/