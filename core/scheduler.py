import asyncio, datetime
from core.db import get_conn
async def check_expired(bot):
    await bot.wait_until_ready()
    while True:
        conn = get_conn(); cur = conn.cursor()
        now = datetime.datetime.utcnow().isoformat()
        rows = cur.execute("SELECT id, user_id, guild_id, action FROM punishments WHERE expires_at IS NOT NULL AND expires_at <= ?", (now,)).fetchall()
        for r in rows:
            pid = r['id']; user_id = r['user_id']; guild_id = r['guild_id']; action=r['action']
            try:
                g = bot.get_guild(guild_id)
                if action=='mute' and g:
                    m = g.get_member(user_id)
                    if m: await m.timeout(None)
                if action=='ban' and g:
                    await g.unban(await bot.fetch_user(user_id))
            except Exception as e:
                print('scheduler error', e)
            cur.execute('DELETE FROM punishments WHERE id=?', (pid,))
            conn.commit()
        conn.close()
        await asyncio.sleep(30)
