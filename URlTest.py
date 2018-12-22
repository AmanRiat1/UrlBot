import discord
from discord.ext import commands
TOKEN = 'NDk1NDMwNTMzNTY4NzkwNTI4.DuS9ZQ.tZcHzt8kMr7CJvBmb0jB7eT78Hs'

client = discord.Client()

bot = commands.Bot(command_prefix='!')

@client.event
async def on_message(message):
    link = 'https://www.google.ca'
    strike = 0
    
    if message.author == client.user:
        return
    
    if message.content.startswith('!editme'):
        new_link = message.content[8:]
        link = new_link
        await client.send_message(message.channel, new_link)
    
    if message.content.startswith('!link'):
        msg = " Here's the link {}".format(link)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!strike'):
        strike += 1
        msg = '{} strikes'.format(strike)
        await client.send_message(message.channel,msg)

    if message.content.startswith('!kick'):
        kick(discord.Member)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))
    


client.run(TOKEN)
