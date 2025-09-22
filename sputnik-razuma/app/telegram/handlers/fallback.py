from aiogram import Router
from aiogram.types import Message
from ...openai_client.assistants import AssistantClient
from ...config import settings
from loguru import logger

router = Router()
client = AssistantClient()

@router.message()
async def to_assistant(message: Message):
    if message.text and message.text.strip().lower() in {"/wipe", "сбросить контекст"}:
        client.reset_thread(message.chat.id)
        await message.answer("Готово. Начинаем «чистую сессию». О чём поговорим сейчас?")
        return

    thread_id = client.ensure_thread(message.chat.id)
    try:
        run_id = client.send_message(thread_id, message.text or "")
        reply = await client.wait_run(thread_id, run_id, timeout_s=60)
        if reply:
            await message.answer(reply)
        else:
            await message.answer("Я здесь. Давай ещё раз коротко: что сейчас важнее всего?")
    except Exception as e:
        logger.exception("assistant error")
        await message.answer("Похоже, я столкнулся с ошибкой. Давай попробуем ещё раз сообщением короче.")
