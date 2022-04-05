import config
from handlers import handlersList
from telegram.ext import Updater

updater = Updater(config.TOKEN, use_context=True)

updater.bot.set_my_commands([('start', 'Pontapé inicial'), ('help', 'VAR nas funcionalidades'), ('escalacao', 'Veja a escalação do seu time pro jogo que vai rolar')])

for handler in handlersList:
    updater.dispatcher.add_handler(handler)

updater.start_webhook(listen="0.0.0.0", port=int(config.PORT), url_path=config.TOKEN)
updater.bot.setWebhook(config.HEROKU + config.TOKEN)

# updater.start_polling()