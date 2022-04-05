import psycopg2
from config import DATABASE_URL

connection = None

def connect():
    global connection
    try:
        connection = psycopg2.connect(DATABASE_URL)
        return True
    except:
        print('Error while connecting to database :(')
        return False

def query(command, parameters=[]):
    result = None
    try:
        connect()
        cursor = connection.cursor()
        cursor.execute(command, vars=tuple(parameters))
        print(cursor.query)
        if ('SELECT' in command[:6] and cursor.rowcount>0):
            result = cursor.fetchall()
    except:
        print('Error while executing query :(')      
    finally:
        if connection:
            connection.commit()
            cursor.close()
            connection.close()
        return result
