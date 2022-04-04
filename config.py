import os

HEROKU='https://telegram-rebot.herokuapp.com/'
TOKEN=os.getenv('TOKEN')
PORT=int(os.environ.get('PORT', 5000))