#!/usr/bin/env bash
set -euo pipefail

: "${INFERFLOW_API_KEY:?Set INFERFLOW_API_KEY first}"
: "${INFERFLOW_BASE_URL:=https://api.inferflow.dev/v1}"
: "${INFERFLOW_MODEL:=deepseek-v4-flash}"

curl "$INFERFLOW_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $INFERFLOW_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"$INFERFLOW_MODEL\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"Reply in one sentence: Inferflow setup works.\"}
    ]
  }"
