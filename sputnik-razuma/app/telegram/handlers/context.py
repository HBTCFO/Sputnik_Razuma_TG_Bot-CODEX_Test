from aiogram import Router, F
from aiogram.types import Message
from ...content.texts import CONTEXT_HELP

router = Router()

@router.message(F.text.lower().contains("помоги вспомнить контекст"))
async def ask_context(message: Message):
    await message.answer(CONTEXT_HELP)
