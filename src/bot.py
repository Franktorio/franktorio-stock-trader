# src/bot.py
# Bot object builder

PRINT_PREFIX = "BOT BUILDER"

# Third-party imports
import discord
from discord.ext import commands

# Create intents with ALL intents enabled
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",  # Default prefix, can be changed later
    intents=intents
)

print(f"[DEBUG] [{PRINT_PREFIX}] Bot initialized with all intents enabled.")