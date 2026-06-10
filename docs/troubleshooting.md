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

## Credential Test Works, Runtime Returns 404

Some tools test credentials with one endpoint but run chat requests through another endpoint.

Check whether the failing runtime call uses:

```text
/v1/chat/completions
```

and not:

```text
/v1/responses
/api/chat/completions
/v1/v1/chat/completions
/v1/chat/completions/chat/completions
```

For Inferflow, configure only the base URL:

```text
https://api.inferflow.dev/v1
```

Let the OpenAI-compatible client append `/chat/completions`.

## Cursor Sends Unsupported Tool or Composer Requests

Cursor and similar AI coding tools may use tool-calling, edit actions, or internal model routes that are stricter than a plain chat completion.

First verify plain chat:

```bash
curl https://api.inferflow.dev/v1/chat/completions \
  -H "Authorization: Bearer $INFERFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply exactly: OK"}]}'
```

If this works but Cursor fails, the issue is probably in Cursor's custom-provider behavior, plan restrictions, or unsupported tool-call parameters. Keep the first test simple before trying Composer, agent modes, or code-edit tools.

## Reasoning Content or Thinking Mode Errors

Some reasoning models expose provider-specific fields such as:

```text
reasoning_content
reasoning
thinking
```

If a tool drops or renames these fields, reasoning models may fail even though basic chat works. Test in this order:

1. Non-streaming basic chat.
2. Non-streaming reasoning model.
3. Streaming reasoning model.
4. Tool calling or agent mode.

Inferflow's public examples focus on text/chat OpenAI-compatible usage. Do not assume image, audio, video, or every provider-specific reasoning extension is available in every client.

## What to Include When Asking for Help

Include these details so someone can reproduce the setup:

```text
Tool: Cursor / Dify / Open WebUI / LangChain / other
Base URL: https://api.inferflow.dev/v1
Model: deepseek-v4-flash
Did the cURL test work? yes/no
Exact error:
```
