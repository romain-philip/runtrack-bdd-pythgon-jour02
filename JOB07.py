import mysql.connector

class Salarie:
    def __init__(self, cnx):
        self.cnx = cnx
        self.cursor = self.cnx.cursor()

    def create(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def read(self, id):
        query = "SELECT * FROM employe WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def update(self, id, nom, prenom, salaire, id_service):
        query = "UPDATE employe SET nom = %s, prenom = %s, salaire = %s, id_service = %s WHERE id = %s"
        values = (nom, prenom, salaire, id_service, id)
        self.cursor.execute(query, values)
        self.cnx.commit()

    def delete(self, id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (id,)
        self.cursor.execute(query, values)
        self.cnx.commit()

cnx = mysql.connector.connect(
    user='root',
    password='noah06600',
    host='localhost'
)

cursor = cnx.cursor()


cursor.execute("CREATE DATABASE IF NOT EXISTS MaBaseDeDonnees")

cursor.execute("USE MaBaseDeDonnees")

cursor.execute("""
    CREATE TABLE employe (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255),
        prenom VARCHAR(255),
        salaire DECIMAL(10, 2),
        id_service INT
    )
""")

cursor.execute("""
    CREATE TABLE service (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255)
    )
""")

employes = [('Jean', 'Dupont', 3500.00, 1), ('Marie', 'Durand', 4500.00, 2)]
services = [('Service 1',), ('Service 2',)]

cursor.executemany("INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)", employes)
cursor.executemany("INSERT INTO service (nom) VALUES (%s)", services)

cnx.commit()

cursor.execute("SELECT * FROM employe WHERE salaire > 3000")
for employe in cursor:
    print(employe)

cursor.execute("""
    SELECT e.nom, e.prenom, s.nom 
    FROM employe e 
    INNER JOIN service s ON e.id_service = s.id
""")
for employe in cursor:
    print(employe)

salarie = Salarie(cnx)
salarie.create('Paul', 'Martin', 4000.00, 1)
print(salarie.read(1))
salarie.update(1, 'Paul', 'Martin', 5000.00, 1)
salarie.delete(1)

cursor.close()
cnx.close()
