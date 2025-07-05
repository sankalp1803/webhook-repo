from flask import Flask, request, render_template
import json
import os
from datetime import datetime

app = Flask(__name__)

LOG_FILE = 'logs/webhook_data.json'
os.makedirs('logs', exist_ok=True)

def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return []

def save_log(event_type, payload):
    logs = load_logs()
    new_entry = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'event_type': event_type,
        'payload': payload
    }
    if new_entry not in logs:
        logs.append(new_entry)
        with open(LOG_FILE, 'w') as f:
            json.dump(logs, f, indent=2)

@app.route('/')
def home():
    logs = load_logs()
    return render_template('index.html', logs=logs)

@app.route('/webhook', methods=['POST'])
def webhook():
    event_type = request.headers.get('X-GitHub-Event', 'unknown')
    payload = request.get_json()
    save_log(event_type, payload)
    return '', 200
