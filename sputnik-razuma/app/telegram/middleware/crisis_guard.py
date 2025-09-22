from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Callable, Dict, Any, Awaitable
import re

TRIGGERS = [
    r"\bсуицид\b", r"\bпокон(чу|чить)\b", r"\bне хочу жить\b",
    r"\bубить себя\b", r"\bнавредить себе\b", r"\bсамоповреждени",
    r"\bголоса\b", r"\bгаллюцинац", r"\bбред\b", r"\bнасилие\b"
]
TRIGGER_RE = re.compile("|".join(TRIGGERS), re.IGNORECASE)

class CrisisGuard(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
                       event: Message,
                       data: Dict[str, Any]) -> Any:
        text = (event.text or "").lower()
        if TRIGGER_RE.search(text):
            data["crisis_triggered"] = True
        return await handler(event, data)
