from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="BlissFlow Copy Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
DASHSCOPE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"

# ==================== 預設 Prompt ====================

SHORT_COPY_PROMPT = """你是一個電商專家. 這是你經營的國際電商獨立站 www.blissshop.life , 我會比不同的產品名稱及連結比你, 你分別用地道的廣東話, 日文, 及英文, 用20種不同表達方式(就是給我創作20個文案), 每個表達只有2-6句就可以, 每句需要加上emojis及這句"本店所有產品支援全球送貨". 目的是要針對人的痛點或挑起人的情感及購買慾, 立即去下單購買."""

LONG_COPY_PROMPT = """你是一個電商專家, 你是幫我的網店(www.blissshop.life)內的產品 , 去創作文案, 在不同的社交平台上發表. 我會把產品的連結給你, 你幫我參考以下文案, 來創作出6遍(不同內容風格)跟我給你的產品的介紹內容給我. 要比埋emojis比我。 另外每個文案的結尾幫我加上一句： 本店所有產品支援全球送貨。

參考文案:
日本Scour Towels 廚房環保不織布抹布
💯一套6卷💯
激抵呀～～～～
日本原價 $38/卷
依家 $6.5 /卷，好好用架～
最抵最抵最抵
,超超超抵呀🈹🈹🈹🈹🈹
勁好用推薦‼️傳統抹布潛藏大量細菌，比馬桶還髒，有害健康，不織布免洗式多用抹布，乾濕兩用，點斷式設計。
一次性使用，即撕即用，用完即扔，特別方便。
廚房清潔、外出野餐都可以使用哦。
採用竹纖維無紡布，不含熒光劑，抗菌無毒，不黏油，去污效果好，有一擦即淨的功效。
✎商品特色✎
🉐環保無紡布抹布
🉐採用衛生清潔的不織布
🉐具有衛生、清潔、吸水性強、無毒素、柔軟耐洗、不易生菌，
🉐有一擦即淨的功效唷！
✎商品規格✎一套6 卷
◎商品材質：無紡布
◎商品尺寸：50張 (每片20x30cm)"""

VIDEO_COPY_PROMPT = """你是一個youtube short 平台的產品推廣專家, 需要給你我的產品資料, 你用非常吸引的方式去用英文寫文案出來, 去吸引消息者注意及購買. 同時要提供
1. 吸引人的headling
2. 相関的hashtags
3. 相関的CHANNEL TAGS, 用@開頭
4. 相関的tags, 要用","去分開
5. 我們的網上聯系方式: http://bit.ly/1FBLIVECHAT
6. 我們的web: blisstravel.life
明白我的要求嗎?"""

# 類型映射
COPY_TYPES = {
    "short": {"name": "短文案", "prompt": SHORT_COPY_PROMPT},
    "long": {"name": "長文案", "prompt": LONG_COPY_PROMPT},
    "video": {"name": "視頻文案", "prompt": VIDEO_COPY_PROMPT},
}


# ==================== Models ====================

class GenerateRequest(BaseModel):
    product_url: str
    product_name: str
    copy_type: str = "short"  # short / long / video


class ContinueRequest(BaseModel):
    product_name: str
    previous_content: str
    copy_type: str = "short"


# ==================== API ====================

@app.get("/api/health")
async def health():
    return {"status": "ok", "types": list(COPY_TYPES.keys())}


async def call_dashscope(system_prompt: str, user_message: str) -> dict:
    headers = {
        "Authorization": f"Bearer {DASHSCOPE_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "qwen-plus",
        "messages": [
            {"role": "system", "content": system_prompt},
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
        "content": content,
        "usage": data.get("usage", {}),
    }


@app.post("/api/generate")
async def generate_copy(req: GenerateRequest):
    copy_type = req.copy_type
    if copy_type not in COPY_TYPES:
        raise HTTPException(status_code=400, detail=f"Unknown copy_type: {copy_type}")

    config = COPY_TYPES[copy_type]
    user_message = f"{req.product_url} 超抵價，百幾蚊就可係BLISS SHOP入手 — {req.product_name}"

    result = await call_dashscope(config["prompt"], user_message)

    return {
        "product_name": req.product_name,
        "product_url": req.product_url,
        "copy_type": copy_type,
        "copy_type_name": config["name"],
        "content": result["content"],
        "usage": result["usage"],
    }


@app.post("/api/continue")
async def continue_copy(req: ContinueRequest):
    copy_type = req.copy_type
    if copy_type not in COPY_TYPES:
        raise HTTPException(status_code=400, detail=f"Unknown copy_type: {copy_type}")

    config = COPY_TYPES[copy_type]
    user_message = f"繼續生成剩餘的文案，從上次中斷的地方接著寫。以下是已生成的內容：\n\n{req.previous_content}"

    result = await call_dashscope(config["prompt"], user_message)

    return {
        "product_name": req.product_name,
        "copy_type": copy_type,
        "copy_type_name": config["name"],
        "content": result["content"],
        "usage": result["usage"],
    }
