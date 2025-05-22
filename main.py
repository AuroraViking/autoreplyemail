### main.py
```python
from gmail_service import get_unread_messages, create_draft
from openai_reply import generate_reply
from filters import is_spam_or_newsletter

def main():
    print("Starting Aurora Reply Assistant...")
    messages = get_unread_messages()
    print(f"Found {len(messages)} messages.")
    for msg in messages:
        if is_spam_or_newsletter(msg):
            print(f"Skipped spam/newsletter: {msg['id']}")
            continue
        print(f"Processing message ID: {msg['id']}")
        reply = generate_reply(msg)
        create_draft(msg, reply)
        print(f"Draft created for message ID: {msg['id']}")

if __name__ == "__main__":
    main()
```# Main logic goes here
