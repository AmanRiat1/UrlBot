import discord

TOKEN = 'NDk1NDMwNTMzNTY4NzkwNTI4.DpE_Yg.vFSZLtuhm3wTYd0FSdOhlzdqkAY'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!link'):
        msg = " Here's the link {0.author.mention} https://www.google.ca/".format(message)
        await client.send_message(message.channel, msg)

client.run(TOKEN)
