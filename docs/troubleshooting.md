# Inferflow Troubleshooting

This guide covers the most common setup problems when using Inferflow as an OpenAI-compatible API.

## 401 Unauthorized

Check that your request sends the API key as a Bearer token:

```text
Authorization: Bearer sk-your-inferflow-key
```

Also confirm that:

- The key is copied from the Inferflow dashboard.
- The key has not been deleted or disabled.
- Your client is not accidentally using an OpenAI, Anthropic, or provider-specific key.

## Wrong Base URL

Use exactly:

```text
https://api.inferflow.dev/v1
```

Do not use:

```text
https://inferflow.dev/v1
https://api.inferflow.dev
https://api.inferflow.dev/api
```

## model_not_found

Use a model alias visible in your Inferflow account.

Good first test:

```text
deepseek-v4-flash
```

Doubao quick test:

```text
doubao-seed-2.0-mini
```

See `docs/model-names.md` for model selection notes.

## insufficient_balance

Open Billing in the Inferflow dashboard, add credits with Paddle, then retry after the balance updates.

Some local payment methods may confirm asynchronously. If payment succeeds but the balance has not updated yet, wait a few minutes and refresh Billing.

## Cursor Setup Does Not Show Model Names

Some Cursor plans or versions may limit named model selection. Use the OpenAI-compatible base URL and API key first, then test with a simple prompt.

Recommended values:

```text
Base URL: https://api.inferflow.dev/v1
Model: deepseek-v4-flash
```

## Dify or Open WebUI Fails

Confirm these three values:

```text
Provider type: OpenAI-compatible
Base URL: https://api.inferflow.dev/v1
API key: your Inferflow API key
```

Then use a visible Inferflow model alias such as `deepseek-v4-flash`.

## Need a Minimal Test

Run:

```bash
bash curl/chat-completions.sh
```

Expected result: the response should include an assistant message.

