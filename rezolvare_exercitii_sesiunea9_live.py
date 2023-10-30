"""
REZOLVARE EXERCITII FUNCTII
"""

"""
IMPORTANT! Pentru toate exercitiile: apelati functia de cel putin 2 ori
cu valori diferite pentru a testa.
Daca functia are return, printeaza raspunsul.                        
"""


"""
1 Functie care returneaza aria dreptunghiului.
"""


# definim o functie numita arie_dreptunghi, care ia doi parametri
# lungime si latime
def arie_dreptunghi(lungime, latime):
    # functia returneaza produsul dintre lungime si latime (aria dreptunghiului)
    return lungime * latime


# invocam/apelam functia arie_dreptunghi, cu argumentele 2 si 5
# adica dam valori pentru parametri lungime si latime
# si printam direct rezultatul functiei apelate.
# lungime va lua valoarea 2
# latime va lua valoarea 5
print(arie_dreptunghi(2, 5))


# invocam/apelam functia arie_dreptunghi, cu argumentele 10 si 15
# adica dam valori pentru parametri lungime si latime
# si printam direct rezultatul functiei apelate.
# lungime va lua valoarea 10
# latime va lua valoarea 15
print(arie_dreptunghi(10, 15))

"""
2. Functie care returneaza aria cercului
"""


# arie cerc = pi * raza la patrat

# Pentru a avea acces la constanta PI, ne putem
# folosi de modulul math, disponibil in Python

# DOCUMENTATIE modul math: https://docs.python.org/3/library/math.html

# Acest modul face parte din Standard Python Library
# ceea ce inseamna ca nu trebuie instalat ci este gata oricand
# de folosire.

# Pentru a putea sa il folosim, va trebui sa il importam
# folosind cuvantul cheie import
import math


# definim o functie numita arie_cerc, care va lua un parametru, reprezentand raza
# cercului a carui arie dorim sa o calculam
def arie_cerc(raza):
    # returnam aria cercului
    return math.pi * raza ** 2


# apelam/invocam functia arie_cerc, cu argumentul 2,
# adica dam valoare pentru parametrul raza, si printam direct rezultatul.
# parametrul raza va avea valoarea 2
print(arie_cerc(2))


# apelam/invocam functia arie_cerc, cu argumentul 2,
# adica dam valoare pentru parametrul raza, si printam direct rezultatul.
# parametrul raza va avea valoarea 4
print(arie_cerc(4))

"""
3. Functie care returneaza True daca un caracter x se gaseste intr-un string dat
si False daca nu se gaseste.
"""


# definim o functie, numita is_char_in_str, care ia doi parametri,
# char si text, char reprezentand caracterul pe care dorim sa il cautam,
# iar text reprezentand stringul in care dorim sa cautam caracterul.
def is_char_in_str(char, text):
    # pentru a verifica daca un caracter este intr-un string,
    # ne putem folosi de operatorul "in"
    if char in text:
        return True
    return False


# apelam/invocam functia is_char_in_str, cu argumentele "a" si "abc"
# si printam direct rezultatul acesteia.
# parametrul char va lua valoarea "a"
# parametrul text va lua valoarea "abc"
print(is_char_in_str("a", "abc"))


# apelam/invocam functia is_char_in_str, cu argumentele "z" si "abc"
# si printam direct rezultatul acesteia.
# parametrul char va lua valoarea "z"
# parametrul text va lua valoarea "abc"
print(is_char_in_str("z", "abc"))

"""
4. Functie fara return, primeste un string si printeaza pe ecran:
Numarul de caractere lower case este x
Numarul de caractere upper case este y 
"""


# definim o functie numita count_chrs_types, care ia un parametru
# numit text
def count_chrs_types(text):
    # definim o variabila locala, numita lower_count (disponibila doar in interiorul
    # acestei functii) pentru a o folosi sa putem sa numaram
    # caracterele scrise cu litera mica
    lower_count = 0

    # definim o variabila locala, numita upper_count (disponibila doar in interiorul
    # acestei functii) pentru a o folosi sa putem sa numaram
    # caracterele scrise cu litera mare
    upper_count = 0

    # parcurgem stringul text, folosind ciclul repetitic for
    # astfel incat la fiecare iteratie sa avem acces la cate un caracter
    # din string-ul text
    # aceste caractere, vor fi disponibile, in interiorul for-ului in variabila char
    for char in text:
        # pentru a verifica daca un caracter este scris cu litera mica
        # ne putem folosi de metoda ajutatoare de pe string-uri
        # numita islower()
        # aceasta metoda ne va returna True, daca caracterul e scris cu litera mica
        # respectiv False, daca caracterul nu e scris cu litera mica
        if char.islower():
            # daca caracterul e scris cu litera mica,
            # crestem valoarea variabilei lower_count cu 1
            lower_count += 1
        else:
            # altfel, crestem valoarea variabilei upper_count cu 1
            upper_count += 1

    # conform enuntului, aceasta functie nu trebuie sa returneze nimic
    # ci trebuie sa afiseze numarul de caractere mici si mari
    print(f"Numarul de caractere lower case este {lower_count}")
    print(f"Numarul de caractere upper case este {upper_count}")


# apelam/invocam functia count_chrs_types cu argumentul "aAbBcd".
# de data aceasta, nu va trebui sa printam rezultatul acestei functii,
# deoarece ea nu returneaza nimic. Noi doar o apelam, deci activam codul
# din interiorul ei, si astfel, se vor afisa mesajele corespunzatoare.
count_chrs_types("aAbBcd")


# apelam/invocam functia count_chrs_types cu argumentul "aaaa".
# de data aceasta, nu va trebui sa printam rezultatul acestei functii,
# deoarece ea nu returneaza nimic. Noi doar o apelam, deci activam codul
# din interiorul ei, si astfel, se vor afisa mesajele corespunzatoare.
count_chrs_types("aaaa")

"""
5. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.
"""


# definim o functie, numita get_positive_numbers care primeste
# un parametru numic numbers
def get_positive_numbers(numbers):
    # conform enuntului, va trebui sa salvam si sa returnam
    # o lista care va contine doar numerele pozitive din
    # lista luata ca si parametru (numbers)
    # astfel, va trebui sa definim o lista goala,
    # pe care sa o populam mai apoi cu numerele positive
    positive_numbers = []

    # accesam fiecare numar din lista/parametrul numbers
    for number in numbers:
        # verificam daca number este pozitiv
        if number > 0:
            # daca da, il adaugam in lista positive_numbers
            positive_numbers.append(number)
    # dupa ce am adaugat TOATE numerele pozitive din lista numbers
    # in lista noasta noua, positive_numbers, o returnam
    return positive_numbers


# apelam/invocam functia get_positive_numbers cu argumentul [1, 2, 3]
# acest argument reprezinta valoarea pentru parametrul numbers
# vom printa direct rezultatul acestei functii apelate.
print(get_positive_numbers([1, 2, 3]))


# apelam/invocam functia get_positive_numbers cu argumentul [-1, -2, 3, 4]
# acest argument reprezinta valoarea pentru parametrul numbers
# vom printa direct rezultatul acestei functii apelate.
print(get_positive_numbers([-1, -2, 3, 4]))

"""
6. Functie care nu returneaza nimic. Primeste doua numere si PRINTEAZA
Primul numar x este mai mare decat al doilea numar y
Al doilea numar y este mai mare decat primul numar x
Numerele sunt egale. 
"""


# definim o functie numita compare_numbers, care ia doi parametri, x si y
def compare_numbers(x, y):
    # comparam cei doi parametri x si y, si in functie de rezultat,
    # printam un mesaj sugestiv
    if x > y:
        print(f"Primul numar x {x} este mai mare decat al doilea numar y {y}")
    elif x < y:
        print(f"Al doilea numar y {y} este mai mare decat primul numar x {x}")
    else:
        print(f"Numerele sunt egale")


# apelam/invocam functia compare_numbers cu argumentele 2 si 1
# 2 se va asigna/va fi valoarea pentru parametrul x
# 1 se va asigna/va fi valoarea pentru parametrul y
compare_numbers(2, 1)


# apelam/invocam functia compare_numbers cu argumentele 1 si 2
# 1 se va asigna/va fi valoarea pentru parametrul x
# 2 se va asigna/va fi valoarea pentru parametrul y
compare_numbers(1, 2)


# apelam/invocam functia compare_numbers cu argumentele 2 si 2
# 2 se va asigna/va fi valoarea pentru parametrul x
# 2 se va asigna/va fi valoarea pentru parametrul y
compare_numbers(2, 2)

"""
7. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Printeaza ‘nu am adaugat numarul in set. Acesta există deja’ + returneaza False
"""


# definim o functie, numita update_set, care primeste
# doi parametri, number si numbers_set
def update_set(number, numbers_set):
    # verificam daca number exista in set, folosind operatorul "in"
    if number in numbers_set:
        # daca number este deja in numbers_set
        # afisam un mesaj sugestiv si returnam False
        print("Nu am adaugat numarul in set. Acesta exista deja")
        return False
    # daca number nu este in set
    # il adaugam folosind metoda ajutatoare de pe set, numita add
    # si returnam True
    numbers_set.add(number)
    return True


# apelam/invocam functia update_set cu argumentele 2 si {1, 3, 4}
# 2 va fi valoarea pentru parametrul number
# {1, 3, 4} va fi valoarea pentru parametrul numbers_set
# printam direct rezultatul acestei functii apelate
print(update_set(2, {1, 3, 4}))


# apelam/invocam functia update_set cu argumentele 2 si {1, 2, 3, 4}
# 2 va fi valoarea pentru parametrul number
# {1, 2, 3, 4} va fi valoarea pentru parametrul numbers_set
# # printam direct rezultatul acestei functii apelate
# print(update_set(2, {1, 2, 3, 4}))

"""
8. Functie care primeste o luna din an si returneaza cate zile are acea luna.
"""
# pentru a vedea cate zile sunt intr-o luna,
# ne putem folosi de un modul din Python Standard Library, numit calendar


# DOCUMENTATIE: https://docs.python.org/3/library/calendar.html

# Va trebui sa importam functia pe care dorim sa o folosim
from calendar import monthrange


# definim o functie numita luna_anului, care ia un parametru numit luna
def luna_anului(luna):
    # apelam functia monthrange, dand valoare pentru cei doi parametri pe care
    # aceasta ii ia si salvam rezultatul sau intr-o variabila, numita rezultat.

    # daca ne uitam in documentatie, sau daca dam click pe metoda monthrange in Pycharm + CTRL
    # vom vedea definitia functiei si ce returneaza ea de fapt.
    # astfel, ne vom da seama ca returneaza un tuplu, in care:
    # - prima valoare reprezinta ziua din saptamana in care pica prima zi din luna data ca parametru
    # - a doua valoare reprezinta numarul de zile din luna daca ca parametru
    rezultat = monthrange(2023, luna)
    print(rezultat)
    return rezultat[1]


print(luna_anului(10))


# def zile_luna(luna):
#     luni = {
#         'ianuarie': 31,
#         'februarie': 28,  # 29 în an bisect
#         'martie': 31,
#         'aprilie': 30,
#         'mai': 31,
#         'iunie': 30,
#         'iulie': 31,
#         'august': 31,
#         'septembrie': 30,
#         'octombrie': 31,
#         'noiembrie': 30,
#         'decembrie': 31
#     }
#     luna = luna.lower()
#
#     if luna in luni:
#         return luni[luna]
#     else:
#         return "Luna introdusă nu este validă."
#
#
# luna_dorita = 'ianuarie'
# numar_zile = zile_luna(luna_dorita)
# if numar_zile != "Luna introdusa nu este valida.":
#     print(f"Luna {luna_dorita.capitalize()} are {numar_zile} zile.")
# else:
#     print(numar_zile)


"""
9. Functie calculator care sa returneze 4 valori: Suma, diferenta, inmulțirea, impartirea a doua numere.

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""


# definim o functie calculator, care ia doi parametri: a si b
def calculator(a, b):
    # calculam suma dintre parametri a si b
    # si o salvam intr-o variabila, numita suma
    suma = a + b

    # calculam diferenta dintre parametri a si b
    # si o salvam intr-o variabila, numita diff
    diff = a - b

    # calculam produsul dintre parametri a si b
    # si il salvam intr-o variabila, numita multiplication
    multiplication = a * b

    # cand vine vorba de impartire, trebuie sa fim atenti,
    # ca divizorul sa nu fie 0, deoarce impartirea la 0
    # nu este posibila
    # astfel avem nevoie de o verificare, si folosim un if
    if b != 0:
        division = a / b
    else:
        division = 0

    # returnam rezultatul tuturor calculelor deodata,
    # sub forma unui tuplu
    return suma, diff, multiplication, division


print(calculator(10, 2))
print(type(calculator(10, 2)))

"""
10. Functie care primeste o lista de cifre (adica doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

# definim o functie, numita count_numbers, care ia un singur parametru,
# numit numbers
def count_numbers(numbers):
    # definim un dictionar in care vom
    # salva recurentele tuturor cifrelor,
    # astfel vom avea o cheie reprezentata
    # de fiecare cifra (0-9) si ca valoare initiala
    # vom pune 0, pentru fiecare cifra
    my_dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        9: 0
    }

    # parcurgem lista de numere
    for number in numbers:
        # crestem recurenta pentru fiecare cifra in dictionar
        my_dict[number] += 1
    # returnam dictionarul
    return my_dict


print(count_numbers([1, 1, 2, 3, 0, 0, 0, 4, 5]))


"""
11. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
"""


def get_max(a, b, c):
    numbers = [a, b, c]
    return max(numbers)


print(get_max(1, 2, 3))
print(get_max(5, 200, -300))

"""
12. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: dacă dam numarul 3, suma va fi 6 (0+1+2+3)
"""

def get_sum(a):
    result = 0
    for i in range(0, a + 1):
        result += i

    return result


print(get_sum(3))
print(get_sum(2))
print(get_sum(5))


"""
13. Functie care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
"""


def get_common_numbers(list1, list2):
    # cele doua liste luate ca parametri pot contine
    # elemente duplicate

    # noi dorim sa returnam numerele comune, iar in cazul
    # in care avem numere duplicate, nu dorim sa le luam
    # in considerare de mai multe ori
    # astfel, putem converti listele la set-uri (set-urile
    # fiind acele structuri de date care nu permit valori duplicate)
    set1 = set(list1)
    set2 = set(list2)

    return set1.intersection(set2)


print(get_common_numbers([1, 1, 2, 3], [2, 2, 3, 4]))

"""
14. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90 de lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.
"""


def apply_discount(price, discount):
    if 0 < discount <= 100:
        return price - price * discount / 100
    else:
        return 0

print(apply_discount(100,10))
"""
15. Funcție care sa afiseze data si ora curenta din Romania.
(bonus: afiseaza si data si ora curenta din China)
"""

# libraria pytz este o librarie din Standard Python Library
# care ne permite sa lucram cu diferite timezone-uri
import pytz

# libraria datetime este o librartie din Standard Python Library
# care ne permite sa lucram cu obiecte data/ora.
# Practic putem obtine ora curenta, putem face operatii
# intre diferite dati din calendar etc
import datetime


def get_current_datetime(timezone):

    # ne folosim de functia timezone din libraria pytz
    # pentru a lua timezone-ul specific unei anumite zone
    # luata ca si parametru (timezone-ul dintre paranteze)
    tz = pytz.timezone(timezone)

    # parametru de mai sus, timezone, este un string, si reprezinta
    # regiunea pentru care dorim sa obtinem timezone-ul.
    # pentru a vedea ce string-uri putem da ca parametru pentru a afla
    # timezone-ul aferent, putem printa pytz.all_timezones si sa gasim
    # cel pe care il dorim
    # print(pytz.all_timezones)

    # pentru a lua data si ora curenta, ne folosim de functia now()
    # care (optional) la timezone-ul pentru regiunea din care dorim sa afisam
    # ora curenta
    current_datetime = datetime.datetime.now(tz)
    print(current_datetime)


# print(pytz.all_timezones)
get_current_datetime('Europe/Bucharest')
get_current_datetime('Asia/Shanghai')

"""
16. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la Craciun
daca nu vrei sa ne zici cand e ziua ta :)
"""

import datetime


def countdown(day, month, year):

    data_curenta = datetime.date.today()
    data_dorita = datetime.date(year, month, day)
    if year < data_curenta.year:
        data_dorita = datetime.date(data_curenta.year, month, day)
    zile_ramase = (data_dorita - data_curenta).days
    print(f'Mai sunt {zile_ramase} zile pana la eveniment!')


countdown(25, 12, 2023)
countdown(29, 6, 1996)
