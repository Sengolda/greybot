import discord
from discord.ext import commands
from .utils._types import *

class Info(Cog):
    @commands.command()
    async def about(self, ctx):
        owner = ", ".join(str(owner) for owner in self.bot.owner)

        await ctx.send(
            embed=discord.Embed(
                colour=ctx.me.colour,
                description=f"I am {self.bot.user}, a bot made by {owner}. My prefix is {self.bot.prefix}.",
            ).set_author(name=f"About {self.bot.user.name}:")
        )
    
    @commands.command()
    async def role_info(self, ctx, *, role: discord.Role):

        embed = discord.Embed(title=role.name)
        if role.colour.value:
            embed.colour = role.colour

        embed.add_field(
            name="Permissions:",
            value=f"[Permissions list](https://discordapi.com/permissions.html#{role.permissions.value})",
        )
        embed.add_field(name="Displayed Separately:", value=role.hoist)
        embed.add_field(name="Is Mentionable:", value=role.mentionable)
        embed.add_field(name="Colour:", value=str(role.colour) if role.colour.value else "None")

        if ctx.guild.chunked:
            role_members = [i for i in role.members]
            embed.add_field(name="Members:", value=len(role_members), inline=False)

        await ctx.send(embed=embed)
    

def setup(bot):
    bot.add_cog(Info(bot))