from aiogram.utils.keyboard import InlineKeyboardBuilder
from . import callbacks

def main_menu():
    b = InlineKeyboardBuilder()
    for title, data in (
        ("Стресс/тревога", callbacks.Topic.STRESS),
        ("Продуктивность/привычки", callbacks.Topic.PRODUCTIVITY),
        ("Отношения/общение", callbacks.Topic.RELATIONSHIPS),
        ("Другое (опишу сам)", callbacks.Topic.OTHER),
        ("Экстренная помощь", callbacks.Topic.CRISIS),
    ):
        b.button(text=title, callback_data=data)
    b.adjust(2, 2, 1)
    return b.as_markup()

def techniques_menu():
    b = InlineKeyboardBuilder()
    for title, data in (
        ("Дыхание 4-7-8", callbacks.Tech.T478),
        ("ПМР (релаксация)", callbacks.Tech.PMR),
        ("Заземление 5-4-3-2-1", callbacks.Tech.GROUND),
        ("Дневник настроения", callbacks.Tech.JOURNAL),
        ("Ритуал закрытия дня", callbacks.Tech.CLOSE),
        ("Сбросить контекст", callbacks.Tech.WIPE),
    ):
        b.button(text=title, callback_data=data)
    b.adjust(2, 2, 2)
    return b.as_markup()

def crisis_menu():
    b = InlineKeyboardBuilder()
    b.button(text="Найти помощь рядом", url="https://findahelpline.com/")
    return b.as_markup()

def technique_controls():
    b = InlineKeyboardBuilder()
    b.button(text="Начать", callback_data="go_start")
    b.button(text="Инструкция", callback_data="go_help")
    b.button(text="Стоп", callback_data="go_stop")
    return b.as_markup()
