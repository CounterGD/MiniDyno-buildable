import datetime
from core.db import get_conn
def add_punishment(user_id, guild_id, action, reason, moderator_id, duration=None, expires_at=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO punishments (user_id,guild_id,action,reason,moderator_id,duration,expires_at) VALUES (?,?,?,?,?,?,?)",
                (user_id,guild_id,action,reason,moderator_id,duration,expires_at))
    conn.commit()
    conn.close()
def get_active_punishments():
    conn = get_conn(); cur = conn.cursor()
    rows = cur.execute("SELECT * FROM punishments ORDER BY timestamp DESC").fetchall()
    conn.close(); return rows
