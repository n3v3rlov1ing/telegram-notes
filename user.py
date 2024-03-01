from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

import keyboards as kb
from states import Notes, Limit
from db import Database

router = Router()
db = Database()

@router.message(F.text == 'Отмена')
async def cmd_note(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Действие отменено', reply_markup=ReplyKeyboardRemove())


@router.message(Command('note'))
async def cmd_note(message: Message, state: FSMContext):
    await state.set_state(Notes.text)
    await message.answer('Напиши текст для заметки', reply_markup=kb.cancel)
    
@router.message(Notes.text)
async def get_note_text(message: Message, state: FSMContext):
    await db.add_note(message.from_user.id, message.text)
    await message.answer('Заметка добавлена!', reply_markup=ReplyKeyboardRemove())
    await state.clear()
    
@router.message(Command('notes'))
async def cmd_get_notes(message: Message, state: FSMContext):
    await state.set_state(Limit.limit)
    await message.answer('Сколько последних заметок вывести? (По умолчанию = 5)', reply_markup=kb.cancel)
    
@router.message(Limit.limit)
async def get_note_text(message: Message, state: FSMContext):
    if message.text.isdigit():
        res = await db.get_notes(user_id = message.from_user.id, limit = message.text)
        await message.answer(f'{res}')
        await state.clear()
    else:
        await message.answer('Это не число')
        
    
    