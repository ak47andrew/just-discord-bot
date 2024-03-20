from src.database import models
import peewee as pw


def get_command_description(command: str) -> str:
    try:
        return models.Help.select().where(models.Help.command == command).get().description
    except pw.DoesNotExist:
        return models.Help.description.default
