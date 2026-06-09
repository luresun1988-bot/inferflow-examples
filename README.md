# Inferflow Examples

Runnable examples for the Inferflow OpenAI-compatible API.

## Connection Values

```text
Base URL: https://api.inferflow.dev/v1
API key: use your Inferflow dashboard key
Recommended model: deepseek-v4-flash
Doubao quick test: doubao-seed-2.0-mini
```

## 1-minute Quickstart

1. Create an account at https://api.inferflow.dev/sign-up.
2. Create an API key in the dashboard.
3. Clone this repository:

```bash
git clone https://github.com/luresun1988-bot/inferflow-examples.git
cd inferflow-examples
```

4. Export the key:

```bash
export INFERFLOW_API_KEY="sk-your-key"
```

5. Run one of the examples:

```bash
bash curl/chat-completions.sh
```

## Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r python/requirements.txt
python python/openai_sdk.py
```

## JavaScript

```bash
cd javascript
npm install
INFERFLOW_API_KEY="sk-your-key" node openai_sdk.mjs
```

## LangChain

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r langchain/requirements.txt
python langchain/chat_openai.py
```

## Guides

- Cursor: `integrations/cursor.md`
- Dify: `integrations/dify.md`
- Open WebUI: `integrations/openwebui.md`
- Python SDK: `python/openai_sdk.py`
- JavaScript SDK: `javascript/openai_sdk.mjs`
- LangChain: `langchain/chat_openai.py`

## Model Names

Start here:

```text
deepseek-v4-flash
```

Higher-quality DeepSeek:

```text
deepseek-v4-pro
```

Doubao compatibility test:

```text
doubao-seed-2.0-mini
```

Use only model names visible in your Inferflow account.

## Troubleshooting

- `401 Unauthorized`: check `INFERFLOW_API_KEY` and the `Authorization: Bearer ...` header.
- `model_not_found`: use a model alias visible in your Inferflow Models page.
- `insufficient_balance`: open Billing, top up with Paddle, and retry after the balance updates.
- Wrong base URL: use exactly `https://api.inferflow.dev/v1`.

## Links

- Docs: https://inferflow.dev/docs/
- Examples page: https://inferflow.dev/examples/
- Model catalog: https://inferflow.dev/models/
- API Reference: https://inferflow.dev/docs/api-reference/

## Safety

Never commit real API keys. Use environment variables or your local secret manager.
