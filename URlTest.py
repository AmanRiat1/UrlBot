# Work with Python 3.6
import discord

TOKEN = 'NDk1NDMwNTMzNTY4NzkwNTI4.DpE_Yg.vFSZLtuhm3wTYd0FSdOhlzdqkAY'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

client.run(TOKEN)
