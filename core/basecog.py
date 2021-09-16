from discord.ext import commands

from .bot import BotBase


class BaseCog(commands.Cog):
    def __init__(self, bot: BotBase):
        self.bot = bot
