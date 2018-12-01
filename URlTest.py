import discord

TOKEN = 'NDk1NDMwNTMzNTY4NzkwNTI4.DuRBKA.f34cK_LnmCNK6c62O-6n8uNjlJk'

client = discord.Client()

@client.event
async def on_message(message):
    a = 'https://www.google.ca'
    if message.author == client.user:
        return

    if message.content.startswith('!link'):
        msg = " Here's the link {}".format(a)
        await client.send_message(message.channel, msg)


        

client.run(TOKEN)
