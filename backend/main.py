from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="BlissFlow Short Copy Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

# 短文案預設 prompt
SHORT_COPY_SYSTEM_PROMPT = """你是一個電商專家. 這是你經營的國際電商獨立站 www.blissshop.life , 我會比不同的產品名稱及連結比你, 你分別用地道的廣東話, 日文, 及英文, 用20種不同表達方式(就是給我創作20個文案), 每個表達只有2-6句就可以, 每句需要加上emojis及這句"本店所有產品支援全球送貨". 目的是要針對人的痛點或挑起人的情感及購買慾, 立即去下單購買."""


class GenerateRequest(BaseModel):
    product_url: str
    product_name: str


class CopyItem(BaseModel):
    language: str
    index: int
    content: str


@app.get("/api/health")
async def health():
    return {"status": "ok"}


@app.post("/api/generate")
async def generate_short_copy(req: GenerateRequest):
    user_message = f"{req.product_url} 超抵價，百幾蚊就可係BLISS SHOP入手 — {req.product_name}"

    headers = {
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": SHORT_COPY_SYSTEM_PROMPT},
            {"role": "user", "content": user_message},
        ],
    }

    async with httpx.AsyncClient(timeout=120) as client:
        resp = await client.post(DASHSCOPE_URL, headers=headers, json=payload)
        if resp.status_code != 200:
            raise HTTPException(status_code=500, detail=f"DashScope error: {resp.text}")

        data = resp.json()
        content = data["choices"][0]["message"]["content"]

    return {
        "product_name": req.product_name,
        "product_url": req.product_url,
        "content": content,
        "usage": data.get("usage", {}),
    }
