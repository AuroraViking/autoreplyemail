### filters.py
```python
def is_spam_or_newsletter(msg):
    headers = msg.get("payload", {}).get("headers", [])
    for h in headers:
        name = h.get("name", "").lower()
        value = h.get("value", "").lower()
        if "unsubscribe" in value or "list-unsubscribe" in name:
            return True
    return False
```# Spam/newsletter filter logic
