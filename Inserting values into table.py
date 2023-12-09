import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sql123$",
    database="university"
)

cursorObject = database.cursor()

sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)" \
      "VALUES (%s, %s, %s, %s, %s)"
val = [("NIKHIL", "CSE", "98", "A", "18"),
       ("NISHA", "CSE", "99", "A", "19"),
       ("ROHAN", "MAE", "43", "B", "20"),
       ("AMIT", "ECE", "24", "A", "21"),
       ("ANIL", "MAE", "45", "B", "20"),
       ("MEGHA", "ECE", "55", "A", "22"),
       ("SITA", "CSE", "95", "A", "19")]

cursorObject.executemany(sql, val)
database.commit()
database.close()
