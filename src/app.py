import asyncio
import os

import aiotg


BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
BOT_NAME = os.environ.get('TG_BOT_NAME')
assert all([BOT_TOKEN, BOT_NAME])

BOT_MENTION_NAME = '@{}'.format(BOT_NAME.lower())
bot = aiotg.Bot(api_token=BOT_TOKEN, name=BOT_NAME)


async def say_hello(chat):
    msg = 'Hello {} from EuroPython 2017!'.format(chat.sender.get('first_name') or '%username%')
    return await chat.reply('msg')


@bot.command(r'/hello')
async def hello(chat, match):
    return await say_hello(chat)


@bot.default
async def default_handler(chat, message):
    if BOT_MENTION_NAME in message.lower():
        return await say_hello(chat)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(bot.loop())

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        bot.stop()
        loop.stop()
