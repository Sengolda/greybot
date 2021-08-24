import contextlib
import datetime as dt
import logging
import re
import traceback
from typing import Optional

import aiosqlite
import discord
from discord.ext import commands

from .context import Context
from lib.config.bot_config import bot_config

logging.basicConfig(
    filename="./lib/cache/bot.log", encoding="utf-8", level=logging.INFO, filemode="w"
)


class BotBase(commands.bot.BotBase, discord.Client):
    def __init__(self):
        self.config = bot_config
        self.start_time = dt.datetime.now(dt.timezone.utc)
        self.token = self.config.token
        self.exts = ["cogs.info", "cogs.admin", "jishaku"]
        self.prefix = "!"
        super().__init__(
            command_prefix=self.prefix,
            intents=discord.Intents.all(),
            owners=self.owners,
            allowed_mentions=discord.AllowedMentions(
                users=True, everyone=False, roles=False, replied_user=True
            ),
        )
        for cog in self.exts:
            self.load_extension(cog)

    owners: Optional[list[discord.User]] = [739443421202087966]

    @property
    def uptime(self):
        return dt.datetime.now(dt.timezone.utc) - self.start_time

    @property
    def owner(self):
        return [self.get_user(owner) for owner in self.owners]

    async def on_ready(self) -> None:
        logging.info(f"Succesfully logged in as {self.user} ({self.user.id})")
        logging.info(f"Logged in at {self.uptime}")
        logging.info("-" * 52)

    async def process_commands(self, message: discord.Message):
        if message.author.bot:
            return

        if message.author == self.user:
            return

        ctx = await self.get_context(message)
        await self.invoke(ctx)

    async def get_context(self, message, *, cls=Context):
        return await super().get_context(message, cls=cls)

    async def setup_database(self):
        if not hasattr(self, "db"):
            self.db = await aiosqlite.connect("./lib/db/bot.db")

    async def on_message(self, message: discord.Message):
        if message.content in (f"<@{self.user.id}>", f"<@!{self.user.id}>"):
            await message.channel.send(f"My prefix is {self.prefix}")
        await self.process_commands(message)

    async def on_connect(self):
        await self.setup_database()
        logging.info("db connected.")
        logging.info("-" * 52)

    async def on_command_error(
        self, ctx: commands.Context, error: commands.CommandError
    ):
        if isinstance(error, commands.CommandNotFound):
            return
        if not isinstance(error, commands.CommandInvokeError):
            title = " ".join(
                re.compile(r"[A-Z][a-z]*").findall(error.__class__.__name__)
            )
            await ctx.send(
                embed=discord.Embed(
                    title=title, description=str(error), color=discord.Color.red()
                )
            )
            return

        if isinstance(error, commands.CommandInvokeError):
            trace_back = traceback.format_exception(
                type(error), error, error.__traceback__
            )
            with open("./lib/cache/errors.log", "a") as f:
                f.write("".join(trace_back))
                f.close()

            embed = discord.Embed(
                title="Error",
                description="An unknown error has occurred and my developer has been notified of it.",
                color=discord.Color.red(),
            )
        with contextlib.suppress(discord.NotFound, discord.Forbidden):
            await ctx.send(embed=embed)
            return

    def run(self):
        return super().run(self.token)
