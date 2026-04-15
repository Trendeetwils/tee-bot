"""
referral.py — Tracks referrals per user in a simple JSON file
"""

import json
import os

REFERRAL_FILE = "referrals.json"
UNLOCK_THRESHOLD = 3  # friends needed to unlock deep dive


def _load():
    if not os.path.exists(REFERRAL_FILE):
        return {}
    with open(REFERRAL_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(REFERRAL_FILE, "w") as f:
        json.dump(data, f)

def get_referral_link(bot_username: str, user_id: int) -> str:
    return f"https://t.me/{bot_username}?start=ref_{user_id}"

def record_referral(referred_by: int):
    data = _load()
    key = str(referred_by)
    data[key] = data.get(key, 0) + 1
    _save(data)

def get_referral_count(user_id: int) -> int:
    data = _load()
    return data.get(str(user_id), 0)

def is_unlocked(user_id: int) -> bool:
    return get_referral_count(user_id) >= UNLOCK_THRESHOLD
