import discord
import random
import time
import requests

BOT_PREFIX = ("!","?")  
TOKEN = {PUT TOKEN HERE}
client = Bot(command_prefix=BOT_PREFIX)
UTIME = time.time()

@client.event()
async def on_message():
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('$Hello!')

@client.command()
async def CTF():
    url ='https://ctftime.org/api/v1/events/?start='+str(UTIME)+'BTC.json'

    responce = requests.get(url)
    value = responce.json() ['url']
    await client.say ("Current events are... " + value)




client.run(TOKEN)
