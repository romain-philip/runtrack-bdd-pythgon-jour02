import mysql.connector


cnx = mysql.connector.connect(
    user='root',
    password='noah06600',
    host='localhost',
    database='LaPlateforme'
)


cursor = cnx.cursor()

cursor.execute("SELECT * FROM etudiants")

for etudiant in cursor:
    print(etudiant)

cursor.close()
cnx.close()
