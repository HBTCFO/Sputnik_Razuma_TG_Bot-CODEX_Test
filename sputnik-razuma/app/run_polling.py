import asyncio
from .telegram.bot import run_polling
from .config import settings

if __name__ == "__main__":
    asyncio.run(run_polling(settings.TELEGRAM_BOT_TOKEN))
