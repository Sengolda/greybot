from typing import *


from discord.ext import commands
import discord

class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

Emoji = Union[
    discord.Emoji,
    str,
]


TextChannel = Union[
    discord.TextChannel,
    discord.DMChannel,
    discord.abc.Messageable,
]


VocalGuildChannel = Union[
    discord.VoiceChannel,
    discord.StageChannel,
]


GuildChannel = Union[
    discord.TextChannel,
    VocalGuildChannel,
    discord.CategoryChannel,
    discord.StoreChannel,
]


User = Union[
    discord.Member,
    discord.User,
]


DiscordEmoji = Union[
    discord.Emoji,
    discord.PartialEmoji,
]


Message = Union[
    discord.Message,
    discord.PartialMessage,
]

Msg = Message

DiscordObject = Union[
    discord.Guild,
    discord.Role,
    GuildChannel,
    User,
    DiscordEmoji,
    Message,
    discord.Invite,
]