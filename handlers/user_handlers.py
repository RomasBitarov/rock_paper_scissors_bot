from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import yes_no_kb, game_kb
from services.services import get_bot_choice, get_winner


game_list = ["💎Камень", "✂Ножницы", "🧻Бумага"]
router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=f"Привет, {message.from_user.first_name}! {LEXICON_RU['/start']}",
                         reply_markup=yes_no_kb)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_any_update(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)

@router.message(F.text == LEXICON_RU['no_button'])
async def process_any_update(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(F.text.in_([LEXICON_RU['rock'],
                            LEXICON_RU['paper'],
                            LEXICON_RU['scissors']]))
async def process_game_button(message: Message):

    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)

    # bot_choice = random.choice(game_list)
    # bot_choice = function(game_list)
    # if message.text == bot_choice:
    #     await message.answer(text="Ничья!", reply_markup=ReplyKeyboardRemove())
    # elif message.text == '💎Камень' and bot_choice == '✂Ножницы' or \
    #         message.text == '✂Ножницы' and bot_choice == '🧻Бумага' or\
    #         message.text == '🧻Бумага' and bot_choice == '💎Камень':
    #     await message.answer(text='Ты победил!', reply_markup=ReplyKeyboardRemove())
    # else:
    #     await message.answer(text='Ты проиграл!, Сыграем еще раз?', reply_markup=yes_no_kb)




