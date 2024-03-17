from sys import stderr

from loguru import logger

from src import config
from src.classes import bot

# Setup logging
logger.remove(0)
logger.add(stderr, format=config.get_var("logger.terminalFormat"), colorize=True, level=config.get_var("logger.level"))
logger.add(config.get_var("logger.path"), format=config.get_var("logger.fileFormat"), level=config.get_var("logger.level"))

# Other initializing
logger.info("Starting...")

try:
    bot.JustBot(config.get_var("bot.token")).run()
except Exception as e:
    logger.exception(e)
