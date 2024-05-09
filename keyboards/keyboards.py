from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU


# btn1 = KeyboardButton(text='Давай!')
# btn2 = KeyboardButton(text='Не хочу!')
# btn3 = KeyboardButton(text='💎Камень')
# btn4 = KeyboardButton(text='✂Ножницы')
# btn5 = KeyboardButton(text='🧻Бумага')


# keyboard = ReplyKeyboardMarkup(keyboard=[[btn1, btn2]], resize_keyboard=True)
# keyboard2 = ReplyKeyboardMarkup(keyboard=[[btn3, btn4, btn5]], resize_keyboard=True)


# ------- Создаем клавиатуру через ReplyKeyboardBuilder -------

# Создаем кнопки с ответами согласия и отказа
button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# ------- Создаем игровую клавиатуру без использования билдера -------

# Создаем кнопки игровой клавиатуры
button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 = KeyboardButton(text=LEXICON_RU['paper'])

# Создаем игровую клавиатуру с кнопками "💎Камень",
# "✂Ножницы" и "🧻Бумага" как список списков
game_kb = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)


