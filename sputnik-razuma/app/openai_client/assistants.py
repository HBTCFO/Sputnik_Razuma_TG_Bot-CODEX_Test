from __future__ import annotations

import asyncio
import os
from typing import Dict, Optional

from openai import OpenAI
from pydantic import BaseModel

class AssistantClient:
    """
    Простая оболочка над OpenAI Assistants API.
    Не хранит локально текст сообщений. Для соответствия политике — только in-memory map chat_id -> thread_id.
    """

    def __init__(self, api_key: str | None = None, assistant_id: str | None = None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.assistant_id = assistant_id or os.getenv("OPENAI_ASSISTANT_ID")
        if not self.assistant_id:
            raise RuntimeError("OPENAI_ASSISTANT_ID is not set")
        self._threads: Dict[int, str] = {}

    def ensure_thread(self, chat_id: int) -> str:
        tid = self._threads.get(chat_id)
        if tid:
            return tid
        thread = self.client.beta.threads.create()
        self._threads[chat_id] = thread.id
        return thread.id

    def reset_thread(self, chat_id: int) -> str:
        thread = self.client.beta.threads.create()
        self._threads[chat_id] = thread.id
        return thread.id

    def send_message(self, thread_id: str, text: str) -> str:
        # Добавляем сообщение и запускаем run
        self.client.beta.threads.messages.create(thread_id=thread_id, role="user", content=text)
        run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=self.assistant_id,
        )
        return run.id

    async def wait_run(self, thread_id: str, run_id: str, timeout_s: int = 60) -> Optional[str]:
        # Ожидание завершения
        client = self.client
        for _ in range(timeout_s * 2):  # опрос каждые 0.5с
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
            if run.status in ("completed", "failed", "cancelled", "expired"):
                break
            await asyncio.sleep(0.5)

        # Получаем последнее ассистентское сообщение
        messages = client.beta.threads.messages.list(thread_id=thread_id, order="desc", limit=5)
        for m in messages.data:
            if m.role == "assistant":
                # Склеиваем текстовые части
                parts = []
                for c in m.content:
                    if c.type == "text":
                        parts.append(c.text.value)
                return "\n".join(parts).strip() or None
        return None
