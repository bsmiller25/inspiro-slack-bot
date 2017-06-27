from app import Bot
from os import environ

inspiro_bot = Bot(environ['INSPIRO_API_TOKEN'])
inspiro_bot.run()
