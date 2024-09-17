import discord
from discord.ext import commands
import commands  # Import the commands module

# Create bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Load commands
commands.setup(bot)

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')