import json
import logging

import discord
from discord.ext import commands
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
import os

with open("database.json", "r") as file:
    data = json.load(file)

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = RotatingFileHandler(filename='discord.log', encoding='utf-8', maxBytes=5*1024*1024, backupCount=1)
handler.setLevel(logging.INFO)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents, activity=discord.Activity(type=discord.ActivityType.listening, name="Dead Man Walking"))
tree = bot.tree
bot.data = data

async def my_setup():
    await bot.load_extension("events.backupSystem")
    await bot.load_extension("events.counterSystem")
    await bot.load_extension("events.submissionSystem")
    await bot.load_extension("events.reviewRatingSystem")
    await bot.load_extension("events.lyricReactionSystem")
    await bot.load_extension("commands.endCommand")
    await bot.load_extension("commands.leaderboardCommand")
    await bot.load_extension("commands.levelCommand")
    await bot.load_extension("commands.purgeCommand")
    await bot.load_extension("commands.resetCommand")
    await bot.load_extension("commands.sayCommand")
    await bot.load_extension("commands.startCommand")
    await bot.load_extension("commands.birthdayCommand")
    await bot.load_extension("commands.reminderCommand")
    await bot.load_extension("commands.lyricCommand")
    await tree.sync(guild=discord.Object(id=1487902534545703072))
    print("Ready")

bot.setup_hook = my_setup

if __name__ == "__main__":
    bot.run(token, log_handler=handler, log_level=logging.DEBUG)