# config/config.py
# Helper functions to read and parse environment variables for configuration

import os
import sys
from typing import Optional, Sequence
from dotenv import load_dotenv

PRINT_PREFIX = "CONFIG"

# Load environment variables from .env file
env_file = os.getenv('ENV_FILE', '.env')
env_path = os.path.join(os.path.dirname(__file__), env_file)
load_dotenv(env_path)

def _get_env_int(key: str, default: Optional[int | str] = None) -> int:
    """Helper function to get integer from environment with error handling"""
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Required environment variable {key} not found")
    try:
        print(f"[INFO] [{PRINT_PREFIX}] Loaded integer env var {key}={value}")
        return int(value)
    except ValueError:
        raise ValueError(f"Environment variable {key} must be a valid integer, got: {value}")

def _get_env_int_list(key: str, default: Optional[Sequence[int] | str] = None) -> list[int]:
    """Helper function to get comma-separated integers from environment"""
    value = os.getenv(key)
    if value is None:
        if default is None:
            raise ValueError(f"Required environment variable {key} not found")
        if isinstance(default, (list, tuple)):
            print(f"[INFO] [{PRINT_PREFIX}] Using default integer list for env var {key}={default}")
            return [int(x) for x in default]
        value = str(default)
    try:
        print(f"[INFO] [{PRINT_PREFIX}] Loaded integer list env var {key}={value}")
        return [int(x.strip()) for x in value.split(',') if x.strip()]
    except ValueError:
        raise ValueError(f"Environment variable {key} must be comma-separated integers, got: {value}")

def _get_env_str_list(key: str, default: Optional[Sequence[str] | str] = None) -> list[str]:
    """Helper function to get comma-separated strings from environment"""
    value = os.getenv(key)
    if value is None:
        if default is None:
            raise ValueError(f"Required environment variable {key} not found")
        if isinstance(default, (list, tuple)):
            print(f"[INFO] [{PRINT_PREFIX}] Using default string list for env var {key}={default}")
            return [str(x) for x in default]
        value = str(default)
    print(f"[INFO] [{PRINT_PREFIX}] Loaded string list env var {key}={value}")
    return [x.strip() for x in value.split(',') if x.strip()]
    
def _get_env_bool(key: str, default: Optional[bool | str] = None) -> bool:
    """Helper function to get boolean from environment"""
    value = os.getenv(key)
    if value is None:
        if default is None:
            raise ValueError(f"Required environment variable {key} not found")
        value = str(default)
        print(f"[INFO] [{PRINT_PREFIX}] Using default boolean env var {key}={value}")
    else:
        print(f"[INFO] [{PRINT_PREFIX}] Loaded boolean env var {key}={value}")
    return value.lower() in ('true', '1', 'yes')

# General Configuration
OPERATING_MODE = os.getenv('OPERATING_MODE', 'development')

# API Configuration
API_ENABLED = _get_env_bool('API_ENABLED', 'true')
API_PORT = _get_env_int('API_PORT', '8000')
API_SECRET_KEY = os.getenv('API_SECRET_KEY', 'supersecretkey_PLEASE_CHANGE_ME')
print(f"[INFO] [{PRINT_PREFIX}] API configuration loaded (enabled={API_ENABLED}, port={API_PORT})")

# Database Configuration
DB_REPLICA_SYNC_INTERVAL = _get_env_int('DB_REPLICA_SYNC_INTERVAL', '300')  # seconds
DB_SNAPSHOT_INTERVAL = _get_env_int('DB_SNAPSHOT_INTERVAL', '3600')  # seconds
DB_SNAPSHOT_RETENTION_COUNT = _get_env_int('DB_SNAPSHOT_RETENTION_COUNT', '72')
DB_HEALTH_CHECK_INTERVAL = _get_env_int('DB_HEALTH_CHECK_INTERVAL', '120')  # seconds
print(f"[INFO] [{PRINT_PREFIX}] Database configuration loaded (snapshot interval={DB_SNAPSHOT_INTERVAL}s, replica sync={DB_REPLICA_SYNC_INTERVAL}s)")

# Bot Configuration
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN', 'your_discord_bot_token_here')
DISCORD_OWNER_ID = _get_env_int('DISCORD_OWNER_ID', 'your_discord_user_id_here')
DISCORD_HOME_GUILD_ID = _get_env_int('DISCORD_HOME_GUILD_ID', 'your_discord_guild_id_here')
print(f"[INFO] [{PRINT_PREFIX}] Bot configuration loaded (Discord token length={len(DISCORD_BOT_TOKEN)}, owner ID={DISCORD_OWNER_ID}, home guild ID={DISCORD_HOME_GUILD_ID})")

# ALPACA Configuration
ALPACA_API_KEY = os.getenv('ALPACA_API_KEY', 'your_alpaca_api_key_here')
ALPACA_API_SECRET_KEY = os.getenv('ALPACA_API_SECRET_KEY', 'your_alpaca_api_secret_key_here')
print(f"[INFO] [{PRINT_PREFIX}] ALPACA configuration loaded (API key length={len(ALPACA_API_KEY)}, secret key length={len(ALPACA_API_SECRET_KEY)})")