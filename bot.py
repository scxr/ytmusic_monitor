import discord
from discord.ext.commands import Bot
from discord.ext import commands, tasks
import asyncio
bot = commands.Bot(command_prefix='djkhfhkfehfwkfhkewhkwejfh√ç√√∫ƒ^ß', description='Hi')

@bot.event
async def on_ready():
    print('Bot is online')
    bot.loop.create_task(mytask())

async def mytask():
    while 1:
        listening_to = open('tmp.txt').read()
        print(listening_to)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listening_to))
        await botasyncio.sleep(10)
bot.run('', bot=False)
