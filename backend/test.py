import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env.local
load_dotenv("backend/.env.local")

api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is actually loaded
if not api_key:
    raise ValueError("API key is missing! Check .env.local and make sure it's correctly loaded.")

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)
