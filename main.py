import os

import discord
from discord.ext import commands


bot = commands.Bot(
    command_prefix = '!',
    case_insensitive=True
)

def import_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            bot.load_extension(f'cogs.{cog[:-3]}')

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

if __name__ == '__main__':
    import_cogs()
    bot.run("TOKEN HERE")