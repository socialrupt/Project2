import asyncio
from telethon import TelegramClient, events
import time
api_id = 2564501
api_hash = "bd2008ffe2eb9a032917b32b03ad18ea"
client = TelegramClient('anon', api_id, api_hash)


client.start()

def run():
    @client.on(events.NewMessage(pattern=r'Please use the correct format.'))
    async def handler(event):
        await asyncio.sleep(300)
        await event.delete()

    client.run_until_disconnected()


with client:
    client.loop.run_until_complete(run())









