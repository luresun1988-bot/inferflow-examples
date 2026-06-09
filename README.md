# Inferflow Examples

Copy-ready examples for the Inferflow OpenAI-compatible API.

## Connection Values

```text
Base URL: https://api.inferflow.dev/v1
API key: use your Inferflow dashboard key
Recommended model: deepseek-v4-flash
Doubao quick test: doubao-seed-2.0-mini
```

## Quickstart

1. Create an account at https://api.inferflow.dev/sign-up.
2. Create an API key in the dashboard.
3. Export the key:

```bash
export INFERFLOW_API_KEY="sk-your-key"
```

4. Run one of the examples:

```bash
bash curl/chat-completions.sh
python python/openai_sdk.py
node javascript/openai_sdk.mjs
python langchain/chat_openai.py
```

## Guides

- Cursor: `integrations/cursor.md`
- Dify: `integrations/dify.md`
- Open WebUI: `integrations/openwebui.md`
- Python SDK: `python/openai_sdk.py`
- JavaScript SDK: `javascript/openai_sdk.mjs`
- LangChain: `langchain/chat_openai.py`

## Safety

Never commit real API keys. Use environment variables or your local secret manager.
