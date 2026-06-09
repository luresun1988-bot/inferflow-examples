import os

from langchain_openai import ChatOpenAI


llm = ChatOpenAI(
    api_key=os.environ["INFERFLOW_API_KEY"],
    base_url=os.environ.get("INFERFLOW_BASE_URL", "https://api.inferflow.dev/v1"),
    model=os.environ.get("INFERFLOW_MODEL", "deepseek-v4-flash"),
)

response = llm.invoke("Reply in one sentence: Inferflow setup works.")
print(response.content)
