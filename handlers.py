import functions
from telegram.ext import CommandHandler

handlersList = []
handlersList.append(CommandHandler('start', functions.start))
handlersList.append(CommandHandler('help', functions.help))