import config
from handlers import handlersList
from telegram.ext import Updater

updater = Updater(config.TOKEN, use_context=True)

for handler in handlersList:
    updater.dispatcher.add_handler(handler)

updater.start_webhook(listen="0.0.0.0", port=int(config.PORT), url_path=config.TOKEN)
updater.bot.setWebhook(config.HEROKU + config.TOKEN)