from discord.ext import commands
from discord.ext.commands.context import Context
from jishaku.codeblocks import codeblock_converter as Codeblock

from .utils._types import *

Extension = str


class Admin(Cog):
    async def cog_check(self, ctx: Context) -> bool:
        return await commands.is_owner().predicate(ctx)

    @commands.command(hidden=True)
    async def eval(self, ctx: Context, *, code: Codeblock) -> None:
        """Evaluates python code.
        `code`: Python code to run.
        """
        jsk_py = self.bot.get_command("jsk python")
        if jsk_py is None:
            raise commands.CommandNotFound()
        else:
            await ctx.invoke(jsk_py, argument=code)

    @commands.command(aliases=["sh"], hidden=True)
    async def shell(self, ctx: Context, *, code: Codeblock) -> None:
        """Executes a command in the shell.
        `code`: The command to run.
        """
        jsk_py = self.bot.get_command("jsk sh")
        if jsk_py is None:
            raise commands.CommandNotFound()
        else:
            await ctx.invoke(jsk_py, argument=code)

    @commands.command(hidden=True)
    async def git(self, ctx: Context, *, code: Codeblock) -> None:
        """Executes a git command.
        `code`: The command to run.
        """
        jsk_git = self.bot.get_command("jsk git")
        if jsk_git is None:
            raise commands.CommandNotFound()
        else:
            await ctx.invoke(jsk_git, argument=code)

    @commands.command(hidden=True)
    async def load(self, ctx: Context, *extensions: Extension) -> None:
        """Load extensions.
        `extensions`: The extensions to load.
        """
        jsk_load = self.bot.get_command("jsk load")
        if jsk_load is None:
            raise commands.CommandNotFound()
        else:
            await ctx.invoke(jsk_load, *extensions)

    @commands.command(hidden=True)
    async def unload(self, ctx: Context, *extensions: Extension) -> None:
        """Unload extensions.
        `extensions`: The extensions to unload.
        """
        jsk_unload = self.bot.get_command("jsk unload")
        if jsk_unload is None:
            raise commands.CommandNotFound()
        else:
            await ctx.invoke(jsk_unload, *extensions)

    @commands.group(invoke_without_command=False, hidden=True)
    async def reload(self, ctx: Context, *extensions: Extension) -> None:
        """Reload extensions.
        `extensions`: The extensions to reload.
        """
        jsk_reload = self.bot.get_command("jsk reload")
        if jsk_reload is None:
            raise commands.CommandNotFound()
        else:
            await ctx.invoke(jsk_reload, *extensions)

    @commands.command(aliases=["logout", "exit"], hidden=True)
    async def restart(self, ctx: Context):
        """Restarts the bot."""
        jsk_shutdown = self.bot.get_command("jsk shutdown")
        if jsk_shutdown is None:
            await self.bot.close()
            return
        else:
            await ctx.invoke(jsk_shutdown)


def setup(bot):
    bot.add_cog(Admin(bot))
