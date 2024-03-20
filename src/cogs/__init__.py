from discord import Cog
from src.cogs.info import Info

cogs: tuple[type[Cog]] = (
    Info,
)

__all__ = ("cogs",)
