"""
REZOLVARE CICLURI REPETITIVE - EXERCITII WORKSHOP (Sesiunea 7)
"""

"""
# 1. Modernizează parcul de mașini:
# 
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# 
# Crează o listă goală, masini_vechi.
# Iterează prin mașini.
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# Printează Modele vechi: x.
# Modele noi: x.
# """
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# masini_vechi = []
#
#  for i in range(0, len(masini)):
#     if masini[i] in ["Lastun", "Trabant"]:
#          masini_vechi.append(masini[i])
#       masini[i] = "Tesla"
#  print(f"Modele vechi: {masini_vechi}")
# print(f"Modele noi: {masini}")

#
# """
# 2. Având dict:
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# Vine un client cu un buget de 15000 euro.
#
# Prezintă doar mașinile care se încadrează în acest buget.
# TIP: Cauta pe net ce e dict.items() si vezi cum poti sa il folosesti
#
# Iterează prin dict.items() și accesează mașina și prețul.
# Printează Pentru un buget de sub 15000 euro puteți alege mașină Lastun
# """
#
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# buget = 15000
#
# for cheie, valoare in pret_masini.items():
#     # cheia e numele masinii
#     # valoarea e pretul
#     if valoare < buget:
#         print(f"Pentru un buget de sub {buget} euro, puteti alege masina {cheie}")
#
#
# """
# 3. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).
# """
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# count = 0
# for numar in numere:
#     if numar == 3:
#         count += 1
#
# print(count)
#
# """
# 4. Aceeași listă:
# Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).
# """
#
# suma = 0
# for numar in numere:
#     suma += numar
# print(suma)
#
# """
# 5. Aceeași listă:
# Iterează prin ea.
# Afișază cel mai mare număr (nu ai voie să folosești max).
# """
# nr_max = 0
# for numar in numere:
#     if numar > nr_max:
#         nr_max = numar
# print(nr_max)
#
# """
# 6. Aceeași listă:
# Iterează prin ea.
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# Afișază noua listă.
# """
#
# for index in range(0, len(numere)):
#     if numere[index] > 0:
#         numere[index] = -1 * numere[index]
# print(numere)
#
# """
# 7.
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Itereaza prin listă alte_numere
# Populează corect celelalte liste
# Afișează cele 4 liste la final
# """
#
# alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
#
# for numar in alte_numere:
#     if numar % 2 == 0:
#         numere_pare.append(numar)
#     else:
#         numere_impare.append(numar)
#
#     if numar > 0:
#         numere_pozitive.append(numar)
#     else:
#         numere_negative.append(numar)
#
# print(numere_pare)
# print(numere_impare)
# print(numere_pozitive)
# print(numere_negative)


# Exerciții Recomandate - studiu individual                                        .

# 1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.
#
# 2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
# Structuri de date
# Flow Control

# """
# 1. Ghicitoare de număr:
# numar_secret = Generați un număr random între 1 și 30
# Numar_ghicit = None
# Folosind un while
#    User alege un număr
#    Programul îi spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitări! Ai ghicit!
# """

# import random
# numar_secret = random.randint(1,30)
# numar_ghicit = int(input('Introduceti un numar de la tastatura intre 1 si 30: '))
#var1
# while numar_secret != numar_ghicit:
#     if numar_ghicit < numar_secret:
#         print('Numarul secret este mai mare!')
#         numar_ghicit = int(input('Introduceti un numar de la tastatura intre 1 si 30: '))
#     elif numar_ghicit >numar_secret:
#         print('Numarul secret este mai mic!')
#         numar_ghicit = int(input('Introduceti un numar de la tastatura intre 1 si 30: '))
# print('Felicitari, ati ghicit!')
#var2
# while numar_secret != numar_ghicit:
#     if numar_ghicit < numar_secret:
#         print('Numarul secret este mai mare!')
#         numar_ghicit = int(input('Introduceti un numar de la tastatura intre 1 si 30: '))
#     elif numar_ghicit > numar_secret:
#         print('Numarul secret este mai mic!')
#         numar_ghicit = int(input('Introduceti un numar de la tastatura intre 1 si 30: '))
# else:
#     print('Felicitari, ati ghicit!')
# """
#
# my_dict = {
#     "name": "Mihai",
#     "salary": 10000,
# }
# print(my_dict)

# colors_set = {"red", "green", "blue"}
#
# colors_set.add("orange")
# colors_set.add("red")
# print(colors_set)

pret_masini = {
    'Dacia': 6800,
    'Lăstun': 500,
    'Opel': 1100,
    'Audi': 19000,
   'BMW': 23000
 }

buget = 15000

for cheie, valoare in pret_masini.items():

    # cheia e numele masinii
     # valoarea e pretul
    if valoare < buget:
     print(f"Pentru un buget de sub {buget} euro, puteti alege masina {cheie}")
#3. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).
# """
    numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

    count = 0
for numar in numere:
     if numar == 3:
         count += 1
         print(count)