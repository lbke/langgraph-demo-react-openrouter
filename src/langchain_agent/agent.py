import os
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],

    base_url="https://openrouter.ai/api/v1",
    name="mistralai/codestral-2508"
)
agent = create_agent(
    model=model,
)
