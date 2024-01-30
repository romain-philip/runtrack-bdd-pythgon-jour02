import mysql.connector

cnx = mysql.connector.connect(
    user='root',
    password='noah06600',
    host='localhost',
    database='LaPlateforme'
)

cursor = cnx.cursor()

cursor.execute("SELECT SUM(superficie) FROM etage")

superficie_totale = cursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {superficie_totale} m2")

cursor.close()
cnx.close()
