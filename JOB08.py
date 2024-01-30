import mysql.connector
from datetime import datetime

class Animal:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()

    def create(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def read(self, id):
        query = "SELECT * FROM animal WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def update(self, id, nom, race, id_cage, date_naissance, pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (nom, race, id_cage, date_naissance, pays_origine, id)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def delete(self, id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.cnx.commit()

class Cage:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()

    def create(self, superficie, capacite):
        query = "INSERT INTO cage (superficie, capacite) VALUES (%s, %s)"
        values = (superficie, capacite)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def read(self, id):
        query = "SELECT * FROM cage WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def update(self, id, superficie, capacite):
        query = "UPDATE cage SET superficie = %s, capacite = %s WHERE id = %s"
        values = (superficie, capacite, id)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def delete(self, id):
        query = "DELETE FROM cage WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.cnx.commit()

cnx = mysql.connector.connect(
    user='root',
    password='noah06600',
    host='localhost'
)

cursor = cnx.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS zoo")

cursor.execute("USE zoo")

cursor.execute("""
    CREATE TABLE animal (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255),
        race VARCHAR(255),
        id_cage INT,
        date_naissance DATE,
        pays_origine VARCHAR(255)
    )
""")

cursor.execute("""
    CREATE TABLE cage (
        id INT AUTO_INCREMENT PRIMARY KEY,
        superficie INT,
        capacite INT
    )
""")

cnx.commit()

animal = Animal(cnx)
cage = Cage(cnx)

cage.create(100, 5)

animal.create('Lion', 'Panthera leo', 1, datetime.now().date(), 'Afrique')

cursor.execute("SELECT * FROM animal")
for animal in cursor:
    print(animal)

cursor.execute("SELECT SUM(superficie) FROM cage")
superficie_totale = cursor.fetchone()[0]
print(f"La superficie totale de toutes les cages est de {superficie_totale} m2")

cursor.close()
cnx.close()
