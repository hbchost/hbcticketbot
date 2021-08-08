import discord
import os
from replit import db
from cryptoaddress import EthereumAddress
#import pynacl
#import dnspython
import server
#from discord.ext import commands

#bot = commands.Bot(command_prefix="!")
#TOKEN = os.getenv("DISCORD_TOKEN")

#@bot.event
#async def on_ready():
#    print(f"Logged in as {bot.user.name}({bot.user.id})")

#@bot.command()
#async def ping(ctx):
#    await ctx.send("pong")

#server.server()
#bot.run(TOKEN)





client = discord.Client()

@client.event

async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return
    if isinstance(message.channel, discord.channel.DMChannel):
      if message.author.id == 148038813048897536 and message.content.startswith("$list"):
        keys = db.keys()
        values = []
        for discordid in keys:
          eth_adr = db[discordid] 
          values.append(eth_adr)
        #remove duplicates
        values = list(dict.fromkeys(values))
        await message.author.send(values)
        return
      try:
        eth_adr = EthereumAddress(message.content)
        #print('The address "%s" is valid.' % str(eth_adr))
        await message.author.send('**You will be able to redeem a HBC 90s Mint Pass.** The address **"%s"** is valid.' % str(eth_adr))
        db[str(message.author.id)] = str(eth_adr)
      except ValueError:
        #print('Error: The address is invalid.')
        await message.author.send('Error: The address is invalid.')
      
server.server()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)