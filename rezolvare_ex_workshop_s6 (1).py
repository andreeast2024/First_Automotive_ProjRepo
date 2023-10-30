# """
# REZOLVARE CICLURI REPETITIVE - EXERCITII WORKSHOP (Sesiunea 6)
# """
#
# """
# 1. Avand lista:
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# Foloseste un for ca sa interezi prin toata lista si sa afisezi 'Masina mea preferata este x':
#
# a. Fa acelasi lucru cu un for each.
# b. Fa acelasi lucru cu un while.
# """
#
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# # FOR EACH
# for masina in masini:
#     print(f"Masina mea preferata este {masina}")
#
# # WHILE
# i = 0
# while i < len(masini):
#     print(f"Masina mea preferata este {masini[i]}")
#     i += 1
#
# """
# 2. Folosind aceeasi lista ca la exercitiul 1:
#
# - foloseste un for else:
#     - in for: modifica elementele din lista astfel incat sa fie scrise cu majuscule,
#     exceptand primul si ultimul.
#     - in else: printeaza lista
# """
# for index in range(len(masini)):
#     masini[index] = masini[index].upper()
# else:
#     print(f"Lista cu masini: {masini}")
#
#
# """
# 3. Folosind aceeasi lista ca la exercitiul 1:
# Vine un cumparator care doreste sa cumpere Mercedes.
# Itereaza prin lista cu masini prin modalitatea aleasa de tine.
# Daca masina e 'Mercedes':
# - printeaza 'Am gasit masina dorita de dvs'
# - iesi din ciclu folosind un cuvant cheie care face acest lucru
# altfel:
# - printeaza 'Am gasit masina X. Mai cautam.'
# """
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for masina in masini:
#     if masina == 'Mercedes':
#         print("Am gasit masina dorita de dvs")
#         break
#     print(f"Am gasit masina {masina}. Mai cautam.")
#
# """
# 4. Folosind aceeasi lista ca la exercitiul 1:
# Vine un cumparator bogat dar indecis.
# Ii vom prezenta toate masinile, cu exceptia Trabant si Lastun.
# Daca masina e Trabant sau Lastun:
# - Foloseste un cuvant cheie sa dea skip la ce urmeaza (nu trebuie else)
# - Printeaza "S-ar putea sa va placa masina X".
# """
#
# for masina in masini:
#     if masina == 'Trabant' or masina == 'Lastun':
#         continue
#     print(f"S-ar putea sa va placa masina {masina}")

"""


# Exemplul 3 - validarea credentialelor de conectare
username = input("Introduceti numele de utilizator: ")
password = input("Introduceti parola: ")

while len(username) < 6 and len(password) < 6:
    print("Usernamel-ul si parola trebuie sa aiba min 6 caractere!")
    username = input("Introduceti numele de utilizator: ")
    password = input("Introduceti parola: ")
print("Autentificare reusita")



