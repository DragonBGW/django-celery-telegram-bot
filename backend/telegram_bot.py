import requests
import time
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from api.models import TelegramUser

# Replace this with the token you got from BotFather
BOT_TOKEN = "7585968322:AAHRW35MUL6ZOFZee39B7dgkU_HcQPt1AKE"
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates(offset=None):
    url = f"{BASE_URL}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    return requests.get(url, params=params).json()

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, data=payload)

def handle_update(update):
    message = update.get("message")
    if not message:
        return

    chat = message["chat"]
    text = message.get("text", "")
    
    if text == "/start":
        tg_id = str(chat["id"])
        username = chat.get("username")
        first_name = chat.get("first_name")

        # Save to DB if new
        user, created = TelegramUser.objects.get_or_create(
            telegram_id=tg_id,
            defaults={"username": username, "first_name": first_name},
        )

        if created:
            send_message(tg_id, f"Hello {first_name}, you've been registered!")
        else:
            send_message(tg_id, "You're already registered!")

def main():
    offset = None
    print("Bot is polling... Press Ctrl+C to stop.")
    while True:
        updates = get_updates(offset)
        for update in updates.get("result", []):
            offset = update["update_id"] + 1
            handle_update(update)
        time.sleep(1)

if __name__ == "__main__":
    main()
