"""
EX5: Implementeaza un context manager care va masura si va afisa
durata de executie a codului executat.
"""

import time
#
# class MasoaraTimpul:
#
#     def __enter__(self):
#         self.start_time = time.time()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         end_time = time.time()
#         exec_time = end_time - self.start_time
#         print(exec_time)
#
# with MasoaraTimpul() as timer:
#     n = 0
#     while n <= 1000000:
#         print(n)
#         n += 1
# # Implementati un iterator numit ReverseIterator, care parcurge o colectie in sens opus. Exemplu de folosire:
# Exemplu de folosire:




note = [3, 7, 5, 8, 10]
# my_grades_reversed = ReverseIterator(note)
my_grades_reversed = list(reversed(note))
print(my_grades_reversed)

print(list(my_grades_reversed))
print(next(my_grades_reversed))
print(next(my_grades_reversed))
print(next(my_grades_reversed))
print(next(my_grades_reversed))
print(next(my_grades_reversed))

for nota in my_grades_reversed:
    print(nota)
    print(iter(note))

class User:

    def __init__(self, nume, email, parola, data_nasterii):
        self.nume = nume
        self.email = email
        self.parola = parola
        self.data_nasterii = data_nasterii
        self.logat = False

    def login_required(original_func):
        def wrapper(self, *args, **kwargs):
            if self.logat:
                return original_func(self, *args, **kwargs)
            else:
                print("Trebuie sa fi logat")
        return wrapper

    def login(self, email, parola):
        if email == self.email and parola == self.parola:
            self.logat = True
            print(f"Buna utilizatorule {self.nume} sunteti logat")
        else:
            print("Email / parola gresita!")

    def logout(self):
        self.logat = False
        print("La revedere utilizatorule!")

    @login_required
    def get_info(self):
        if self.logat:
            print(f"Nume: {self.nume}, email: {self.email}, parola: {self.parola}, data nasteri: {self.data_nasterii}")
        else:
            print(f"Nu sunteti logat")


user = User("Dumi", "idk@gmail.com", "nimic", "04.12.1994")

user.get_info()
user.login("idk@gmail.com", "nimic")
user.get_info()
user.logout()
user.get_info()
user.login("idk@gmail.com", "nimic")
user.get_info()
user.logout()
user.login("321321", "321321")
user.get_info()

"""
DECORATORS

4. Implementați următorii decoratori:
timeit – decorator care măsoară timpul de execuție al unei funcții 
logger – decorator care printeaza argumentele de intrare, și rezultatul unei funcții
"""
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