import discord

TOKEN = 'Mjg1ODU0MDk4OTcwOTAyNTI5.DhMEqA.5hpwdiHc0jkOgn2gm4I_KpoRzA0'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('loggen in as')
    print('client.user.name')
    print('client.user.id')
    print('------')

client.run(TOKEN)
