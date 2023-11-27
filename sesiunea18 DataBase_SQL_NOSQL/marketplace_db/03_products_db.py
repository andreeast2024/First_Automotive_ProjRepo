"""
INTERACTIUNEA cu tabelul products
"""
import sqlite3
connection = sqlite3.connect("pyta11_marketplace.db")

cursor = connection.cursor()
# # CREATE USER
# # user 1
# # are completate doar campurile obligatorii
cursor.execute(
    """
    INSERT INTO products (name, category, price, stock_count, description)
    VALUES ('laptop', 'devices', '8000','29', '10000');
    """
)
connection.commit()
# user 2
# are completate toate campurile si adaugam valori pentru campuri in mod dinamic
# user_query = """
#     INSERT INTO products (name, category, price, stock_count, description)
#     VALUES (?, ?, ?, ?, ?);
# """
#
# cursor.execute(
#     user_query,
#     ('Iphone 12', 'devices', '4000', '9', 'Apple Smartphone')
# )
# connection.commit()
# adaugarea mai multor inregistrari odata intr-un tabel
# user_query = """
#     INSERT INTO products (name, category, price, stock_count, description)
#     VALUES (?, ?, ?, ?, ?);
# """
users_to_create = [
    ('Iphone 15', 'devices', '8000', '9', 'Apple Smartphone'),
    ('Headset Sony', 'gadgets', '500', '9', 'Sony 2379'),
    ('Mouse Dell', 'gadgets', '200', '9', 'Dell 1179'),
    ('Keyboard HP', 'gadgets', '500', '9', 'Wireless Keyboard 1134')
]
# cursor.executemany(
#     user_query,
#     users_to_create
# )
# connection.commit()


# va trebui sa aveti disponibila conexiunea la baza de date
# si cursorul

# operatiile CRUD

# CREATE product -> TODO: WORKSHOP Sesiunea 18

# READ product

# READ product
# 1. Citeste din baza de date (tabelul products), toate produsele disponibile
# si afiseaza detaliile disponibile pentru fiecare.

cursor.execute(
    """
    SELECT * FROM products;
    """
)


print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchall())
for row in cursor.execute("SELECT * FROM products;"):
     print(row)

# 2. Citeste din baza de date (tabelul products), produsul cu id-ul 2,
# si afiseaza cantitatea in stoc disponibila pentru produsul respectiv.

     cursor.execute(
         """
         SELECT * FROM products
         WHERE id = 2;
         """

     )
     print(cursor.fetchone())
     print(cursor.fetchone())
# UPDATE product
# 3. Sa presupunem ca s-a vandut o bucata din produsul cu id-ul 2.
# Actualizeaza cantitatea din stoc pentru acesta.
cursor.execute(
    """
    SELECT stock_count FROM products
    WHERE id = 2;
    """
)
stock = cursor.fetchone()[0]
print(stock)
stock_update = stock - 1


cursor.execute(
    """
    
    UPDATE products SET stock_count = ?
    WHERE id = 2;
    """,
    (stock_update,)
)
connection.commit()
cursor.execute(
    """
    SELECT stock_count FROM products
    WHERE id = 2;
    """
)
stock = cursor.fetchone()[0]
print(stock)

# DELETE product
# 4. Nu mai colaboram cu furnizorul care ne livra produsul cu id-ul 1.
# Sterge-l din baza de date
# UPDATE product

# DELETE product
cursor.execute(
    """
    DELETE FROM products
    WHERE id = 1;
    """
)

connection.commit()
connection.close()