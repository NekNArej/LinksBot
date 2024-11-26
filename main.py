# https://t.me/test2jiwoc
# https://t.me/+xl7FMyr1FHNjMjcy
from aiogram import Bot, Dispatcher
from telethon import TelegramClient
import logging
from settings import settings
from handlers_bot.basic import get_links, start_bot
import asyncio
token = settings.bots.bot_token
admin_id = settings.bots.admin_id
api_id = settings.client.api_id
api_hash = settings.client.api_hash
admin_id = settings.bots.admin_id
client = TelegramClient('ms', api_id, api_hash,
                        device_model='iPhone 55 Pro',
                        system_version='IOS 100.0')

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token)    
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.message.register(get_links)


    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print('Bot stopped')

    finally:
        await bot.session.close()
try:
    if __name__=='__main__':
        asyncio.run(main())
except KeyboardInterrupt:
        print('Bot stopped')


