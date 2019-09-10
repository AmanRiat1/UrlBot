import discord
import psycopg2
import os 

TOKEN = 'NDk1NDMwNTMzNTY4NzkwNTI4.DuS9ZQ.tZcHzt8kMr7CJvBmb0jB7eT78Hs'
PGHOST = os.getenv("POSTGRES_HOST")
PGDATABASE = os.getenv("POSTGRES_DB")
PGUSER = os.getenv("POSTGRES_USER")
PGPASSWORD = os.getenv("POSTGRES_PASSWORD")


conn_string = "host="+ PGHOST +" port="+ "5432" +" dbname="+ PGDATABASE +" user=" + PGUSER +" password="+ PGPASSWORD
conn=psycopg2.connect(conn_string)
print("Connected!")
cursor = conn.cursor()

client = discord.Client()

@client.event

async def on_message(message):
    a = 'https://www.google.ca'

    if message.content.startswith('!link'):
        msg = " Here's the link {}".format(a)
        channel = client.get_channel(518464784803299330)
        await channel.send(msg)

    if message.content.startswith('!set_link'):
        new_link = message.content[8:]
        sql = "INSERT INTO website_information VALUES({new_link})"
        channel = client.get_channel(518464784803299330)
        await channel.send("Saved website")
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
