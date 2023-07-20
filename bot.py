import discord
import random
import random,os
from bot_logic import*

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)



#events
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hola'):
        await message.channel.send(presentacion_es(1))
    elif message.content.startswith('no quiero'):
        await message.channel.send(":skull:")
    elif message.content.startswith("que es contaminacion"):
        await message.channel.send(random_es1(1))
    elif message.content.startswith("como prevenir la contaminacion"):
        await message.channel.send(random_es2(1))

client.run("####")

#not finished yet :)
