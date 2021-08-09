from core.bot import BotBase as CustomBotBase
from discord.ext.commands import Bot

class BotBase(Bot, CustomBotBase):
    ...