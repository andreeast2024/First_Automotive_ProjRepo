"""
INTERACTIUNEA CU tabelul users
"""
import sqlite3
connection = sqlite3.connect("pyta11_marketplace.db")

cursor = connection.cursor()
# CREATE USER

# user 1
# are completate doar campurile obligatorii
cursor.execute(
    """
    INSERT INTO users (username, email, password, first_name, last_name)
    VALUES ('stefana', 'andreeaa@yahoo.ro', '123', 'Andreea', 'Saper');
    """
)
connection.commit()

# user 2
# are completate toate campurile si adaugam valori pentru campuri in mod dinamic
user_query = """
    INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

cursor.execute(
    user_query,
    ('alinapopa', 'alina@gmail.com', '456', 'Alina', 'Popa', 'strada Ion Rus 25', 'Simeria', '334568', 'RO')
)
connection.commit()

# adaugarea mai multor inregistrari odata intr-un tabel
user_query = """
    INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""
users_to_create = [
    ('paulamarc', 'paula@yahoo.com', 'abc', 'Paula', 'Marc', 'str. 1 mai, bloc 23, ap 11',
     'Hateg', '253410', 'RO'),
    ('bobdavid', 'david@gmail.com', '111', 'David', 'Bob', 'str. trandafirilor 230', 'Cluj-Napoca', '407234', 'RO')
]
cursor.executemany(
    user_query,
    users_to_create
)
connection.commit()
