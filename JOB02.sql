
mysql> USE LaPlateforme;
Database changed
mysql> CREATE TABLE etage (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     numero INT,
    ->     superficie INT
    -> );
Query OK, 0 rows affected (0.11 sec)

mysql>
mysql> CREATE TABLE salle (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     id_etage INT,
    ->     capacite INT
    -> );
Query OK, 0 rows affected (0.03 sec)