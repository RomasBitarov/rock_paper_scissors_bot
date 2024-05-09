from aiogram import Router, F
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import keyboard, keyboard2
import random
from services.services import function


game_list = ["💎Камень", "✂Ножницы", "🧻Бумага"]
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}! {LEXICON_RU['/start']}",
                         reply_markup=keyboard)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(F.text == 'Давай!')
async def process_any_update(message: Message):
    await message.answer(text="Отлично! Делай свой выбор!", reply_markup=keyboard2)

@router.message(F.text == 'Не хочу!')
async def process_any_update(message: Message):
    await message.answer(text='Хорошо. Если, вдруг, захочешь сыграть - открой клавиатуру и нажми "Давай!"', reply_markup=ReplyKeyboardRemove())


@router.message(F.text.in_({"💎Камень", "✂Ножницы", "🧻Бумага"}))
async def process_any_update(message: Message):
    # bot_choice = random.choice(game_list)
    bot_choice = function(game_list)
    print(bot_choice)
    print(message.text)
    if message.text == bot_choice:
        await message.answer(text="Ничья!", reply_markup=ReplyKeyboardRemove())
    elif message.text == '💎Камень' and bot_choice == '✂Ножницы' or \
            message.text == '✂Ножницы' and bot_choice == '🧻Бумага' or\
            message.text == '🧻Бумага' and bot_choice == '💎Камень':
        await message.answer(text='Ты победил!', reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(text='Ты проиграл!, Сыграем еще раз?', reply_markup=keyboard)




