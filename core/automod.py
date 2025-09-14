import re, datetime
from core.db import get_conn
from core.punishments import add_punishment
from collections import defaultdict
user_messages = defaultdict(list)
def load_patterns():
    conn = get_conn(); cur = conn.cursor()
    rows = cur.execute("SELECT pattern FROM bad_words").fetchall()
    conn.close()
    return [re.compile(r['pattern'], re.IGNORECASE) for r in rows]
BAD_PATTERNS = load_patterns()
def is_bad_message(content):
    for pat in BAD_PATTERNS:
        if pat.search(content): return True
    return False
def record_message_and_check_spam(user_id):
    now = datetime.datetime.utcnow().timestamp()
    lst = user_messages[user_id]
    lst.append(now)
    user_messages[user_id] = [t for t in lst if now - t < 5]
    return len(user_messages[user_id]) > 6
