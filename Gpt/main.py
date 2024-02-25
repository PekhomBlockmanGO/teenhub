import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.commands = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello! I am your friendly bot.')

# Add more commands as needed

# Start the bot
keep_alive()
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'
bot.run(TOKEN)
