import config
from handlers import handlersList
from telegram.ext import Updater

updater = Updater(config.TOKEN, use_context=True)

for handler in handlersList:
    updater.dispatcher.add_handler(handler)

# updater.start_webhook('127.0.0.1', 2009, )

updater.start_polling()
