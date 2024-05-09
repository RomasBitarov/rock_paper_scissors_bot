from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)


btn1 = KeyboardButton(text='Давай!')
btn2 = KeyboardButton(text='Не хочу!')
btn3 = KeyboardButton(text='💎Камень')
btn4 = KeyboardButton(text='✂Ножницы')
btn5 = KeyboardButton(text='🧻Бумага')


keyboard = ReplyKeyboardMarkup(keyboard=[[btn1, btn2]], resize_keyboard=True)
keyboard2 = ReplyKeyboardMarkup(keyboard=[[btn3, btn4, btn5]], resize_keyboard=True)
