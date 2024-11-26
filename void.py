from settings import settings
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon import errors
api_id = settings.client.api_id
api_hash = settings.client.api_hash
admin_id = settings.bots.admin_id
client = TelegramClient('ms', api_id, api_hash,
                        device_model='iPhone 55 Pro',
                        system_version='IOS 100.0')



from telethon.sync import TelegramClient
from telethon import functions, types
import logging
from telethon.tl.functions.messages import ImportChatInviteRequest
links = [
    'https://t.me/+znSrnq9hc5I3ZmMy',
    'https://t.me/test1jiwoc',
    'https://t.me/+xl7FMyr1FHNjMjcy',
    'https://t.me/mydonortest',
]
bad_links = [
    'https://t.me/+znSrnqfwe9hc5I3ZmMy',
    'https://t.me/tfwfwest1jiwoc',
    'https://t.me/+xlwefw7FMyr1FHNjMjcy',
    'https://t.me/mydefwonortest',
]
links+=bad_links
async def links_check(links):
    for i in links:
        await client.start()
        # result = client.get_peer_id(i)
        # print(i, result)
        try:
            await client.get_peer_id(i)
            print('sux',i)
        except Exception as e:
            # print(e.args[0][:7])
            if e.args[0][:7] == 'No user' or type(e).__name__ in ['InviteHashExpiredError', 'FloodWait']:
                print('Error')
            else:
                print(i)
        # print(await client.get_peer_id('https://t.me/+xlwefw7FMyr1FHNjMjcy'))
        await client.disconnect()



client.loop.run_until_complete(links_check(links))