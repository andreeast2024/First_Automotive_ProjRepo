"""
INTERACTIUNEA CU tabelul users
"""
import sqlite3
connection = sqlite3.connect("pyta11_marketplace.db")

cursor = connection.cursor()
# CREATE USER

# user 1
# are completate doar campurile obligatorii
# cursor.execute(
#     """
#     INSERT INTO users (username, email, password, first_name, last_name)
#     VALUES ('stefana', 'andreeaa@yahoo.ro', '123', 'Andreea', 'Saper');
#     """
# )
# connection.commit()

# user 2
# are completate toate campurile si adaugam valori pentru campuri in mod dinamic
# user_query = """
#     INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
# """
#
# cursor.execute(
#     user_query,
#     ('alinapopa', 'alina@gmail.com', '456', 'Alina', 'Popa', 'strada Ion Rus 25', 'Simeria', '334568', 'RO')
# )
# connection.commit()

# adaugarea mai multor inregistrari odata intr-un tabel
# user_query = """
#     INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
# """
# users_to_create = [
#     ('paulamarc', 'paula@yahoo.com', 'abc', 'Paula', 'Marc', 'str. 1 mai, bloc 23, ap 11',
#      'Hateg', '253410', 'RO'),
#     ('bobdavid', 'david@gmail.com', '111', 'David', 'Bob', 'str. trandafirilor 230', 'Cluj-Napoca', '407234', 'RO')
# ]
# cursor.executemany(
#     user_query,
#     users_to_create
# )
# connection.commit()
# CREATE product -> TODO: WORKSHOP Sesiunea 18

# READ product
cursor.execute(
    """
    SELECT * FROM users;
    """
)

#putem folosi metoda fetchone() disponibile pe cursor
print(cursor.fetchone())# prima intrare(sub forma de tuplu)
print(cursor.fetchone())# a 2 a intrare(sub forma de tuplu)
print(cursor.fetchall())#obtinem toate intrarile citite din tabel, sub forma de lista cu tupluri
# for row in cursor.execute("SELECT * FROM users;"):
#     print(row)
#     print(row[2])# accesam emailul

# READ USER by ID
cursor.execute(
    """
    SELECT * FROM users
    WHERE id = 1;
    """

)
print(cursor.fetchone())# prima intrare(sub forma de tuplu)
print(cursor.fetchone())# a 2 a intrare(sub forma de tuplu)

# READ USER BY USERNAME
# cursor.execute(
#     """
#     SELECT email FROM users
#     WHERE username = 'stefana';
#     """
#
# )
# user = cursor.fetchone()
# print(user)
# #definire tuplu cu un singur element
# my_tuple = (1)
# print(my_tuple)
# print(type(my_tuple))
# my_tuple = (1,)
# print(my_tuple)
# print(type(my_tuple)
# # UPDATE product
# UPDATE USER
# cursor.execute(
#     """
#     UPDATE users SET username='cstefan', email='aaa@gmail.com'
#     WHERE id = 1;
#     """
# )
# connection.commit()

#DELETE USER
cursor.execute(
    """
    DELETE FROM users
    WHERE id = 4;
    """
)
connection.commit()
connection.close()