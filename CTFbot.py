from discord.ext import commands
import discord
import requests
import json
import time


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
	#print(message.content)
	await bot.process_commands(message)

@bot.command()
async def ping(ctx):
	await ctx.send(bot.latency)


@bot.command()
async def hello(ctx):
	await ctx.send("Hello!")

@bot.command()
async def ctf(ctx):
	url ='https://ctftime.org/api/v1/events/?limit=100&start=' + str((int(time.time()))) + '&finish=' + str((int(time.time())+4838400))
	print(url)

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
	r = requests.get(url, headers=headers)

	ctfs = r.json()
	ctflist = []
	i = 0
	#Title Date Link

	for ctf in ctfs:
		if ctf.get('onsite') != True:
			ctflist.append({'title':ctf.get('title'), 'date':ctf.get('start'), 'link':ctf.get('url')})	
			print(ctf.get('onsite'))
		
			if i<5:
				embed=discord.Embed(title=ctflist[i].get('title'), url="https://google.com", description=ctflist[i].get('date'), color=0x00dcff)
				embed.set_footer(text='Retrieved from ctftime.org')
				await ctx.send(embed=embed)

			i += 1

@bot.command()
async def ctfplus(ctx):
	url ='https://ctftime.org/api/v1/events/?limit=100&start=' + str((int(time.time()))) + '&finish=' + str((int(time.time())+4838400))
	print(url)

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
	r = requests.get(url, headers=headers)

	ctfs = r.json()
	ctflist = []
	i = 0
	#Title Date Link

	for ctf in ctfs:
		if ctf.get('onsite') != True:
			ctflist.append({'title':ctf.get('title'), 'desc':ctf.get('description'), 'date':ctf.get('start'), 'link':ctf.get('url')})	
			print(ctf.get('onsite'))
		
			if i<5:
				embed=discord.Embed(title=ctflist[i].get('title'), url="https://google.com", description=ctflist[i].get('date'), color=0x00dcff)
				embed.add_field(name="Description", value=ctflist[i].get('desc'), inline=True)
				embed.set_footer(text='Retrieved from ctftime.org')
				await ctx.send(embed=embed)

			i += 1
bot.run(TOKEN)				
