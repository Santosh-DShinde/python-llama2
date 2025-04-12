# 🧠 LLaMA2 Chat API (DRF + Ollama Integration)

This project provides a simple REST API built with Django REST Framework to interact with the LLaMA2 language model using the Ollama CLI. It accepts a user prompt and returns a response generated by the LLaMA2 model running locally.

---

## 📌 Features

- Accepts text prompts via POST requests
- Uses `ollama` CLI to run `llama2` model
- Returns AI-generated responses
- Handles errors gracefully (empty input, timeouts, subprocess errors)

---

## 🚀 API Endpoint

### `POST /conversation/`

**Request Body:**
```json
{
  "prompt": "Tell me a joke!"
}
```
