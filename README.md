# BlissFlow Copy Generator

> AI-powered product copy generator for e-commerce — short copy, long copy, and video scripts in one click.

![BlissFlow](https://img.shields.io/badge/BlissFlow-Copy%20Generator-66%25%200.14%2035)
![License](https://img.shields.io/badge/License-MIT-blue)
![Pure Frontend](https://img.shields.io/badge/Pure%20Frontend-✓-success)

## ✨ Features

- **One-click generation** — Generate short copy, long copy, and video scripts simultaneously
- **Three languages UI** — 繁中 / English / 日本語 interface switcher
- **Multi-language output** — Copy generated in Cantonese, Japanese, and English
- **History** — All generated copies saved locally for review
- **Download** — Export each copy as TXT file
- **Dark mode** — Warm humanist design with dark/light theme toggle
- **Pure frontend** — No backend required, API key stored in browser localStorage
- **Privacy-first** — Your API key never leaves your browser

## 🚀 Quick Start

1. **Open the app**

   Just open `frontend/商品文案生成器多語言版.html` in any modern browser. No build step, no server needed.

2. **Set your API Key**

   Click "Set API Key" and paste your [DashScope API Key](https://dashscope.console.aliyun.com/apiKey).

3. **Generate**

   Enter product name + URL → Click "Generate All Three" → Wait 30-90 seconds → Done!

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Single HTML file, vanilla JS, CSS custom properties |
| API | [DashScope](https://dashscope.aliyun.com) (Qwen models) |
| Design | Warm Humanist system — Fraunces + DM Sans, OKLCH colors |
| Storage | Browser localStorage (API key, language, theme, history) |

## 📁 Project Structure

```
blissflow-short-copy/
├── frontend/
│   └── 商品文案生成器多語言版.html   # The entire app (single file)
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
Get your DashScope API Key from [Alibaba Cloud DashScope](https://dashscope.console.aliyun.com/apiKey).

### Model
Default model is `qwen3.7-plus`. You can change it in Settings.

### Prompts
The system prompts for short/long/video copy are defined in the `PROMPTS` object inside the HTML file. Customize them to fit your brand voice.

## 🌐 Language Switching

The UI supports three languages:
- **繁中** (Traditional Chinese) — Default
- **English**
- **日本語** (Japanese)

Language preference is saved in `localStorage`. The Qwen-generated copy is always multi-language (Cantonese + Japanese + English) regardless of UI language.

## 📝 License

MIT License — see [LICENSE](LICENSE) file.

## 🤝 Contributing

This is part of the larger [BlissFlow](https://github.com/user/blissflow) open-source e-commerce automation project. Contributions welcome!

## 🔗 Related

- [BlissFlow](https://github.com/user/blissflow) — Full SaaS platform (Next.js + FastAPI + n8n)
- [DashScope API Docs](https://help.aliyun.com/zh/dashscope/)
- [Qwen AI](https://chat.qwen.ai/)
