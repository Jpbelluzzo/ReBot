import os

HEROKU='https://telegram-rebot.herokuapp.com/'
TOKEN=os.getenv('TOKEN')
DATABASE_URL=os.getenv('DATABASE_URL')
PORT=int(os.environ.get('PORT', 5000))