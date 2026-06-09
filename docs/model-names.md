# Inferflow Model Names

Inferflow exposes OpenAI-compatible model aliases. Use the exact model string shown in your Inferflow dashboard.

Base URL:

```text
https://api.inferflow.dev/v1
```

## Recommended Starting Points

Use `deepseek-v4-flash` for a first request because it is fast and low cost.

Use `deepseek-v4-pro` when you need stronger reasoning, coding, or longer-form answers.

Use `doubao-seed-2.0-mini` for a quick Doubao compatibility check.

Use `qwen-flash` or `qwen-plus` for Qwen-family workloads when those aliases are visible in your account.

Use `mimo-v2.5` or `mimo-v2.5-pro` for MiMo-family workloads when those aliases are visible in your account.

## Example Request

```bash
curl https://api.inferflow.dev/v1/chat/completions \
  -H "Authorization: Bearer $INFERFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [
      {"role": "user", "content": "Reply exactly: Inferflow OK"}
    ]
  }'
```

## Common Mistakes

- Do not use provider console names unless they are also visible in your Inferflow account.
- Do not add spaces, uppercase changes, or suffixes to model aliases.
- Do not use internal or experimental aliases that are not listed in the Inferflow Models page.
- If a model disappears from your account, switch to another visible alias before retrying.

## Where to Check Availability

- Dashboard Models page: https://api.inferflow.dev/catalog
- Public model guide: https://inferflow.dev/models/
- API models endpoint: `GET https://api.inferflow.dev/v1/models`

