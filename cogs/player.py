import argparse
import logging
import sys
import zeroconf

import discord
from discord.ext import commands
import pychromecast
from pychromecast.controllers.youtube import YouTubeController

CAST_NAME = "CAST NAME HERE"

class BasicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, url):
        if not url:
            ctx.send("Invalid link. Format like: `!play https://www.youtube.com/watch?v=dQw4w9WgXcQ`")
            return
        url = url(s[32:])

        services, browser = pychromecast.discovery.discover_chromecasts()
        pychromecast.discovery.stop_discovery(browser)

        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[CAST_NAME])

        if not chromecasts:
            print('No chromecast with name "{}" discovered'.format(CAST_NAME))
            sys.exit(1)

        cast = chromecasts[0]
        # Start socket client's worker thread and wait for initial status update
        cast.wait()

        yt = YouTubeController()
        cast.register_handler(yt)
        yt.play_video(url)

        # Shut down discovery
        browser.stop_discovery()
                
def setup(bot):
    bot.add_cog(BasicCog(bot))