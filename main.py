# main.py
# Entry point for the application.

import datetime

# Automatically sets up logging on import
import src.logging as logging # type: ignore
logging.initialize_logging()

PRINT_PREFIX = "MAIN"

from config.config import DISCORD_BOT_TOKEN, DISCORD_HOME_GUILD_ID
from src.bot import bot

@bot.event
async def on_ready():

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print startup information
    print(f"[INFO] [{PRINT_PREFIX}] Bot is online")
    print(f"[INFO] [{PRINT_PREFIX}] Time: {now} UTC")
    print(f"[INFO] [{PRINT_PREFIX}] Logged in as: {bot.user} (ID: {bot.user.id})")
    print(f"[INFO] [{PRINT_PREFIX}] Connected to {len(bot.guilds)} guild(s)")
    print("="*50)
    
    # Sync command tree
    print(f"[INFO] [{PRINT_PREFIX}] Syncing command tree...")
    try:
        synced = await bot.tree.sync()
        print(f"[INFO] [{PRINT_PREFIX}] Successfully synced {len(synced)} command(s)")
    except Exception as e:
        print(f"[ERROR] [{PRINT_PREFIX}] Failed to sync commands: {e}")
        print(f"[WARNING] [{PRINT_PREFIX}] Bot will continue running but slash commands may not be available")
    
    # Sync everything to home guild
    home_guild = bot.get_guild(DISCORD_HOME_GUILD_ID)
    if home_guild:
        try:
            synced = await bot.tree.sync(guild=home_guild)
            print(f"[INFO] [{PRINT_PREFIX}] Successfully synced {len(synced)} command(s) to home guild '{home_guild.name}' (ID: {DISCORD_HOME_GUILD_ID})")
        except Exception as e:
            print(f"[ERROR] [{PRINT_PREFIX}] Failed to sync commands to home guild: {e}")
    else:
        print(f"[WARNING] [{PRINT_PREFIX}] Home guild with ID {DISCORD_HOME_GUILD_ID} not found among connected guilds")

    print("="*50)
    print(f"[WARNING] [{PRINT_PREFIX}] Bot completed startup sequence at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} UTC")
    
bot.run(DISCORD_BOT_TOKEN)