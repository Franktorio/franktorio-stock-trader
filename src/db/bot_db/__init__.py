"""
Database module that holds all the internal API functions for bot_db.db:
1. Querying the bot_db.db database
2. Inserting/updating data in the bot_db.db database
3. Any other helper functions related to the bot_db.db database
"""

from ..connections import connect_db
from .schema import DB_FILE_NAME, SCHEMA # Schema is imported because its used on the db init process

def connect_grader_db():
    """Connect to the grader database."""
    return connect_db(DB_FILE_NAME)

def connect_grader_db_ro():
    """Connect to the grader database in read-only mode."""
    return connect_db(DB_FILE_NAME, read_only=True)
