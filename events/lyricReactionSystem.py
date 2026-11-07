import random
import discord
from discord.ext import commands

class LyricReactionSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.guild is None:
            return
        lyrics = self.bot.lyrics
        for song in lyrics:
            title = song.split(" - ")[0]

            if " " + title + " " in message.content.lower() or message.content.lower().startswith(title + " ") or message.content.lower().endswith(" " + title) or message.content.lower() == title:
                lines = lyrics[song]
                line_index = random.randrange(0, len(lines))
                await message.channel.send(lines[line_index])
                await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=title))


async def setup(bot):
    await bot.add_cog(LyricReactionSystem(bot))