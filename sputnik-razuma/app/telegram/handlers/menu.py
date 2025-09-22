from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from ..callbacks import Topic
from ..keyboards import techniques_menu
from ...content.texts import STRESS_FOLLOWUP

router = Router()

@router.callback_query(F.data == Topic.STRESS)
async def pick_stress(c: CallbackQuery):
    await c.message.answer(STRESS_FOLLOWUP, reply_markup=techniques_menu())
    await c.answer()

@router.callback_query(F.data == Topic.PRODUCTIVITY)
async def pick_prod(c: CallbackQuery):
    await c.message.answer("Окей. Что мешает фокусу сегодня? 1) отвлечения 2) прокрастинация 3) усталость 4) другое",
                           reply_markup=techniques_menu())
    await c.answer()

@router.callback_query(F.data == Topic.RELATIONSHIPS)
async def pick_rel(c: CallbackQuery):
    await c.message.answer("Про отношения. Что сейчас важнее? 1) конфликт 2) недопонимание 3) поддержка 4) другое",
                           reply_markup=techniques_menu())
    await c.answer()

@router.callback_query(F.data == Topic.OTHER)
async def pick_other(c: CallbackQuery):
    await c.message.answer("Опиши своими словами, что хочется улучшить. Я предложу короткий план.",
                           reply_markup=techniques_menu())
    await c.answer()

@router.callback_query(F.data == Topic.CRISIS)
async def pick_crisis(c: CallbackQuery):
    await c.message.answer("Если есть угроза жизни — звони 112. Хочешь, подскажу ресурсы рядом?",
                           reply_markup=techniques_menu())
    await c.answer()
