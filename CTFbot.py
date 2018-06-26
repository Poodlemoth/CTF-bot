from discord.ext.commands import Bot
from discord import Game
import random
import time
import requests

BOT_PREFIX = ("!","?")  
TOKEN = 'Mjg1ODU0MDk4OTcwOTAyNTI5.DhMEqA.5hpwdiHc0jkOgn2gm4I_KpoRzA0'
client = Bot(command_prefix=BOT_PREFIX)
UTIME = time.time()

@client.command()
async def Hello():
    responces = [
        'Hello, How are you?',
        'Hello'
    ]
    await client.say(random.choice(responces))

@client.command()
async def CTF():
    url ='https://ctftime.org/api/v1/events/?start='+str(UTIME)+'BTC.json'

    responce = requests.get(url)
    value = responce.json() ['url']
    await client.say ("Current events are... " + value)




client.run(TOKEN)
