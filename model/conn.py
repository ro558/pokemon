import mysql.connector


def connection():
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="",
      database="Pokedex"
    )

    return mydb, mydb.cursor()
