import discord
import requests

client = discord.Client() 

TOKEN = {PUT TOKEN HERE}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(TOKEN)

@client.event
async def on_message():
    if message.author == client.user:
        return
    if message.content.startswith('$CTF'):
        url ='https://ctftime.org/api/v1/events/?start='+str(UTIME)+'BTC.json'

        responce = requests.get(url)
        value = responce.json() ['url']
        await client.channel.send("$Current events are... " + value)
