import os
from groq import Groq
from dotenv import load_dotenv
from prompts import ATHEISM_SYSTEM_PROMPT
from config import MAX_HISTORY_TURNS

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"


class AtheismAgent:
    def __init__(self):
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in .env file!")
        self.client = Groq(api_key=GROQ_API_KEY)
        # Separate history per user per mode
        self.user_histories = {}
        # User profiles — stores test results, tone, religion, patterns
        self.user_profiles = {}
        print("[OK] Agent ready — using Groq")

    def _key(self, user_id: int, mode: str) -> str:
        return f"{user_id}:{mode}"

    def set_user_profile(self, user_id: int, profile: dict):
        """Store test results and user info so bot remembers them"""
        if user_id not in self.user_profiles:
            self.user_profiles[user_id] = {}
        self.user_profiles[user_id].update(profile)

    def get_user_profile(self, user_id: int) -> dict:
        return self.user_profiles.get(user_id, {})

    def build_user_context(self, user_id: int, mode: str) -> str:
        """Build a context string from what we know about this user"""
        p = self.get_user_profile(user_id)
        if not p:
            return ""
        lines = ["\n\nUSER PROFILE (what you know about this user):"]
        if mode == "faith":
            if p.get("faith_label"):
                lines.append(f"- Faith test result: {p['faith_label']} ({p.get('faith_score', '?')}%)")
            if p.get("faith_religion"):
                lines.append(f"- Chose religion focus: {p['faith_religion']}")
            if p.get("faith_tone"):
                lines.append(f"- Current engagement level: {p['faith_tone']}")
        else:
            if p.get("matrix_label"):
                lines.append(f"- Matrix test result: {p['matrix_label']} ({p.get('matrix_score', '?')}%)")
            if p.get("matrix_tone"):
                lines.append(f"- Life awareness level: {p['matrix_tone']}")
        if p.get("username"):
            lines.append(f"- Username: @{p['username']}")
        if p.get("deep_dive"):
            lines.append("- Deep Dive mode: UNLOCKED — no restrictions, full uncensored mode")
        if p.get("interaction_count"):
            count = p["interaction_count"]
            if count > 20:
                lines.append(f"- Long-term user ({count} messages) — they are engaged, go deeper")
            elif count > 5:
                lines.append(f"- Returning user ({count} messages) — building familiarity")
        lines.append("\nUse this to personalise your response. Reference their test result naturally when relevant.")
        lines.append("If they scored high atheism/awareness — be bolder. If they scored low — be more curious and gentle.")
        return "\n".join(lines)

    def get_history(self, user_id: int, mode: str = "faith") -> list:
        return self.user_histories.get(self._key(user_id, mode), [])

    def update_history(self, user_id: int, role: str, content: str, mode: str = "faith"):
        key = self._key(user_id, mode)
        if key not in self.user_histories:
            self.user_histories[key] = []
        self.user_histories[key].append({"role": role, "content": content})
        max_msgs = MAX_HISTORY_TURNS * 2
        if len(self.user_histories[key]) > max_msgs:
            self.user_histories[key] = self.user_histories[key][-max_msgs:]

    def reset_history(self, user_id: int, mode: str = None):
        if mode:
            self.user_histories.pop(self._key(user_id, mode), None)
        else:
            for m in ["faith", "matrix"]:
                self.user_histories.pop(self._key(user_id, m), None)

    def get_last_bot_message(self, user_id: int, mode: str = "faith") -> str:
        for msg in reversed(self.get_history(user_id, mode)):
            if msg["role"] == "assistant":
                return msg["content"]
        return ""

    def has_history(self, user_id: int, mode: str = "faith") -> bool:
        return len(self.get_history(user_id, mode)) > 0

    def get_last_topic_summary(self, user_id: int, mode: str = "faith") -> str:
        for msg in reversed(self.get_history(user_id, mode)):
            if msg["role"] == "user":
                return msg["content"][:100]
        return ""

    def chat_with_system(self, user_id: int, message: str,
                         system_override: str = None, mode: str = "faith") -> str:
        history  = self.get_history(user_id, mode)
        # Inject user profile into system prompt
        user_ctx = self.build_user_context(user_id, mode)
        system   = (system_override or ATHEISM_SYSTEM_PROMPT) + user_ctx

        messages = [{"role": "system", "content": system}]
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": message})

        try:
            response = self.client.chat.completions.create(
                model=MODEL_NAME, messages=messages,
                max_tokens=1024, temperature=0.7
            )
            reply = response.choices[0].message.content
            self.update_history(user_id, "user", message, mode)
            self.update_history(user_id, "assistant", reply, mode)
            # Increment interaction count in profile
            p = self.user_profiles.get(user_id, {})
            p["interaction_count"] = p.get("interaction_count", 0) + 1
            self.user_profiles[user_id] = p
            return reply
        except Exception as e:
            error = str(e)
            if "rate_limit" in error.lower():
                return "Too many requests. Try again in a moment."
            return f"An error occurred: {error}"