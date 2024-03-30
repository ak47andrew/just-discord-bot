import discord
from discord.ext import commands
from typing import DefaultDict
from src.database import api


class Info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.name = "Info"

    @discord.commands.slash_command()
    async def help(self, ctx: discord.ApplicationContext):
        categories: dict[str, list[discord.ApplicationCommand]] = DefaultDict(lambda: list())
        for command in self.bot.application_commands:
            categories[command.cog.name if commands.cog is not None else "No category"].append(command)

        def format_command(command: discord.ApplicationCommand) -> str:
            return f"`{command.name}` - *{api.get_command_description(command.name)}*\n"

        def format_category(name: str, commands: list[discord.ApplicationCommand]) -> str:
            out = f"**{name}:**\n"

            for command in commands:
                out += format_command(command)

            return out

        await ctx.respond(embed=discord.Embed(
            title="Commands",
            color=discord.Color.random(seed=self.bot.application_id),
            description="\n".join([format_category(*category) for category in categories.items()])
        ))

    @discord.commands.slash_command()
    async def configure(self, ctx: discord.ApplicationContext):
        pass
