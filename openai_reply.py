### openai_reply.py
```python
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_reply(message):
    snippet = message.get("snippet", "")
    prompt = f"""You are Kolbeinn, a friendly, playful, and professional Icelandic tour guide from Aurora Viking. Write a warm and helpful reply to this message:

{snippet}

Reply:
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8
    )
    return response.choices[0].message.content.strip()
```
# OpenAI reply generator
