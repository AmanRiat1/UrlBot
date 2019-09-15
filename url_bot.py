import discord
import psycopg2
import os
import logging
import prettytable

TOKEN = ''
PGHOST = os.getenv("POSTGRES_HOST")
PGDATABASE = os.getenv("POSTGRES_DB")
PGUSER = os.getenv("POSTGRES_USER")
PGPASSWORD = os.getenv("POSTGRES_PASSWORD")
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL")

logging.basicConfig(level=LOGGING_LEVEL)
conn_string = "host="+ PGHOST +" port="+ "5432" +" dbname="+ PGDATABASE +" user=" + PGUSER +" password="+ PGPASSWORD
client = discord.Client()

def database_query(operation):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(operation)
        query = cursor.fetchall()
        logging.info('queried information')
        return query

    except (Exception, psycopg2.Error) as error:
        logging.error("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (conn):
            cursor.close()
            conn.close()
            logging.info("PostgreSQL connection is closed")

def make_prettytable(links_list):
    links_table = prettytable.PrettyTable(["Number", "Link"])
    for row in links_list:
        links_table.add_row([row[0], row[1]])
    return links_table

@client.event
async def on_message(message):

    if message.content.startswith('!link'):
        link_number = message.content[6:]
        logging.debug('the content is ' + link_number)
        link_query = f"SELECT * FROM website_information WHERE id={link_number}"
        link = database_query(link_query)
        channel = client.get_channel(518464784803299330)
        await channel.send("Here's the link " + link[0][1])

    if message.content.startswith('!alllinks'):

        link_query = "SELECT * FROM website_information"
        links = database_query(link_query)
        links_table = make_prettytable(links)
        print (links_table)
        channel = client.get_channel(518464784803299330)
        await channel.send(links_table)

    if message.content.startswith('!setlink'):
        new_link = message.content[10:]
        link_info = f"INSERT INTO website_information (url) VALUES('{new_link}')"

        try:
            conn = psycopg2.connect(conn_string)
            cursor = conn.cursor()
            cursor.execute(link_info)
            conn.commit()
            channel = client.get_channel(518464784803299330)
            await channel.send("Saved website")
            logging.info("Saved website")
            await channel.send(new_link)

        except (Exception, psycopg2.Error) as error:
            logging.error("Error while fetching data from PostgreSQL", error)

        finally:
            if (conn):
                cursor.close()
                conn.close()
                logging.info("PostgreSQL connection is closed")
        
@client.event
async def on_ready():
    logging.info('Logged in as ' + client.user.name + ' with id ' + str(client.user.id))

client.run(TOKEN)
