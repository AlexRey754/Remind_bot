from loader import dp

from aiogram import types
from aiogram.dispatcher import FSMContext

from states import Request_reg
import keyboards
from utils.db_api import db



@dp.message_handler(state=Request_reg.header)
async def set_header(message: types.Message, state: FSMContext):
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        text = message.text
        await state.update_data(header=text)
        await message.answer('Введите текст заметки',reply_markup=keyboards.default.cancel)
        await Request_reg.text.set()


@dp.message_handler(state=Request_reg.text)
async def set_text(message: types.Message, state: FSMContext):
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        text = message.text
        await state.update_data(text=text)
        await message.answer('Установить напоминание или сохранить как заметку?',reply_markup=keyboards.default.time_or_remind)
        await Request_reg.time_or_remind.set()

@dp.message_handler(state=Request_reg.time_or_remind)
async def set_text(message: types.Message, state: FSMContext):
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)

    elif message.text == '⏰Назначить напоминание':
        await message.answer('Укажите время в формате <b>##:##</b>',reply_markup=keyboards.default.cancel)
        await Request_reg.time.set()

    elif message.text == '🗒Сохранить как заметку':
        await state.update_data(time='Заметка')
        await Request_reg.confirm.set()
        await message.answer('Сохранить?',reply_markup=keyboards.default.save)


@dp.message_handler(state=Request_reg.time)
async def set_text(message: types.Message, state: FSMContext):
    if message.text == '❌Отмена':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)
    else:
        user_time = message.text
        # Защита от дурака
        try:
            if ':' in user_time:
                # Проверка на соответствие стандарта указания времени
                time = user_time.split(':')
                if 0<=int(time[0])<=23 and 0<=int(time[1])<=59:
                    await state.update_data(time=user_time)
                    await message.answer('Желаете сохранить?',reply_markup=keyboards.default.save)
                    await Request_reg.confirm.set()
                else: raise
            else: raise
        except:
            await message.answer('Пожалуйста введите время в формате <b>##:##</b>',reply_markup=keyboards.default.cancel)


@dp.message_handler(state=Request_reg.confirm)
async def save_note(message: types.Message, state: FSMContext):
    if message.text == '✅Да':
        data = await state.get_data()
        header = data.get('header')
        text = data.get('text')
        time = data.get('time')
        uid = message.from_user.id
        if time == 'Заметка':
            db.add_text(uid,header,text)
        else:
            db.add_text(uid,header,text,time,is_note=False)
        await state.finish()
        await message.answer('Сохранил',reply_markup=keyboards.default.menu)

    elif message.text == '❌Нет':
        await state.finish()
        await message.answer('Отмена',reply_markup=keyboards.default.menu)

        
