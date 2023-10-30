# """
# CICLURI REPETITIVE - EXERCITII WORKSHOP (Sesiunea 7)
# """
#
# """
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
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# masini_vechi = []
#
# for masini_vechi in masini:
#     if masini_vechi == 'Lastun' or masini_vechi == "Trabant"
#         print("Acestea sunt masini vechi:")
#
#         masini
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
# pret_masini = {
#     'Dacia': 6800,
#     'Lăstun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# for marca, pret in pret_masini.items():
#     if pret <= 15000:
#
#        print(f" masini cu pretul sub 15000 de euro: {marca}, {pret}")
#     else:
#        print(f" masini cu pretul peste 15000 de euro: {marca}, {pret}")
#
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
#
# buget = 15000
#
# for masina, pret in pret_masini.items():
#     if pret <= buget:
#         print(f"Pentru un buget de sub {buget} euro, puteți alege mașina {masina}.")




#
# """
# 3. Având lista:
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# Iterează prin ea.
# Afișează de câte ori apare 3 (nu ai voie să folosești count).
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# for numar in numere:
#    if numar != 3:
#       continue
#    print(numar)


# """
#
# """
# 4. Aceeași listă:
# Iterează prin ea
# Calculează și afișează suma numerelor (nu ai voie să folosești sum).

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# suma = 0
# for numar in numere:
#    suma += numar
# print(suma)
# """
#
#
# """
# # 5. Aceeași listă:
# # Iterează prin ea.
# #



# """
#
# """
# 6. Aceeași listă:
# Iterează prin ea.
# Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
# Ex: dacă e 3, să devină -3
# Afișază noua listă.

# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# numere_negative = [0]
#
# for numar in numere:
#    if numar > 0:
#       numar *= -1
#    print(numar)

# """
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
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for numar in alte_numere:
   if numar % 2 ==0:
      numere_pare.append(numar)
   else:
      numere_impare.append(numar)
   if numar >= 0:
   numere_pozitive.append(numar)
   else:
   numere_negative.append()
   print("Afiseaza numere pare")

   numere.ne









# Exerciții Recomandate - studiu individual                                        .

# 1. Revizualizează sesiunile din această săptămână și ia notițe în caz că ți-a scăpat ceva.
#
# 2. Vizualizează din cursul  ‘Primii pași în Programare’ de la sectiunile de mai jos:
# Structuri de date
# Flow Control
# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterează prin listă 2d
# Printează ‘Cifra curentă este x’
# (hint: nested for - adică for în for)

# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# for tastatura in tastatura_telefon:
#     print(f"Linia curenta este: {tastatura}")
#     for cifra in tastatura:
#         print(cifra)
