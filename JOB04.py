import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='noah06600',
    host='localhost',
    database='LaPlateforme'
)

cursor = cnx.cursor()

cursor.execute("SELECT nom, capacite FROM salle")

for salle in cursor:
    print(salle)

cursor.close()
cnx.close()
