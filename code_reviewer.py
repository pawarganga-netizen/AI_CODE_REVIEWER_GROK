from openai import OpenAI
import os
from dotenv import load_dotenv
from prompt import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROK_API_KEY"),
    base_url="https://api.x.ai/v1"
)

def review_code(code):
    response = client.chat.completions.create(
        model="grok-4",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": code
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content