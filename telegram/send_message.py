import requests
import os

def send_to_telegram(text):
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    res = requests.post(url, json=payload)
    print("[TELEGRAM] Wysłano:", res.status_code)
