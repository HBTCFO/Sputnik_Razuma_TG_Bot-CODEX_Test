import os
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import PlainTextResponse
from starlette.background import BackgroundTask

from .utils.logging import setup_logging  # noqa: F401
from .config import settings
from .telegram.bot import build_dp
from aiogram import types

app = FastAPI(title="Sputnik Razuma Backend")

# /healthz
@app.get("/healthz", response_class=PlainTextResponse)
async def healthz():
    return "ok"

# /privacy
@app.get("/privacy", response_class=PlainTextResponse)
async def privacy():
    path = os.path.join(os.path.dirname(__file__), "content", "privacy_ru.md")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# webhook endpoint (for prod)
dp = build_dp(settings.TELEGRAM_BOT_TOKEN)
bot = dp["bot"]

@app.post("/webhook/{token}")
async def telegram_webhook(token: str, request: Request):
    if token != os.getenv("WEBHOOK_SECRET", settings.WEBHOOK_SECRET or ""):
        raise HTTPException(status_code=403, detail="forbidden")

    data = await request.json()
    update = types.Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"ok": True}
