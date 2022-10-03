from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Request_reg
import keyboards
from utils.db_api import db

@dp.message_handler(content_types=['text'])
async def text_buttons_func(message: types.Message, state: FSMContext):
    # uid = message.from_user.id
    if message.text == '➕Добавить заметку':
        await message.answer('Введите заголовок заметки', reply_markup=keyboards.default.cancel)
        await Request_reg.header.set()

    elif message.text == '🤚Просмотреть заметки':
        uid = message.from_user.id
        text = db.get_notes(uid)
        await message.answer(text,reply_markup=keyboards.default.menu)

    elif message.text == '🗒Список':
        text = db.get_data()
        await message.answer(text)

    elif message.text.startswith('/del'):
        row_id = int(message.text[4:])
        uid = message.from_user.id
        try:
            db.del_note(uid,row_id)
            await message.answer("Удалил")
        except:
            await message.answer("Вы можете удалять только свои заметки")


