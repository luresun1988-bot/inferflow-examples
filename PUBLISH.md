# Publish `inferflow-examples`

This directory is ready to publish as a standalone public GitHub repository.

Recommended repository name:

```text
inferflow-examples
```

## One-time publish

Create an empty GitHub repository, then run from this directory:

```bash
git init
git add .
git commit -m "initial inferflow examples"
git branch -M main
git remote add origin git@github.com:YOUR_ACCOUNT/inferflow-examples.git
git push -u origin main
```

HTTPS alternative:

```bash
git remote add origin https://github.com/YOUR_ACCOUNT/inferflow-examples.git
```

## After publishing

Add the public URL to:

- `https://inferflow.dev/docs/`
- `https://inferflow.dev/llms.txt`
- Cursor, Dify, Open WebUI, Python, JavaScript, and LangChain SEO pages.

Do not include real API keys in commits.
