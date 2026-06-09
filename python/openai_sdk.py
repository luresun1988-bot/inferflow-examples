import os

from openai import OpenAI


client = OpenAI(
    api_key=os.environ["INFERFLOW_API_KEY"],
    base_url=os.environ.get("INFERFLOW_BASE_URL", "https://api.inferflow.dev/v1"),
)

model = os.environ.get("INFERFLOW_MODEL", "deepseek-v4-flash")

response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "user", "content": "Reply in one sentence: Inferflow setup works."}
    ],
)

print(response.choices[0].message.content)
