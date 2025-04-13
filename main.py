
import json
from flask import Flask, request
import requests

app = Flask(__name__)

# Telegram Bot Setup
TELEGRAM_BOT_TOKEN = "7319745922:AAFH2bSLHvRcJgQ6KnxBVdeEmxdyPwmaUew"
TELEGRAM_CHAT_ID = "-1002174325669"

# Signal Message Formatter
def format_message(data):
    pair = data.get("ticker", "Unknown")
    signal_type = data.get("signal", "Signal")
    entry = data.get("entry", "N/A")
    sl = data.get("sl", "N/A")
    tp1 = data.get("tp1", "N/A")
    tp2 = data.get("tp2", "N/A")
    tp3 = data.get("tp3", "N/A")

    return f"""
🚀 <b>AMFX Trader</b>
<b>{signal_type}</b> Signal – {pair}

📍<b>Entry:</b> {entry}
🔻<b>SL:</b> {sl}
🎯<b>TP1:</b> {tp1}
🎯<b>TP2:</b> {tp2}
🎯<b>TP3:</b> {tp3}

🟢<b>Status:</b> Signal Active
"""

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received data:", data)
    message = format_message(data)
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(url, json=payload)
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
# Webhook system for AMFX signals  ← ye comment add kar do
