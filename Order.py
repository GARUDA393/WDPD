import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sql123$",
    database="university"
)

cursorObject = database.cursor()

query = "SELECT * FROM STUDENT ORDER BY NAME ASC"

cursorObject.execute(query)

myresult = cursorObject.fetchall()

for x in myresult:
    print(x)
    database.close()
