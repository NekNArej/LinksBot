from telethon import TelegramClient
from settings import settings
from aiogram.types import Message
from aiogram import Bot
import time

api_id = settings.client.api_id
api_hash = settings.client.api_hash
admin_id = settings.bots.admin_id
client = TelegramClient('ms', api_id, api_hash,
                        device_model='iPhone 55 Pro',
                        system_version='IOS 100.0')

async def start_bot(bot: Bot):
    await client.start()
    await client.send_message('me','Start')
    await client.disconnect()
    await bot.send_message(admin_id, 'Start')

async def get_links(links: Message, bot: Bot):
    await client.start()
    link = links.text.split('\n')
    r = []
    for i in link:
        try:
            await client.get_peer_id(i)
            if i not in r:
                r.append(i)
        except Exception as e:
            if type(e).__name__ == 'FloodWaitError':
                await bot.send_message(links.from_user.id, f'Ваш запрос обрабатывается. Время ожидания: {e.seconds} секунд')
                time.sleep(e.seconds)
            elif e.args[0][:7] == 'No user' or type(e).__name__ in ['InviteHashExpiredError']:
                continue
            else:
                if i not in r:
                    r.append(i)
    else:
        r = '\n'.join(r)
        await bot.send_message(links.from_user.id, r)
    await client.disconnect()
