from aiogram import Router
from aiogram.types import Message
from ...content.texts import CRISIS_MSG
from ..keyboards import crisis_menu

router = Router()

@router.message()
async def crisis_entry(message: Message, crisis_triggered: bool | None = None):
    if crisis_triggered:
        await message.answer(CRISIS_MSG, reply_markup=crisis_menu())
