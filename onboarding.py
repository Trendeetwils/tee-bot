"""
onboarding.py — Tracks user onboarding state and belief profile
"""
import json, os

USERS_FILE = "users.json"

def _load():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def _save(data):
    with open(USERS_FILE, "w") as f:
        json.dump(data, f)

def is_onboarded(user_id: int) -> bool:
    data = _load()
    return str(user_id) in data and data[str(user_id)].get("onboarded", False)

def get_user(user_id: int) -> dict:
    data = _load()
    return data.get(str(user_id), {})

def set_user(user_id: int, profile: dict):
    data = _load()
    data[str(user_id)] = profile
    _save(data)

def save_mode(user_id: int, mode: str):
    data = _load()
    key = str(user_id)
    if key not in data:
        data[key] = {}
    data[key]["mode"] = mode
    _save(data)

def get_mode(user_id: int) -> str:
    data = _load()
    return data.get(str(user_id), {}).get("mode", "faith")

def complete_onboarding(user_id: int, religion: str, score: int, total: int, label: str):
    percentage = round((score / (total * 5)) * 100)
    # Assign tone mode based on score
    if percentage <= 30:
        tone = "gentle"       # Curious and respectful — spark doubt slowly
    elif percentage <= 60:
        tone = "analytical"   # Direct, introduce contradictions
    else:
        tone = "provocative"  # Bold, confrontational, sharp

    profile = {
        "onboarded": True,
        "religion": religion,
        "score": percentage,
        "label": label,
        "tone": tone,
        "interaction_count": 0,
    }
    set_user(user_id, profile)
    return profile

def increment_interactions(user_id: int):
    data = _load()
    key = str(user_id)
    if key in data:
        data[key]["interaction_count"] = data[key].get("interaction_count", 0) + 1
        # Gradually escalate tone based on interactions
        count = data[key]["interaction_count"]
        current_tone = data[key].get("tone", "gentle")
        if current_tone == "gentle" and count >= 5:
            data[key]["tone"] = "analytical"
        elif current_tone == "analytical" and count >= 15:
            data[key]["tone"] = "provocative"
        _save(data)
        return data[key]
    return {}

def get_tone(user_id: int) -> str:
    return get_user(user_id).get("tone", "analytical")

def get_religion(user_id: int) -> str:
    return get_user(user_id).get("religion", "all") 