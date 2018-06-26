from discord.ext import commands
import requests
import json

with open("./auth.json", "r") as read_file:
	data = json.load(read_file)
TOKEN = data.get("token")
#prefix = data.get("prefix")

prefix = "$"
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
	print(message.content)
	await bot.process_commands(message)



@bot.command()
async def ping(ctx):
	await ctx.send(bot.latency)


@bot.command()
async def hello(ctx):
	await ctx.send("Hello!")

@bot.command()
async def ctf(ctx):
	url ='https://ctftime.org/api/v1/events/?start='+str(UTIME)+'BTC.json'

	responce = requests.get(url)
	value = responce.json() ['url']
	await bot.channel.send("Current events are... " + value)

bot.run(TOKEN)				
