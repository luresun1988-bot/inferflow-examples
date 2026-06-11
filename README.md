# Inferflow Examples

Runnable examples for the Inferflow OpenAI-compatible API, including DeepSeek, Doubao, MiMo, and Qwen model aliases where enabled for Cursor, Dify, Open WebUI, Python, JavaScript, LangChain, and cURL.

Inferflow uses the same client pattern as OpenAI:

```text
base_url = https://api.inferflow.dev/v1
authorization = Bearer <your Inferflow API key>
```

## What This Repository Covers

- OpenAI-compatible chat completions.
- China frontier model aliases such as DeepSeek V4, Doubao Seed, MiMo, and Qwen where enabled.
- Setup examples for Cursor, Dify, Open WebUI, Python, JavaScript, LangChain, and cURL.
- Common fixes for `401 Unauthorized`, `model_not_found`, `insufficient_balance`, and wrong base URL errors.

## Connection Values

```text
Base URL: https://api.inferflow.dev/v1
API key: use your Inferflow dashboard key
Recommended model: deepseek-v4-flash
Doubao quick test: doubao-seed-2.0-mini
```

## 3-minute Quickstart

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

6. If the response says credit or balance is insufficient, open Billing in the Inferflow console, complete a Paddle top-up, and retry the same command.

## Debug a Tool Setup

If Cursor, Dify, Open WebUI, LangChain, or another client fails, test Inferflow outside that tool first:

```bash
curl https://api.inferflow.dev/v1/chat/completions \
  -H "Authorization: Bearer $INFERFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply exactly: Inferflow OK"}]}'
```

If cURL works, the API key, balance, model name, and Inferflow route are valid. The remaining issue is usually the tool's custom provider settings, unsupported parameters, or a client-specific route such as `/responses` instead of `/chat/completions`.

If cURL fails, fix the API key, base URL, model name, or balance before debugging the tool.

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
- Cursor with DeepSeek and Doubao: `integrations/cursor-deepseek-doubao.md`
- Dify: `integrations/dify.md`
- Open WebUI: `integrations/openwebui.md`
- Python SDK: `python/openai_sdk.py`
- JavaScript SDK: `javascript/openai_sdk.mjs`
- LangChain: `langchain/chat_openai.py`
- Model names: `docs/model-names.md`
- Troubleshooting: `docs/troubleshooting.md`

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

Doubao coding test, if enabled in your account:

```text
doubao-seed-2.0-code
```

Use only model names visible in your Inferflow account.

More aliases and selection notes: `docs/model-names.md`.

## Troubleshooting

- `401 Unauthorized`: check `INFERFLOW_API_KEY` and the `Authorization: Bearer ...` header.
- `model_not_found`: use a model alias visible in your Inferflow Models page.
- `insufficient_balance`: open Billing, top up with Paddle, and retry after the balance updates.
- Wrong base URL: use exactly `https://api.inferflow.dev/v1`.
- Credential test works but runtime returns 404: check whether the tool is calling `/responses` or appending a route to an already complete URL.
- Cursor/Dify/Open WebUI setup is unclear: run the cURL test above first, then copy the same base URL and model name into the tool.

Full troubleshooting guide: `docs/troubleshooting.md`.

OpenAI-compatible setup checklist:
https://inferflow.hashnode.dev/openai-compatible-api-setup-checklist-base-url-model-names-401-404-and-chat-completions

## Ask for Setup Help

When opening a GitHub issue or asking in a community thread, include:

```text
Tool: Cursor / Dify / Open WebUI / LangChain / other
Base URL used: https://api.inferflow.dev/v1
Model used: deepseek-v4-flash
Did the cURL test work? yes/no
Exact error message:
```

## Links

- Docs: https://inferflow.dev/docs/
- Examples page: https://inferflow.dev/examples/
- Model catalog: https://inferflow.dev/models/
- API Reference: https://inferflow.dev/docs/api-reference/
- OpenAI-compatible setup checklist: https://inferflow.hashnode.dev/openai-compatible-api-setup-checklist-base-url-model-names-401-404-and-chat-completions
- GitHub repository: https://github.com/luresun1988-bot/inferflow-examples

## Safety

Never commit real API keys. Use environment variables or your local secret manager.
