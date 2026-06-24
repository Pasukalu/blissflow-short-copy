# BlissFlow Copy Generator

> AI-powered product copy generator for e-commerce — short copy, long copy, and video scripts in one click. Supports multiple LLM providers.

![BlissFlow](https://img.shields.io/badge/BlissFlow-Copy%20Generator-66%25%200.14%2035)
![License](https://img.shields.io/badge/License-MIT-blue)
![Pure Frontend](https://img.shields.io/badge/Pure%20Frontend-✓-success)
![Multi Provider](https://img.shields.io/badge/Multi%20Provider-✓-success)

## ✨ Features

- **One-click generation** — Generate short copy, long copy, and video scripts simultaneously
- **Multi-provider support** — DashScope (Qwen) / DeepSeek / OpenAI / OpenRouter / Custom OpenAI-compatible API
- **Three languages UI** — 繁中 / English / 日本語 interface switcher
- **Multi-language output** — Copy generated in Cantonese, Japanese, and English
- **History** — All generated copies saved locally with provider & model info
- **Download** — Export each copy as TXT file
- **Dark mode** — Warm humanist design with dark/light theme toggle
- **Pure frontend** — No backend required, API key stored in browser localStorage
- **Privacy-first** — Your API key never leaves your browser

## 🚀 Quick Start

1. **Open the app**

   Just open `frontend/index.html` in any modern browser. No build step, no server needed.

2. **Choose your provider & set API Key**

   Click "API Settings" → Select a provider → Paste your API Key → Pick a model → Save.

3. **Generate**

   Enter product name + URL → Click "Generate All Three" → Wait 30-90 seconds → Done!

## 🔌 Supported Providers

| Provider | Models | API Key URL |
|----------|--------|------------|
| **DashScope (Qwen)** | qwen3.7-plus, qwen-plus, qwen-max, qwen-turbo, qwen3-235b-a22b | [Get Key](https://dashscope.console.aliyun.com/apiKey) |
| **DeepSeek** | deepseek-chat, deepseek-reasoner | [Get Key](https://platform.deepseek.com/api_keys) |
| **OpenAI** | gpt-4o, gpt-4o-mini, gpt-4-turbo, o1-mini | [Get Key](https://platform.openai.com/api-keys) |
| **OpenRouter** | gemini-2.0-flash, claude-3.5-sonnet, llama-3.3-70b, qwen-2.5-72b | [Get Key](https://openrouter.ai/keys) |
| **Custom** | Any model name | Any OpenAI-compatible endpoint |

Each provider stores its own API Key and model selection independently. Switch providers anytime without losing settings.

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Single HTML file, vanilla JS, CSS custom properties |
| API | OpenAI-compatible `/v1/chat/completions` (works with any provider) |
| Design | Warm Humanist system — Fraunces + DM Sans, OKLCH colors |
| Storage | Browser localStorage (per-provider keys, language, theme, history) |

## 📁 Project Structure

```
blissflow-short-copy/
├── frontend/
│   └── index.html                   # The entire app (single file)
├── backend/                           # Legacy backend (not required)
│   ├── main.py
│   └── requirements.txt
├── .env.example
└── .gitignore
```

## 🎨 Design System

- **School**: Warm Humanist (Stripe Press / early Mailchimp vibe)
- **Fonts**: Fraunces (display, italic) + DM Sans (body)
- **Colors**: OKLCH color space, warm terracotta brand (`oklch(66% 0.14 35)`)
- **Motion**: `ease-out-quart` curves, 120-500ms durations
- **Radius**: Hierarchical — 4px inputs → 6px buttons → 10px cards

## 🔧 Configuration

### API Key
Each provider has its own key storage (`bf_key_<provider>` in localStorage). Keys are never sent anywhere except directly to the provider's API endpoint.

### Model
Each provider has a recommended model list in the Settings dropdown. For the "Custom" provider, you can type any model name manually.

### Prompts
The system prompts for short/long/video copy are defined in the `PROMPTS` object inside the HTML file. Customize them to fit your brand voice.

## 🌐 Language Switching

The UI supports three languages:
- **繁中** (Traditional Chinese) — Default
- **English**
- **日本語** (Japanese)

Language preference is saved in `localStorage`. The generated copy is always multi-language (Cantonese + Japanese + English) regardless of UI language.

## 📝 License

MIT License — see [LICENSE](LICENSE) file.

## 🤝 Contributing

This is part of the larger BlissFlow open-source e-commerce automation project. Contributions welcome!

## 🔗 Related

- [BlissFlow](https://github.com/Pasukalu/blissflow) — Full SaaS platform (Next.js + FastAPI + n8n)
- [DashScope API Docs](https://help.aliyun.com/zh/dashscope/)
- [DeepSeek API Docs](https://platform.deepseek.com/api-docs)
- [OpenRouter Docs](https://openrouter.ai/docs)
