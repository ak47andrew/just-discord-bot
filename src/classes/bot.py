from datetime import datetime
from typing import Any
from discord import Colour, Embed, EmbedAuthor, TextChannel
from discord.ext import commands
from loguru import logger
from src.config import get_var
from src.cogs import cogs
import traceback


class JustBot(commands.Bot):
    token: str
    log_channel: TextChannel

    def __init__(self, token: str):
        super().__init__(command_prefix="None")  # type: ignore
        self.token = token
        logger.trace("Initilised bot")

        logger.trace("Start loading cogs")
        for cog in cogs:
            try:
                self.add_cog(cog)
                logger.trace(f"Loaded cog {cog.qualified_name} sucsessfuly")
            except Exception as e:
                logger.error(f"Error happend while loading {cog.qualified_name}\n{traceback.format_exception(e)[:-1]}")
        logger.trace(f"Sucsesfully loaded {len(cogs)} cogs")

    async def on_ready(self):
        log_channel = await self.fetch_channel(int(get_var("logger.channel")))
        if not isinstance(log_channel, TextChannel):
            raise ValueError("You should specify TextChannel id in logger.channel")
        self.log_channel = log_channel

        logger.info(get_var("logger.messages.onReady"))
        if self.user is None: raise Exception()

        await log_channel.send(embed=Embed(
            title=get_var("logger.messages.onReady"),
            color=Colour.random(seed=self.application_id),
            timestamp=datetime.now(),
            author=EmbedAuthor(
                name=self.user.display_name,
                icon_url=self.user.display_avatar.url
            )
        ))

    async def on_command_error(self, context: commands.Context, exception: commands.CommandError) -> None:  # type: ignore
        logger.error(f"Error happend while executing {context.command.name}\n{traceback.format_exception(exception)[:-1]}")  # type: ignore

    async def on_error(self, event_method: str, *args: Any, **kwargs: Any) -> None:
        logger.error(f"Error in the function {event_method} | args={args} | kwargs={kwargs}\n{traceback.format_exc()[:-1]}")

    def run(self) -> None:  # type: ignore
        logger.trace("Connecting to discord servers...")
        return super().run(self.token)
