import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.INFERFLOW_API_KEY,
  baseURL: process.env.INFERFLOW_BASE_URL ?? "https://api.inferflow.dev/v1",
});

const model = process.env.INFERFLOW_MODEL ?? "deepseek-v4-flash";

const response = await client.chat.completions.create({
  model,
  messages: [
    { role: "user", content: "Reply in one sentence: Inferflow setup works." },
  ],
});

console.log(response.choices[0].message.content);
