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

#MongoDB connection
# client = pymongo.MongoClient(os.getenv('CLIENT'))

@dp.message_handler(commands=["start"])
async def start_func(message):
    await bot.send_message(message.chat.id, "Привет, друже {}".format(message.from_user.first_name))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
