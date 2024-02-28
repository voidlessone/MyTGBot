 
from telethon import TelegramClient, sync
from telethon import events

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id =  DDDDDD 
api_hash = 'DDDDDDDDDDD'

client = TelegramClient('selfbot', api_id, api_hash).start()


#@client.on(events.NewMessage(incoming=True, pattern='love'))
@client.on(events.NewMessage(pattern='love'))
async def handler(event):
    #print(event.message.message)
    await event.reply('Hey!')

client.run_until_disconnected()
