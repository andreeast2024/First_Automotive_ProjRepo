"""
EXERCITII FUNCTII
"""

"""
IMPORTANT! Pentru toate exercitiile: apelati functia de cel putin 2 ori
cu valori diferite pentru a testa.
Daca functia are return, printeaza raspunsul.                        
"""


"""
1. Functie care returneaza aria dreptunghiului
"""
def arie_dreptunghi(lungime, latime):
    aria = lungime * latime
    return aria
dreptunghi1 = arie_dreptunghi(5, 7)
print(dreptunghi1)

dreptunghi2 = arie_dreptunghi(8, 4)
print(dreptunghi2)
"""
2. Functie care returneaza aria cercului
"""
import math  # Importăm modulul math pentru a folosi constanta π

print(math.pi)
def aria_cercului(r):
    if r < 0 :
        return "Raza nu poate fi negativa "
    return math.pi * r**2
rezultat = aria_cercului(4)
print(rezultat)

"""
3. Functie care returneaza True daca un caracter x se gaseste intr-un string dat
si False daca nu se gaseste.
"""
# def gaseste_caracter(caracter,sir):)
# return caracter in sir
# def gaseste_caracter (caracter, sir):
#     if caracter in sir:
#         return True
#     return False
#
# s = 'abc'
# x = 'a'
#
# rezultat = gaseste_caracter(x,s)
# print(rezultat)
# print(gaseste_caracter('a','bcd'))

"""
4. Functie fara return, primeste un string si printeaza pe ecran:
Numarul de caractere lower case este x
Numarul de caractere upper case este y 
"""
def count_lower_and_upper(text):
    count_lower = 0
    count_upper = 0
    for char in text:
        if char.islower():
            count_lower +=1
        else:
            count_upper +=1
    print(f'Nr de caractere cu litere mici {count_lower} si litere mari {count_upper}')

count_lower_and_upper('DSAdsaa')

"""
5. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.
"""
# def get_positive_numbers(lista):
#     lista_nr_pozitive = []
#     for numar in lista:
#
#         if numar > 0:
#             lista_nr_pozitive.append(numar)
#
#     return lista_nr_pozitive
# print(get_positive_numbers([-1,7,-6,9]))"""

"""
6. Functie care nu returneaza nimic. Primeste doua numere si PRINTEAZA
Primul numar x este mai mare decat al doilea numar y
Al doilea numar y este mai mare decat primul numar x
Numerele sunt egale. 
"""
def comparare(x, y):
    if x > y:
        print(f'{x} este mai mare decat {y}')
    elif y > x:
        print(f'{y} este mai mare decat {x}')
    else:
        print(f' {y} este egal cu {x}')

comparare( 5 , 5)

"""
7. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Printeaza ‘nu am adaugat numarul in set. Acesta există deja’ + returneaza False
"""
numar = 3
numere = {1,2,5,8}
def add_number_to_set(numar, numere):
    if numar not in numere:
        numere.add(numar)
        print("Am adaugat acest numar")
        print(numere)
        return True
    else:
        print('Acest numar exista deja')
        return False
print(add_number_to_set(3,{1,2,5,8}))
print(add_number_to_set(2,{1,2,5,8}))
"""
8. Functie care primeste o luna din an si returneaza cate zile are acea luna.
"""
# from calendar import monthrange
#
# def luna_anului(luna):
#     rezultat = monthrange(2023, luna)
#     print(rezultat)
#     return rezultat[1]

# print(luna_anului(7))
from calendar import monthrange
import calendar

def luna_anului(luna):
    rezultat = calendar.monthrange(2023, luna)
    print(rezultat)
    return rezultat[1]

print(luna_anului(10))

"""
9. Functie calculator care sa returneze 4 valori: Suma, diferenta, inmulțirea, impartirea a doua numere.

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""

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
def numere(lista):
    my_dict ={}
    for cifra in lista:
        if cifra in my_dict:
            my_dict[cifra] += 1
        else:
            my_dict[cifra] = 1
    for cifra in range(10):
        if cifra not in my_dict:
            my_dict[cifra] = 0
    return my_dict
nume_lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
my_dict = numere(nume_lista)
print(my_dict)
"""
11. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
"""
def max(a, b, c):
    maxim = 0
    if a > b:
        if a > c:
            maxim = a
        else:
            maxim = c
    else:
        maxim = b
        if b > c:
            maxim = b
        else:
            maxim = c
    return maxim
print(max(1,3,9))


def max(a, b, c):
    nr_maxim =


"""
12. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: dacă dam numarul 3, suma va fi 6 (0+1+2+3)
"""

def get_max_number(x):
  sum = 0
  for i in range(x+1):
      sum += i
  return sum
print(get_max_number(1))







"""
13. Functie care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
"""
 list1 =[]
 list2 = []
 def common_elements(list1, list2):
     result = []
     for element in list1:
         if element in list2:
             result.append(element)
    return result

 print(common_elements([1,2,2,7],[1,3,3,7]))

"""
14. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90 de lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.
"""


"""
15. Funcție care sa afiseze data si ora curenta din Romania.
(bonus: afiseaza si data si ora curenta din China)
"""
from datetime import datetime
#
# # datetime object containing current date and time
# now = datetime.now()
#
# print("now =", now)
#
# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
# print("date and time =", dt_string)

# datetime = datetime.now(time_CHINA)
# print("In China ora este: ", datetime.strftime("%H:%M:%S") )
#


"""
16. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la Craciun
daca nu vrei sa ne zici cand e ziua ta :)
"""