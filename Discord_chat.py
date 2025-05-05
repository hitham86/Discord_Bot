import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging


load_dotenv()
TOKEN = os.getenv("TOKEN")


if not TOKEN:
    raise ValueError("TOKEN not found in environment variables.")


logging.basicConfig(level=logging.INFO)


intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("I'm ready")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    logging.info(f"Received message: {message.content}")

    if message.content.lower() == "hi":
        await message.channel.send("hey how are you?")
    elif message.content.lower() == "bye":
        await message.channel.send("see you later")
    elif message.content.lower() == "cool":
        await message.add_reaction("😎")


    await bot.process_commands(message)


@bot.command()
async def hello(ctx):
    await ctx.send("Hello there!")


@bot.event
async def on_error(event, *args, **kwargs):
    with open("error.log", "a") as f:
        f.write(f"Unhandled error in {event}: {args} {kwargs}\n")


bot.run(TOKEN)





















































