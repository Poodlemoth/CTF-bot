import discord
import random
import time
import requests

 
TOKEN = {PUT TOKEN HERE}
UTIME = time.time()
client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('$Hello!')

@client.event
async def on_message():
    if message.author == client.user:
        return
    if message.content.startswith('$CTF'):
        url ='https://ctftime.org/api/v1/events/?start='+str(UTIME)+'BTC.json'

        responce = requests.get(url)
        value = responce.json() ['url']
        await client.channel.send("$Current events are... " + value)




client.run(TOKEN)
