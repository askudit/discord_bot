import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response, contains_blacklisted_words, generate_warning_message
from discord.ext import commands
import discord

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')

intents=Intents.default()
intents.message_content=True
client=discord.Client(intents=intents)
bot = commands.Bot(command_prefix="$", intents=intents)


async def send_msg(message,usr_message):
    if not usr_message:
        print("mind checking the intents ig it wasnt enabled properly")
        return
    is_private = usr_message[0]=='?'
    if is_private:
        usr_message=usr_message[1:]

    try:
        response=get_response(usr_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f"Error sending message: {e}")


@client.event
async def on_ready():
    try:
        print(on_ready)
    except Exception as e:
        print(f"Error on_ready: {e}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    username=str(message.author)
    user_message=message.content
    channel=str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_msg(message, user_message)

    if message.author == client.user:
        return

    if contains_blacklisted_words(message):
        try:
            warning_message = generate_warning_message(message.author)
            await message.channel.send(warning_message)
            await message.delete()
        except discord.Forbidden:
            await message.channel.send("I don't have permission to delete messages.")
        except discord.HTTPException as e:
            print(f"Failed to delete message: {e}")

def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()