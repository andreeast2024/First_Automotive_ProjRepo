"""
DESIGN PATTERNS - EXERCITII WORKSHOP - Sesiunea 16
"""

"""
Se da următoarea clasa:
"""


class PresedinteRomania(object):
    __instance = None
    sector = "Politic"
    def __str__(self):

        return "Eu sunt presedintele Romaniei"

    def say_hello(self):
        return f'Salut! {self}'
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

"""
In momentul de fata, dacă încercăm să creăm mai multe obiecte din clasa aceasta, vom putea:
"""

a = PresedinteRomania()
b = PresedinteRomania()
c = PresedinteRomania()
d = PresedinteRomania()
e = PresedinteRomania()
f = PresedinteRomania()
g = PresedinteRomania()
e = PresedinteRomania()
h = PresedinteRomania()
i = PresedinteRomania()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'ID(c) = {id(c)}')
print(f'ID(d) = {id(d)}')
print(f'ID(e) = {id(e)}')
print(f'ID(f) = {id(f)}')
print(f'ID(g) = {id(g)}')
print(f'ID(h) = {id(h)}')
print(f'ID(i) = {id(i)}')
print(f'Acelasi obiect? {a is b and a is c and a is d and a is e and a is f and a is g and a is h and a is i}')

"""
Scopul acestui exercițiu este sa modificăm clasa de mai sus folosind DP Singleton pentru a obține mereu același obiect:
Vom folosi functia `__new__` (adevăratul constructor din Python)
Vom tine singurul obiect pe clasa (cls), și îl vom crea doar la prima apelare a lui __new__
La orice alta apelare, vom returna obiectul deja existent
"""
