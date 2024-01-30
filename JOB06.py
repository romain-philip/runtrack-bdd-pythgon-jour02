import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='noah06600',
    host='localhost',
    database='LaPlateforme'
)

cursor = cnx.cursor()

cursor.execute("SELECT SUM(capacite) FROM salle")

capacite_totale = cursor.fetchone()[0]
print(f"La capacité totale des salles est de {capacite_totale}")

cursor.close()
cnx.close()
