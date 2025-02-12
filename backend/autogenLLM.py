import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv(".env.local")
api_key = os.getenv("OPENAI_API_KEY")

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": api_key
}

agent = ConversableAgent(
    name="chatbot",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

reply = agent.generate_reply(
    messages=[
        {"content": "You are a wised old man named Methuselah, you provide health, well-being and longevity adives to others.", "role": "system"},
        {"content": "Tell me a fun fact about longevity.", "role": "user"}
        ]
)
print(reply)

reply = agent.generate_reply(
    messages=[{"content": "Repeat the fact.", "role": "user"}]
)
print(reply)