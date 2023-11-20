"""
Iteratori, generatori, context managers, decoratori
EXERCITII WORKSHOP - Sesiunea 16
"""



"""
1. Creeaza urmatoarele variabile: o lista, o tupla, un string.
Itereaza prin fiecare dintre ele, prima data folosind o bucla for,
iar apoi folosind un iterator (ne vom folosi de metodele iter si next):

my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(f'Primul element: {next(my_iterator)}')
print(f'Al doilea element: {next(my_iterator)}')
print(f'Al treilea element: {next(my_iterator)}')
print(f'Aici va da eroare: {next(my_iterator)}')
"""
#a.
my_list = [1, 2, 3]
for i in my_list:
    print(i)
my_list_iter = iter(my_list)
print(f"Primul element: {next(my_list_iter)}")
print(f"Al 2-lea element: {next(my_list_iter)}")
print(f"Al 3-lea element: {next(my_list_iter)}")

# b.
my_tuple = (1, 2, 3)
for i in my_tuple:
    print(i)
my_tuple_iter = iter(my_tuple)
print(f"Primul element: {next(my_tuple_iter)}")
print(f"Al 2-lea element: {next(my_tuple_iter)}")
print(f"Al 3-lea element: {next(my_tuple_iter)}")

# c.
my_string = 1, 2, 3
for i in my_string:
    print(i)
my_string_iter = iter(my_string)
print(f"Primul element: {next(my_string_iter)}")
print(f"Al 2-lea element: {next(my_string_iter)}")
print(f"Al 3-lea element: {next(my_string_iter)}")
"""

#
# ""
# 2. Atunci cand nu mai contine elemente, un iterator va arunca o exceptie
# de tipul StopIteration.
# Foloseste un bloc try-except pe codul de mai sus pentru a gestiona aceasta exceptie
# si pentru a te asigura ca programul tau ajunge la final cu un exit code de succes (adica 0).
# """
# a. lista
my_list = [1, 2, 3]
for i in my_list:
    print(i)
my_list_iter = iter(my_list)
print(f"Primul element: {next(my_list_iter)}")
print(f"Al 2-lea element: {next(my_list_iter)}")
print(f"Al 3-lea element: {next(my_list_iter)}")

# b.
my_tuple = (1, 2, 3)
for i in my_tuple:
    print(i)
my_tuple_iter = iter(my_tuple)
print(f"Primul element: {next(my_tuple_iter)}")
print(f"Al 2-lea element: {next(my_tuple_iter)}")
print(f"Al 3-lea element: {next(my_tuple_iter)}")

# c.
my_string = 1, 2, 3
for i in my_string:
    print(i)
my_string_iter = iter(my_string)
print(f"Primul element: {next(my_string_iter)}")
print(f"Al 2-lea element: {next(my_string_iter)}")
print(f"Al 3-lea element: {next(my_string_iter)}")
"""
2. Atunci cand nu mai contine elemente, un iterator va arunca o exceptie
de tipul StopIteration.
Foloseste un bloc try-except pe codul de mai sus pentru a gestiona aceasta exceptie
si pentru a te asigura ca programul tau ajunge la final cu un exit code de succes (adica 0).
"""
my_list = [1, 2, 3]
my_list_iter = iter(my_list)
try:
    print(f"Primul element: {next(my_list_iter)}")
    print(f"Al 2-lea element: {next(my_list_iter)}")
    print(f"Al 3-lea element: {next(my_list_iter)}")
    print(f"Al 3-lea element: {next(my_list_iter)}")
except StopIteration:
    print("Ai ajuns la limita maxima de iterare")

"""
3. Declara un string care contine toate literele alfabetului.
Folosind functia enumerate, care primeste ca si parametru o colectie
(lista, tupla, string) si returneaza un iterator,
 afiseaza pentru fiecare litera in parte:
`Pe mine ma cheama X si sunt a n-a litera din alfabet`
Nu uite sa gestionezi cazurile speciale (prima litera, etc)

Useful resource: https://www.geeksforgeeks.org/enumerate-in-python/
"""
#
# import string
#
# my_string = string.ascii_uppercase
# my_number = string.ascii_letters
#
# my_string_enum = enumerate(iter(my_string))
# my_number_enum = enumerate(iter(my_number), 1)
# # Var 1.
# try:
#     print(f"Pe mine ma cheama {next(my_string_enum)[1]} si sunt a {next(my_number_enum)[0]} litera din alfabet")
#     print(f"Pe mine ma cheama {next(my_string_enum)[1]} si sunt a {next(my_number_enum)[0]} litera din alfabet")
#     print(f"Pe mine ma cheama {next(my_string_enum)[1]} si sunt a {next(my_number_enum)[0]} litera din alfabet")
#     print(f"Pe mine ma cheama {next(my_string_enum)[1]} si sunt a {next(my_number_enum)[0]} litera din alfabet")
#     print(f"Pe mine ma cheama {next(my_string_enum)[1]} si sunt a {next(my_number_enum)[0]} litera din alfabet")
# except StopIteration:
#     print("Ai ajuns la final")
#
# # Var 2.
# while True:
#     try:
#         print(f"Pe mine ma cheama {next(my_string_enum)[1]} si sunt a {next(my_number_enum)[0]} litera din alfabet")
#     except StopIteration:
#         break
# """


#
# """
# #4. Declara trei liste: una cu oameni, una cu salarii, si una cu meserii
# # (important: trebuie sa aiba acelasi numar de elemente).
# # Apoi foloseste functia zip, care primeste ca si parametru un numar de colectii
# # si returneaza un iterator pentru a afisa:
# # `Pe mine ma cheama X, sunt de profesie Y, si castig Z ron pe luna`
#
# Useful resource: https://www.w3schools.com/python/ref_func_zip.asp
# """
lista_oameni = ["Andreea", "Calina", "Iosefina"]
lista_meserii = ["Inginer", "Antreprenor", "Tehnician dentar"]
lista_salarii = [8000, 10000, 6000]

lista_oameni_iter = iter(lista_oameni)
lista_meserii_iter = iter(lista_meserii)
lista_salarii_iter = iter(lista_salarii)

colectie = zip(lista_oameni_iter, lista_meserii_iter, lista_salari_iter)

# Var 1.
for oameni, meserii, salarii in colectie:
    print(f"Pe mine ma cheama {oameni}, sunt de profesie {meserii} si castig {salarii}")

# Var 2.
while True:
    try:
        nume, meserie, salariu = next(colectie)
        print(f"Pe mine ma cheama {nume}, sunt de profesie {meserie}, și câștig {salariu} lei pe lună.")
    except StopIteration:
        break
        



# Python program to illustrate ascii()
test_str = "G ë ê k s f ? r G ? e k s"
print(ascii(test_str))
