"""
Join-uri:
 Join-urile sunt comenzi SQL prin care putem combina date din doua sau mai multe tabele pe baza coloanei de legatura(coloana foreign key)

Tipuri de JOIN-uri:
1. INNER JOIN
-obtinem inregistrari care fac match la valori din ambele tabele
2. LEFT (OUTER) JOIN
-obtinem toate inregistrarile din tabelul din stanga +inregistrarile care fac match din tabelul din dreapta
3.RIGHT (OUTER) JOIN
-obtinem toate inregistrarile din tabelul din dreapta +inregistrarile care fac match din tabelul din stanga
4.FULL (OUTER) JOIN
- se returneaza toate inregistrarile din ambele atunci cand se face match fie in tabelul din stanga fie in tabelul din dreapta

"""
import sqlite3
connection = sqlite3.connect("pyta11_marketplace.db")

cursor = connection.cursor()
#exemplu de inner join
#selectam id-ul comenzii facand un inner join intre tabelele orders si user
# query = """
# SELECT orders.id, users.username
# FROM orders
# INNER JOIN users ON orders.customer_id == users.id
#
# """
#
# cursor.execute(query)
#
# print(cursor.fetchall())
#exemplu de left join

# returnam toti userii +id ul comenzii asociate indiferent daca au sau nu match la vreo comanda
query = """
SELECT users.username, orders.id
FROM users
LEFT JOIN orders ON users.id == orders.customer_id
"""
cursor.execute(query)
print(cursor.fetchall())

connection.close()


