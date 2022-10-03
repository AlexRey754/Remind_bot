from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(True,True)
menu.row(KeyboardButton('➕Добавить заметку'))
menu.row(KeyboardButton('🤚Просмотреть заметки'))
menu.row(KeyboardButton('🤚Просмотреть напоминания'))



cancel = ReplyKeyboardMarkup(True, True)
cancel.row(KeyboardButton('❌Отмена'))

save = ReplyKeyboardMarkup(True, True)
save.row(KeyboardButton('✅Да'))
save.row(KeyboardButton('❌Нет'))

time_or_remind = ReplyKeyboardMarkup(True,True)
time_or_remind.row(KeyboardButton('⏰Назначить напоминание'))
time_or_remind.row(KeyboardButton('🗒Сохранить как заметку'))
time_or_remind.row(KeyboardButton('❌Отмена'))

