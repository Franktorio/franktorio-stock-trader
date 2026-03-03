# src/db/bot_db/schema.py
# Schema definition for the bot database

DB_FILE_NAME = "bot_db.db"

SCHEMA = {
    # Table to store all transactions (buys/sells) made by the bot, along with reasons and timestamps
    "transactions": """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stock_symbol TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        transaction_type TEXT NOT NULL,
        category TEXT NOT NULL,
        reason TEXT NOT NULL,
        timestamp INTEGER DEFAULT (strftime('%s', 'now')),
        FOREIGN KEY (stock_symbol) REFERENCES stock_mapping(stock_symbol)
    );
    """,

    # Table to store the current portfolio holdings of the bot, updated after each transaction or regularly when fetching latest prices
    "portfolio": """
    CREATE TABLE IF NOT EXISTS portfolio (
        stock_symbol TEXT PRIMARY KEY,
        quantity INTEGER NOT NULL,
        average_price REAL NOT NULL,
        latest_price REAL NOT NULL,
        last_updated INTEGER DEFAULT (strftime('%s', 'now')),
        FOREIGN KEY (stock_symbol) REFERENCES stock_mapping(stock_symbol)
    );
    """,

    # Table to store a summary of historical performance of the bot, updated after each transaction or at regular intervals
    "performance": """
    CREATE TABLE IF NOT EXISTS performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        stocks_held TEXT NOT NULL,
        portfolio_value REAL NOT NULL,
        cash_value REAL NOT NULL,
        total_value REAL NOT NULL,
        strongest_sector TEXT NOT NULL,
        timestamp INTEGER DEFAULT (strftime('%s', 'now'))
    );
    """,

    # Table to store the performance metrics of different sectors (e.g. tech, energy, etc.) for better analysis and decision-making
    "sector_performance": """
    CREATE TABLE IF NOT EXISTS sector_performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        current_slope REAL NOT NULL,
        volatility REAL NOT NULL,
        is_strongest INTEGER NOT NULL,
        timestamp INTEGER DEFAULT (strftime('%s', 'now'))
    );
    """,

    # Table to map stock symbols to their categories (e.g. tech, energy, etc.) for better analysis and decision-making
    "stock_mapping": """
    CREATE TABLE IF NOT EXISTS stock_mapping (
        stock_symbol TEXT PRIMARY KEY,
        category TEXT NOT NULL
    );
    """,

    "account_meta": """
    CREATE TABLE IF NOT EXISTS account_meta (
        id INTEGER PRIMARY KEY CHECK (id = 1), -- Only one row for this table since it's just for storing account-level metadata
        cash_balance REAL NOT NULL,
        buying_power REAL NOT NULL,
        last_updated INTEGER DEFAULT (strftime('%s', 'now'))
    );
    """
}