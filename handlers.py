import functions
from telegram.ext import CommandHandler

handlersList = []
handlersList.append(CommandHandler('start', functions.start))
handlersList.append(CommandHandler('help', functions.help))
handlersList.append(CommandHandler('escalacao', functions.escalacao, pass_args=True))