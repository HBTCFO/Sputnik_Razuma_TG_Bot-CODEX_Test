from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from ..callbacks import Tech
from ...content import texts
from ..keyboards import technique_controls

router = Router()

@router.callback_query(F.data == Tech.T478)
async def t478(c: CallbackQuery):
    await c.message.answer(texts.TECH_478_SHORT, reply_markup=technique_controls())
    await c.answer()

@router.callback_query(F.data == Tech.PMR)
async def pmr(c: CallbackQuery):
    await c.message.answer(texts.TECH_PMR_SHORT, reply_markup=technique_controls())
    await c.answer()

@router.callback_query(F.data == Tech.GROUND)
async def ground(c: CallbackQuery):
    await c.message.answer(texts.TECH_GROUND_SHORT, reply_markup=technique_controls())
    await c.answer()

@router.callback_query(F.data == Tech.JOURNAL)
async def journal(c: CallbackQuery):
    await c.message.answer(texts.JOURNAL_PROMPT)
    await c.answer()

@router.callback_query(F.data == Tech.CLOSE)
async def close_day(c: CallbackQuery):
    await c.message.answer(texts.CLOSE_DAY_PROMPT)
    await c.answer()

@router.callback_query(F.data == Tech.WIPE)
async def wipe_ctx(c: CallbackQuery):
    # обработка в общем хендлере fallback (создаст новый thread)
    await c.message.answer("Начинаю «чистую сессию». Напиши, с чего начнём.")
    await c.answer()
