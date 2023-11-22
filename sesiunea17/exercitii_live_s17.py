"""
SESIUNEA 17: Iterators, Generators, Decorators, Context Managers
"""

"""
ITERATORS

1. Implementati un iterator numit ReverseIterator, care parcurge o colectie in sens opus. Exemplu de folosire:

note = [3, 7, 5, 8, 10] 
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
s.a.m.d
"""
# note = [3, 7, 5, 8, 10]
# # rev_it = ReverseIterator(note)
#
# class ReverseIterator:
#
#     def __init__(self, note):
#         self.note = note
#         self.index = len(self.note) - 1
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < 0:
#            raise StopIteration
#         result = self.note[self.index]
#         self.index -= 1
#         return result
#
# note = [3, 7, 5, 8, 10]
# rev_it = ReverseIterator(note)
# print(next(rev_it))  # printeaza 10
# print(next(rev_it))  # printeaza 8
# print(next(rev_it))# printeaza 5
# print(next(rev_it))# printeaza 7
# print(next(rev_it)) # printeaza 3
# print(next(rev_it)) # -->StopIteration
# my_grades_reversed = iter(reversed(note))
#
# print(my_grades_reversed)
#
#
# print(next(my_grades_reversed))
# print(next(my_grades_reversed))
# print(next(my_grades_reversed))
# print(next(my_grades_reversed))
# print(next(my_grades_reversed))
#
# for nota in my_grades_reversed:
#     print(nota)
#     print(iter(note))

"""
GENERATORS

2. Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv)
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
"""
import random

random.randint(1, 49) # se va genera un numar random intre 1 (inclusiv 1) si 10 (inclusiv 10)
# denumire generator: lottery_generator
import random


def generator_loto():

    nr_magic = random.randint(1000000, 9999999)
    for n in range(6):
        n = random.randint(1, 49)
        yield n
    yield nr_magic


loto = generator_loto()
# Var 1
for i in range(7):
    if i < 6:
        print(f'{i+1} Bila cu nr: {next(loto)}')
    else:
        print(f'Numar magic: {next(loto)}')

# Var 2
for i, nr in enumerate(loto, 1):
    if i == 7:
        print(f"Nr magic este : {nr}")
    else:
        print(f"Bila cu nr: {i} este: {nr} ")
# DECORATORS
#
# 3. Implementați o clasă User, cu următoarele cerințe:
# – constructorul va primi ca parametri nume, email, parola, și data nasterii
# - atribute in constructor: nume, email, parola, data_nasterii, este_logat (valoare default False)
# – o metoda login, care va primi email și parola ca parametrii; dacă acestea sunt corecte, userul va fi marcat ca logat
# – o metoda get_info, care va returna toate informațiile despre user DOAR DACĂ acesta este logat,
# folosind un decorator `@login_required`
# – o metoda logout, fara params, care delogheaza userul.
#
# Se va testa apelarea metodei get_info inainte de logare, dupa logare, dupa delogare, și după încă o logare.

# class User:
#
#     def __init__(self, nume, email, parola, data_nasterii):
#         self.nume = nume
#         self.email = email
#         self.parola = parola
#         self.data_nasterii = data_nasterii
#         self.logat = False
#
#
#
#
#
#
#     def login_required(original_func):
#         def wrapper(self, *args, **kwargs):
#             if self.logat:
#                 return original_func(self, *args, **kwargs)
#             else:
#                 print("Trebuie sa fi logat")
#
#         return wrapper
#
#     def login(self, email, parola):
#         if email == self.email and parola == self.parola:
#             self.logat = True
#             print(f"Buna utilizatorule {self.nume} sunteti logat")
#         else:
#             print("Email / parola gresita!")
#
#     def logout(self):
#         self.logat = False
#         print("La revedere utilizatorule!")
#
#     @login_required
#     def get_info(self):
#         if self.logat:
#             print(f"Nume: {self.nume}, email: {self.email}, parola: {self.parola}, data nasterii: {self.data_nasterii}")
#         else:
#             print(f"Nu sunteti logat")
#
#
# user = User("Stefan", "office@gmail.com", "birou07", "03.10.2000")
#
# user.get_info()
# user.login("office@gmail.com", "birou07")
# user.get_info()
# user.logout()
# user.get_info()
# user.login("office@gmail.com", "birou07")
# user.get_info()
# user.logout()
# user.login("office@gmail.com", "birou07")
# user.get_info()







#
#
# DECORATORS
#
# 4. Implementați următorii decoratori:
# timeit – decorator care măsoară timpul de execuție al unei funcții
# logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
# """
import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Timpul de execuție al funcției '{func.__name__}': {execution_time} secunde")
        return result
    return wrapper


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Funcția '{func.__name__}' a primit următoarele argumente:")
        print(f"Argumente poziționale: {args}")
        print(f"Argumente cheie: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Rezultatul funcției '{func.__name__}': {result}")
        return result
    return wrapper


@timeit
def functie_timp():
    time.sleep(2)
    print("Execuție funcție timp")


@logger
def functie_logger(*args, **kwargs):
    my_sum = 0
    for arg in args:
        my_sum += arg
    for value in kwargs.values():
        my_sum += value
    return my_sum


functie_timp()
functie_logger(2, 3, b=2, c=3)