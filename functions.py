import emoji
import queries
import database as db
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(emoji.emojize('Opa, e ai, belezinha?!\n\n Sou o ReBot, um botzin futebolístico que faz algumas coisinhas inúteis por aí :soccer_ball:\n\n Você pode digitar um /help para ver os comandos disponíveis :winking_face:', language='en'))

def help(update: Update, context: CallbackContext):
    update.message.reply_text(emoji.emojize('Camarada, posso fazer isso daqui ó:\n\n/start \- Pontapé inicial\n/help \- VAR nas funcionalidades\n\nEstou no processo de desenvolvimento, se tiver sugestões, mande em [Jpbelluzzo \- ReBot](https://github.com/Jpbelluzzo/ReBot)', language='es'), parse_mode='MarkdownV2')

def escalacao(update: Update, context: CallbackContext):
    time = context.args[0]
    update.message.reply_text(time)
    result = db.query(queries.get_escalacao_equipes)
    if (result == None):
        update.message.reply_text(emoji.emojize('Esse time ainda não tá disponível :('))