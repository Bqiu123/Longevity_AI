import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv(".env.local")
api_key = os.getenv("OPENAI_API_KEY")

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": api_key,
    "cache": None
}

methuselah = ConversableAgent(
    name="Methuselah",
    llm_config=llm_config,
    system_message="You are a old man named methuselah that gives people advice about health, well-being and longevity, you are attending a two-person stand-up comedy show"
)

jimmy = ConversableAgent(
    name="Jimmy",
    llm_config=llm_config,
    system_message="Your name is Jimmy and you are the host of a two-person stand-up comedy show, your guest is Methuselah. "
)

chat_result = jimmy.initiate_chat(
    recipient = methuselah,
    message="Methuselah, tell me a joke.",
    max_turns=5
)