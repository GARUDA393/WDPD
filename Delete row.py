import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sql123$",
    database="university"
)

cursorObject = database.cursor()

query = "DELETE FROM STUDENT WHERE NAME='NIKHIL'"

cursorObject.execute(query)
database.commit()
database.close()
