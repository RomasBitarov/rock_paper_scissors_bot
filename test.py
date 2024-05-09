from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, \
    ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo



BOT_TOKEN = '7129172882:AAGKbOhFPaKUl3lpaALEv9I7Q3bLeuIH-Cw'
# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# # Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()


# Создаем кнопки
contact_btn = KeyboardButton(
    text='Отправить телефон',
    request_contact=True
)
geo_btn = KeyboardButton(
    text='Отправить геолокацию',
    request_location=True
)
pool_btn = KeyboardButton(
    text='Создать опрос',
    request_poll=KeyboardButtonPollType(type='regular')
)
pool_btn2 = KeyboardButton(
    text='Создать викторину',
    request_poll=KeyboardButtonPollType(type='quiz')
)

# Создаем кнопку
web_app_btn = KeyboardButton(
    text='Start Web App',
    web_app=WebAppInfo(url="https://stepik.org/")
)
# Создаем объект клавиатуры
web_app_keyboard = ReplyKeyboardMarkup(
    keyboard=[[web_app_btn]],
    resize_keyboard=True
)


# Добавляем кнопки в билдер
kb_builder.add(contact_btn, geo_btn, pool_btn, pool_btn2)
kb_builder.adjust(1, 1, 2)


# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=keyboard
    )

# Этот хэндлер будет срабатывать на команду "/web_app"
@dp.message(Command(commands='web_app'))
async def process_web_app_command(message: Message):
    await message.answer(
        text='Экспериментируем со специальными кнопками',
        reply_markup=web_app_keyboard
    )

# # Инициализируем билдер
# kb_builder = ReplyKeyboardBuilder()
# # Создаем список с кнопками
# buttons: list[KeyboardButton] = [
#     KeyboardButton(text=f'button {i + 1}') for i in range(10)
# ]
# # Распаковываем список с кнопками в билдер, указываем, что
# # в одном ряду должно быть 4 кнопки
# kb_builder.row(*buttons, width=4)
#
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(
#         text='Вот такая получается клавиатура',
#         reply_markup=kb_builder.as_markup(resize_keyboard=True)
#     )
#
# # Создаем объекты кнопок
# button_1 = KeyboardButton(text='Собак 🦮')
# button_2 = KeyboardButton(text='Огурцов 🥒')
# button_3 = KeyboardButton(text='Пылесосов 🥒')
# button_4 = KeyboardButton(text='Марта 🥒')
# button_5 = KeyboardButton(text='Тортил 🥒')
#
# # Создаем объект клавиатуры, добавляя в него кнопки
# keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2],
#                                          [button_3, button_4, button_5]],
#                                resize_keyboard=True)
#
#
# # Этот хэндлер будет срабатывать на команду "/start"
# # и отправлять в чат клавиатуру
# @dp.message(CommandStart())
# async def process_start_command(message: Message):
#     await message.answer(
#         text='Чего кошки боятся больше?',
#         reply_markup=keyboard,
#         one_time_keyboard=True
#     )
#
#
# # Этот хэндлер будет срабатывать на ответ "Собак 🦮"
# @dp.message(F.text == 'Собак 🦮')
# async def process_dog_answer(message: Message):
#     await message.answer(
#         text='Да, несомненно, кошки боятся собак. '
#              'Но вы видели как они боятся огурцов?'
#         #reply_markup=ReplyKeyboardRemove()
#     )
#
#
# # Этот хэндлер будет срабатывать на ответ "Огурцов 🥒"
# @dp.message(F.text == 'Огурцов 🥒')
# async def process_cucumber_answer(message: Message):
#     await message.answer(
#         text='Да, иногда кажется, что огурцов '
#              'кошки боятся больше',
#         #reply_markup=ReplyKeyboardRemove()
#     )


if __name__ == '__main__':
    dp.run_polling(bot)