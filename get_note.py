from loader import bot
import asyncio
from utils.db_api import db
import datetime
from utils.db_api.db import get_all_data

async def check_user_notes():
    data = get_all_data()
    while True:    
        cur_time = datetime.datetime.now().strftime("%H:%M")
        for row in data:
            if row.time == cur_time:
                db.del_text(row.uid,row.id,is_note=False)
                await bot.send_message(row.uid,row.text)
        await asyncio.sleep(60)


# async def check():
#     while True:
#         cur.execute("SELECT * FROM reminders;")
#         reminders_results = cur.fetchall()
#         #
#         time = datetime.utcnow().strftime("%H:%M")
#         for x in reminders_results:
#             if x[4] == time:#     "time"
#                 if x[6] == 'onetime':#     "days"
#                     cur.execute("DELETE FROM reminders WHERE id=%s;" % str(x[0]))
#                     conn.commit()
#                     await bot.send_message(chat_id=x[1], text=x[5])#     "user_chat_id"#     "text"
#                 #
#                 else:
#                     days = [bool(int(y)) for y in x[6].split('|')]#     "days
#                     if days[datetime.utcnow().weekday()]:
#                         await bot.send_message(chat_id=x[1], text=x[5])#     "user_chat_id"#     "text"
#         #
#         await asyncio.sleep(60)


