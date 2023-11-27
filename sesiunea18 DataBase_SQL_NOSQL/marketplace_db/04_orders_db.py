"""

INTERACTIUNEA cu tabelul orders
"""
import sqlite3
connection = sqlite3.connect("pyta11_marketplace.db")

cursor = connection.cursor()
# CREATE ORDER

# CREATE ORDER

"""
- Ne asiguram ca avem o intrare in tabelul users, pentru user-ul
pentru care dorim sa cream comanda
- Cream o intrare in tabelul orders
- Ne asiguram ca avem o intrare in tabelul products, pentru produsul
pe care dorim sa il adaugam in comanda
- Cream cel putin o intrare in tabelul order_items
"""
# comanda va fi facuta de user-ul cu id-ul 2
order_query = """
INSERT INTO orders (customer_id, order_date)
VALUES (2, '27.11.2023')
"""

cursor.execute(order_query)
connection.commit()

# se va comanda produsul cu id-ul 1 (din tabelul products)
# cantitatea comandata va fi 1
order_item_query = """
INSERT INTO order_items (order_id, product_id, total_price)
VALUES (1, 1, 2000)
"""

cursor.execute(order_item_query)
connection.commit()

# READ ORDER
# 1. Citim din baza de date informatiile despre comanda cu id-ul 1
# 2. Afisati adresa de email a utilizatorului care a pus comanda cu id -UL 1
# 3. Citim toate liniile de comanda care apartin de comanda cu id ul 1
# 4. Afisati numele produselor care au fost comandate in comanda cu id -ul 1


# READ ORDER
# 1. Citim din baza de date informatiile despre comanda cu id-ul 1.
cursor.execute(
    """
    SELECT * FROM orders
    WHERE id = 1;
    """
)
orders = cursor.fetchone()
print(orders)
# 2. Afisati adresa de mail a utilizatorului care a pus comanda cu id-ul 1.
cursor.execute(
    """
    SELECT email FROM users
    WHERE id = ?;
    """,
    str(orders[1])
)
email_client = cursor.fetchone()
print(email_client)
# 3. Citim toate liniile de comanda care apartin de comanda cu id-ul 1.
cursor.execute(
    """
    SELECT * FROM order_items
    WHERE id = 1;
    """
)
comenzi = cursor.fetchone()
print(comenzi)
# 4. Afisati numele produselor care au fost comandate in comanda cu id-ul 1.
cursor.execute(
    """
    SELECT name FROM products
    WHERE id = ?;
    """,
    str(comenzi[2])
)
nume_produs = cursor.fetchone()
print(nume_produs)

#UPDATE ORDER
#5. Clientul care a facut comanda cu id-ul 1, doreste sa mai adauge
#in comanda sa (in cosul de cumparaturi) inca un produs (cantitatea = 2).
#Acualieaza comanda corespunzator.

cursor.execute(
    """
    UPDATE order_items SET quantity = 2
    WHERE id = 1;
    """
)
connection.commit()

# DELETE ORDER
#6. Clientul s-a razgandit si doreste sa anuleze comanda.
#Sterge comanda cu id-ul 1 din baza de date.
cursor.execute(
    """
    DELETE FROM orders
    WHERE id = 1;
    """
)
connection.commit()

connection.close()