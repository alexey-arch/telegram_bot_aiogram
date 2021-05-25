from __future__ import unicode_literals
import os
import re
import logging
from unicodedata import normalize

import asyncio
from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
import pytube


loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)

if __name__ == '__main__':
    from handler import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)


