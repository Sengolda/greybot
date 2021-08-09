from __future__ import annotations

from discord.ext import commands
import discord
import io

from typing import (
    TYPE_CHECKING,
    Union
    )

if TYPE_CHECKING:
    from discord.asset import ValidAssetFormatTypes
    from .bot import BotBase

__all__ = ("Context",)



CHECK_MARK = "\N{WHITE HEAVY CHECK MARK}"


class Context(commands.Context):
    def __init__(self, **attrs):
        super().__init__(**attrs)
    

    def reply(self, *args, **kwargs):
        mention_author = kwargs.pop("mention_author", True)
        return super().reply(*args, mention_author=mention_author, **kwargs)

    def author_is_in_guild(self, guild: discord.Guild = None):
        guild = guild or self.guild

        if guild.get_member(self.author):
            return True
        
        else:
            return False
    
    async def _get_previous_message(self, message: discord.Message,channel: discord.TextChannel = None):
        channel = channel or self.channel
        async for msg in channel.history(before=message, limit=1):
            return msg
    

    async def download_attachment(message: discord.Message, *, index: int = 0) -> io.BytesIO:
        attachment = io.BytesIO()
        await message.attachments[index].save(attachment)
        return attachment
    