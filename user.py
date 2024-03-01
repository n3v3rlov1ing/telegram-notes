from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from aiogram.exceptions import TelegramBadRequest

from states import Notes
from db import Database

router = Router()
db = Database()

@router.message(Command('note'))
async def cmd_note(message: Message, state: FSMContext):
    await state.set_state(Notes.text)
    await message.answer('Напиши текст для заметки')
    
@router.message(Notes.text)
async def get_note_text(message: Message, state: FSMContext):
    await db.add_note(message.from_user.id, message.text)
    await message.answer('Заметка добавлена!')
    await state.clear()
    
@router.message(Command('notes'))
async def cmd_note(message: Message):
    try:
        limit = message.text.split()
        await message.answer(text=await db.get_notes(user_id=message.from_user.id, limit=limit[1]))
    except IndexError:
        await message.answer(text=await db.get_notes(user_id=message.from_user.id))
    except TelegramBadRequest:
        await message.answer('Ошибка при получении заметок')
    
    