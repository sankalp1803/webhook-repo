# Webhook Receiver

This Flask app listens to GitHub Webhooks and displays event logs in a web UI.

## Run Locally

```bash
pip install flask
python app.py
```

Endpoint: `http://localhost:5000/webhook`

## Webhook Setup

On your GitHub repo, go to:
Settings → Webhooks → Add webhook  
Payload URL: `http://<your-public-url>/webhook`  
Content type: `application/json`  
Events: push, pull_request, (optional: merge)

## Bonus Points

Merge detection included via `"action": "closed"` and `"merged": true` inside `pull_request` payloads.