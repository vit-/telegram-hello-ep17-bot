import asyncio
import os

import aiotg


BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
BOT_NAME = os.environ.get('TG_BOT_NAME')
assert all([BOT_TOKEN, BOT_NAME])

bot = aiotg.Bot(api_token=BOT_TOKEN, name=BOT_NAME)


@bot.command(r'/hello')
async def hello(chat, match):
    msg = 'Hey {}! Welcome to EuroPython 2017!'.format(
        chat.sender.get('first_name') or '%username%')
    return await chat.reply(msg)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.loop())
