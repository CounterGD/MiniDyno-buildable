import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).resolve().parents[0].parent / 'data' / 'modbot.db'
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
def get_conn():
    conn = sqlite3.connect(DB_PATH.as_posix(), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS punishments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        guild_id INTEGER,
        action TEXT,
        reason TEXT,
        moderator_id INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        duration INTEGER,
        expires_at DATETIME
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS bad_words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pattern TEXT NOT NULL
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS user_strikes (
        guild_id INTEGER,
        user_id INTEGER,
        strikes INTEGER DEFAULT 0,
        PRIMARY KEY (guild_id, user_id)
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS strike_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        guild_id INTEGER,
        user_id INTEGER,
        action TEXT,
        reason TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()
