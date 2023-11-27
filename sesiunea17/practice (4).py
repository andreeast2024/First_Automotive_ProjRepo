# DECORATORI

# def new_decorator(original_func):
#     def wrapper_func():
#         print("Niste cod inaintea apelului original_func")
#         original_func()
#         print("Niste cod dupa apelul original_func")
#
#     return wrapper_func


# @new_decorator
# def func_needs_decoration():
#     print("Vreau sa fiu decorata")
#
#
# @new_decorator
# def hello():
#     print("Hello Pythonistas!")
#
#
# @new_decorator
# def greet():
#     print("Greetings to you")
#
#
# func_needs_decoration()
# hello()
# greet()


# Daca aplicam decoratorul pe functia de mai jos, va functiona?

# def new_decorator(original_func):
#     def wrapper_func(name):
#         print("Niste cod inaintea apelului original_func")
#         original_func(name)
#         print("Niste cod dupa apelul original_func")
#
#     return wrapper_func
#
# @new_decorator
# def salut(name):
#     print(f"Salut, {name}")
#
# salut("Cosmina")
#
# @new_decorator
# def func_needs_decoration():
#     print("Vreau sa fiu decorata")
#
# func_needs_decoration()


def new_decorator(original_func):
    def wrapper_func(*args, **kwargs):
        print("Niste cod inaintea apelului original_func")
        original_func(*args, **kwargs)
        print("Niste cod dupa apelul original_func")

    return wrapper_func

@new_decorator
def salut(name):
    print(f"Salut, {name}")


salut("Cosmina")


@new_decorator
def func_needs_decoration():
    print("Vreau sa fiu decorata")


func_needs_decoration()


@new_decorator
def suma(a, b, c):
    my_sum = a + b + c
    print(my_sum)

suma(1, 2, 3)


# *args ca parametru la o functie -> indica ca acea functie
# poate sa fie apelata cu oricate argumente pozitionale.

def suma(*args):
    print(args)

suma() # args e un tuplu gol
suma(1) # args e un tuplu cu un singur element
suma(1, 2)
suma(1, 2, 3)
suma(1, 2, 3, 4)

# **kwargs ca parametru la o functie -> indica ca acea functie
# poate sa fie apelata cu oricate named arguments

def suma(**kwargs):
    print(kwargs)

# suma(1, 2, 3, 4)
suma(a=1, b=2, c=3, d=4)


def suma(*args, **kwargs):
    my_sum = 0
    for arg in args:
        my_sum += arg
    # sum(args)

    for value in kwargs.values():
        my_sum += value

    return my_sum


print(suma(1, 2, x=3, y=4))
print(suma(1, 2))
print(suma(a=1, b=2))

"""
GENERATORS

2. Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv)
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
"""

import random

random.randint(1, 49)

def generator_loto():
    nr_magic = random.randint(1000000, 9999999)
    for n in range(6):
        n = random.randint(1, 49)
        yield n
    yield nr_magic

loto = generator_loto()
for i in range(7):
    if i < 6:
        print(f'{i+1} Bila cu nr: {next(loto)}')
    else:
        print(f'Numar magic: {next(loto)}')



