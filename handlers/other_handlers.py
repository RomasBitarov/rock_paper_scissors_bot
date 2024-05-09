from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


router = Router()
# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@router.message()
async def send_echo(message: Message):
    try:
        await message.answer(text="Я реагирую только на нажатие кнопок")
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])