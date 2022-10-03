from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Request_reg
import keyboards
from utils.db_api import db

@dp.message_handler(content_types=['text'])
async def text_buttons_func(message: types.Message, state: FSMContext):
    # uid = message.from_user.id
    match message.text:
        case '➕Добавить заметку':
            await message.answer('Введите заголовок заметки', reply_markup=keyboards.default.cancel)
            await Request_reg.header.set()

        case '🤚Просмотреть заметки':
            uid = message.from_user.id
            text = db.get_text(uid,is_note=True)
            await message.answer(text,reply_markup=keyboards.default.menu)

        case '🤚Просмотреть напоминания':
            uid = message.from_user.id
            text = db.get_text(uid,is_note=False)
            await message.answer(text,reply_markup=keyboards.default.menu)

        case message.text.startswith('/delN'):
            row_id = int(message.text[5:])
            uid = message.from_user.id
            try:
                db.del_text(uid,row_id,is_note=True)
                await message.answer("Удалил заметку")
            except:
                await message.answer("Вы можете удалять только свои заметки")
        
        case message.text.startswith('/delR'):
            row_id = int(message.text[5:])
            uid = message.from_user.id
            try:
                db.del_text(uid,row_id,is_note=False)
                await message.answer("Удалил напоминание")
            except:
                await message.answer("Вы можете удалять только свои напоминания")


