from email import message
import emoji
import queries
import database as db
from telegram import Update, Message
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    update.message.reply_text(emoji.emojize('Opa, e ai, belezinha?!\n\n Sou o ReBot, um botzin futebolístico que faz algumas coisinhas inúteis por aí :soccer_ball:\n\n Você pode digitar um /help para ver os comandos disponíveis :winking_face:', language='en'))

def help(update: Update, context: CallbackContext):
    update.message.reply_text(emoji.emojize('Camarada, posso fazer isso daqui ó:\n\n/start \- Pontapé inicial\n/help \- VAR nas funcionalidades\n\nEstou no processo de desenvolvimento, se tiver sugestões, mande em [Jpbelluzzo \- ReBot](https://github.com/Jpbelluzzo/ReBot)', language='es'), parse_mode='MarkdownV2')

# Informs the lineup of a team for a game to users subscribed to this team
def escalacao(update: Update, context: CallbackContext):
    time = context.args[0]                                              # team passed as parameter
    result = db.query(queries.get_equipes)                              # verify if team is available
    if ((result == None) or (time not in result)):                          
        update.message.reply_text('Esse time ainda não tá disponível :(')
    else:                                                               # if team is available...
        user = update.message.from_user.username                        # get username
        result = db.query(queries.get_usuarios_equipe, [time])          # verify if user has already subscribed to this team
        if user in result:
            update.message.reply_text(emoji.emojize('Você já está acompanhando as escalações desse time :wink:', language='en'))
        else:                                                           # if user has not subscribed to this team yet
            result = db.query(queries.set_equipe_usuarios, [user, time])
            str = 'Agora você está acompanhando as escalações do ' + time + ' :wink:'
            update.message.reply_text(emoji.emojize(str, language='en'))
