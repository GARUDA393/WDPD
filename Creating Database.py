import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sql123$"
)

cursorObject = database.cursor()
cursorObject.execute("CREATE DATABASE UNIVERSITY")
