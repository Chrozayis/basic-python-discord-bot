import discord
import asyncio
import logging
import random
import requests

owner = 'example#1234'
token = ''

# ===FROM HERE===
logging.basicConfig(level=logging.INFO)

client = discord.Client()


@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print(client)


@client.event
async def on_message(message):
# ===TO ABOUT HERE===
# is pure magic, don't ask me what is going on

    # Logs server activity to terminal
    print(str(message.author) + ' @ ' + str(message.channel) + ' : ' + message.content)

    # ping th bot and it pongs back!
    if message.content.startswith(']ping'):
        await client.send_message(message.channel, message.author.mention + ' pong!')

    # prints a helpful message
    if message.content.startswith(']help'):  # make sure to update this with new commands as they are added
        await client.send_message(message.channel,
        '```' +
        ']help : Prints this help message\n'
        ']ping : Ping me and I will pong you back!\n'
        ']roll : Roll a die\n'
        ']flip : Flip a coin'
        ']cat  : Finds a cute cat'
        '```')

        # unlisted commands:
        # ]catgif, sometimes fails
        # ]eval, can be used to dump internal variables to Discord
        # ]game, sets the bot's playing status

    # coinflip, flips a coin
    if message.content.startswith((']coinflip', ']flip')):
        tmp = await client.send_message(message.channel, 'flipping coin...')
        flip = random.randint(0, 1)
        if flip == 0:
            await client.edit_message(tmp, 'tails')
        else:
            await client.edit_message(tmp, 'heads')

    # die roll
    if message.content.startswith(']roll'):
        tmp = await client.send_message(message.channel, 'rolling die...')
        roll = random.randint(1, 6)
        await client.edit_message(tmp, roll)

    # no Discord bot is complete without the ability to find cats, courtesy of theCatApi
    if message.content.startswith(']catgif'):
            # output a cat picture
            await client.send_message(message.channel, requests.get('http://thecatapi.com/api/images/get?format=src&type=gif').url + ' :cat:')
    elif message.content.startswith(']cat'):
            # output a cat picture
            await client.send_message(message.channel, requests.get('http://thecatapi.com/api/images/get?format=src&type=jpg').url + ' :cat:')

    # can spit out internal variables into Discord, sometimes useful
    if message.content.lower().startswith(']eval '):
        if str(message.author) == owner:
            await client.send_message(message.channel, eval(message.content[6:]))
        else:
            await client.send_message(message.channel, 'you do not have permission to do that')

    # for setting the playing status
    if message.content.lower().startswith(']game '):
        if str(message.author) == owner:
            await client.change_presence(game=discord.Game(name=message.content[6:]))
        else:
            await client.send_message(message.channel, 'you do not have permission to do that')

    # self explanatory
    if message.content.lower().startswith((']whoisagoodbot', ']whoisthebestbot')):
        await client.send_message(message.channel, 'I am!')

client.run(token)
