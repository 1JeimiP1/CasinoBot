from aiogram import Bot, Dispatcher, types, filters
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, reply_keyboard
from aiogram.utils import executor
import os
import asyncio
import dotenv 
import pymongo
import datetime

#getting environment variables
dotenv.load_dotenv()

#logging telegram bot
bot = Bot(token = os.getenv('TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#MongoDB connections
client = pymongo.MongoClient(os.getenv('CLIENT'))
database = client['Casino']
users_mongo = database["users"]

@dp.message_handler(commands=["start"])
async def start_func(message):
    id_check = message.from_user.id
    res = users_mongo.find_one({"user_id": id_check}) #checking for presence of the user in database
    if res:
        pass #user in database
    else:
        users_mongo.insert_one({
               "user_id": message.from_user.id,
               "first_name": message.from_user.first_name,
               "username": message.from_user.username
              }) #writing user to database
    await bot.send_message(message.chat.id, "<i>Эй, игрок, приходи в казино поиграть.\nТы своим не поверишь глазам!\nЖдёт тебя впереди диффитчентов каскад!\nТы готов?) Проходите в вип-зал!</i>", parse_mode="HTML", reply_to_message_id=message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
