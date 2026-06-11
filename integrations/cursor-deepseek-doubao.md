# Cursor with DeepSeek and Doubao

Use this when you want one OpenAI-compatible Cursor setup for both DeepSeek and Doubao models through Inferflow.

## Connection values

```text
Provider: OpenAI-compatible
API Key: your Inferflow API key
Base URL: https://api.inferflow.dev/v1
Default model: deepseek-v4-flash
Higher-quality model: deepseek-v4-pro
Doubao test model: doubao-seed-2.0-mini
Doubao coding model: doubao-seed-2.0-code
```

Only use model names visible in your Inferflow account.

## Verify the endpoint first

Before changing Cursor settings, run a direct request:

```bash
curl https://api.inferflow.dev/v1/chat/completions \
  -H "Authorization: Bearer $INFERFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply exactly: Inferflow OK"}]}'
```

If this works, your key, balance, base URL, and selected model are valid.

## Cursor setup sequence

1. Open Cursor settings.
2. Go to the model or provider settings area.
3. Add or enable an OpenAI-compatible provider.
4. Paste your Inferflow API key.
5. Set the base URL to `https://api.inferflow.dev/v1`.
6. Add one model alias, for example `deepseek-v4-flash`.
7. Test a short prompt before using agent/composer modes.

If Cursor says named models are not available on your plan, use Auto mode for Cursor itself and verify Inferflow through cURL, Python, JavaScript, Open WebUI, or Dify.

## Model choices

Start with `deepseek-v4-flash` because it is the simplest fast baseline.

Use `deepseek-v4-pro` when you need better reasoning quality.

Use `doubao-seed-2.0-mini` for a lightweight Doubao setup test.

Use `doubao-seed-2.0-code` for coding prompts if it is enabled in your account.

## Common errors

### 401 Unauthorized

The API key is missing, malformed, or belongs to another gateway.

### model_not_found

The model name is not enabled for your account. Copy a model name from the Inferflow Models page.

### 404 at runtime

The client may be building the wrong route.

Correct:

```text
Base URL: https://api.inferflow.dev/v1
Runtime route: https://api.inferflow.dev/v1/chat/completions
```

Wrong:

```text
Base URL: https://api.inferflow.dev/v1/chat/completions
```

That may cause the tool to append another route.

### Credential test works but chat fails

The credential test and runtime request may use different routes. Check whether Cursor is using `/chat/completions` or another endpoint.
