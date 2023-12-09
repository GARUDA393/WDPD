import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="sql123$",
    database="university"
)

cursorObject = database.cursor()

StudentRecord = """CREATE TABLE STUDENT(
                    NAME VARCHAR(20) NOT NULL, 
                    BRANCH VARCHAR(5),
                    ROLL INT NOT NULL,
                    SECTION VARCHAR(5),
                    AGE INT)"""

cursorObject.execute(StudentRecord)
database.close()
