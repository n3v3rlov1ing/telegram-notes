from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = [[
        KeyboardButton(text='Отмена')
    ]]
cancel = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)