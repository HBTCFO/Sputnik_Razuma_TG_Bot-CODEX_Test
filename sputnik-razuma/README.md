# «Спутник Разума» — Telegram-бот (Backend)

Мягкий помощник для саморазвития и стресс-менеджмента. Без локального хранения переписки. Контекст — в памяти OpenAI Assistants.  
Локальный запуск — polling, прод — webhook (Cloud Run/VPS).

## Быстрый старт (локально, macOS)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # заполните токены
export PYTHONUTF8=1
python -m app.run_polling
```

## Prod (webhook)

- Соберите Docker-образ, задеплойте (Cloud Run/VPS с TLS).
- Установите вебхук (`/set_webhook` описано в `app/telegram/bot.py`).
- FastAPI-приложение: `app.main:app`, маршрут `/healthz`, `/privacy`, `/webhook/{token}`.

## Политика

- Не сохраняем локально переписку и профили.
- Логи — только технические метаданные (без текста сообщений).
- Контекст в памяти Assistants API.
