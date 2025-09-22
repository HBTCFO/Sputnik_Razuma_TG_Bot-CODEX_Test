import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .middleware.crisis_guard import CrisisGuard
from .handlers import start, menu, techniques, crisis, context, fallback

def build_dp(token: str) -> Dispatcher:
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    dp = Dispatcher()
    # middleware
    dp.message.middleware(CrisisGuard())
    # routers
    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(techniques.router)
    dp.include_router(crisis.router)
    dp.include_router(context.router)
    dp.include_router(fallback.router)
    dp["bot"] = bot
    return dp

async def run_polling(token: str):
    dp = build_dp(token)
    bot = dp["bot"]
    await dp.start_polling(bot)
