"""
REZOLVARE STRUCTURI DE DATE - EXERCITII WORKSHOP (Sesiunea 5)
"""

"""
Pentru toate exercitiile se va folosi notiunea de if in rezolvare!
Indirect, veti exersa si operatorii in cadrul conditiilor ramurilor din if.
"""

# --------- LISTE ---------

"""
1. Avand 2 liste: [3, 1, 0, 2] si [6, 5, 4],
gaseste 2 variante prin care sa le unesti intr-o singura lista.
"""

list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]

# Varianta 1
# Pentru a uni/concatena doua liste putem folosi semnul +

# unim cele doua liste si salvam rezultatul intr-o variabila noua, list3
list3 = list1 + list2

# afisam list3
print(list3)

# Varianta 2
# Pentru a uni/concatena doua liste putem folosi o metoda ajutatoare
# disponibila pe liste, numita extend.
# ATENTIE: In acest caz, se va suprascrie lista pe care o extindem
# cu lista extinsa

# extindem list1 cu valorile din list2
list1.extend(list2)

# afisam list1, care acum reprezinta lista extinsa
print(list1)

"""
2. 
a. Sorteaza lista generata la exercitiul 1, folosind functia built-in sorted().
Afiseaza lista. Ce observi?
b. Sorteaza lista generata la exercitiul 1 folosind o metoda ajutatoare de pe liste.
Afiseaza lista. Ce observi?
"""

# a.
# Functia built-in sorted() poate fi folosita pentru a sorta o lista.
# Aceasta functie returneaza o noua lista, sortata.
# Lista initiala ramane la fel.

# Sortam lista list3, folosind functia sorted() si afisam rezultatul.
# Rezultatul va fi lista sortata
print(sorted(list3))

# Afisam lista list3 si observam ca aceasta nu e modificata.
print(list3)

# b.
# Pentru a sorta o lista putem sa folosim o metoda ajutatoare de pe liste,
# numita sort().
list3.sort()

# Folosind metoda ajutatoare sort() vom observa ca lista initiala este acum
# sortata.
print(list3)

"""
3. Folosind un if, verifica daca lista generata la exercitiul 1 este goala,
si afiseaza un mesaj corespunzator in functie de caz:
- Lista este goala
- Lista nu este goala
"""

# Varianta 1
# O lista goala nu are nici un element, astfel ca o modalitate prin care
# putem verifica daca o lista este goala sau nu, este sa verificam lungimea acesteia.
if len(list3) == 0:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# Varianta 2
# O lista goala, [], convertita la bool va fi False
if not bool(list3):
    print("Lista este goala")
else:
    print("Lista nu este goala")

# Varianta 3
# Cand folosim un if, ceea ce scriem ca si conditie la if, este
# convertit de catre Python la True sau False, astfel ca,
# conversia listei la bool pentru verificare nu este neaparat necesara (este optionala)
if not list3:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# Varianta 4
# Putem verifica daca lista are valoarea [], in acest caz aceasta fiind goala.
if list3 == []:
    print("Lista este goala")
else:
    print("Lista nu este goala")

"""
4. Foloseste o functie (metoda ajutatoare de pe lista) care sa stearga lista de la exercitiul 1.
"""
list3.clear()
print(list3)

"""
5. Copy paste la exercitiul 3.
Verifica inca o data. Acum ar trebui sa se afiseze ca lista este goala.
"""

# Varianta 1
# O lista goala nu are nici un element, astfel ca o modalitate prin care
# putem verifica daca o lista este goala sau nu, este sa verificam lungimea acesteia.
if len(list3) == 0:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# Varianta 2
# O lista goala, [], convertita la bool va fi False
if not bool(list3):
    print("Lista este goala")
else:
    print("Lista nu este goala")

# Varianta 3
# Cand folosim un if, ceea ce scriem ca si conditie la if, este
# convertit de catre Python la True sau False, astfel ca,
# conversia listei la bool pentru verificare nu este neaparat necesara (este optionala)
if not list3:
    print("Lista este goala")
else:
    print("Lista nu este goala")

# Varianta 4
# Putem verifica daca lista are valoarea [], in acest caz aceasta fiind goala.
if list3 == []:
    print("Lista este goala")
else:
    print("Lista nu este goala")


# --------- DICTIONARE ---------

"""
6. Se da dictionarul:
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}

Foloseste o functie (metoda ajutatoare dictionar) ca sa afisezi numele elevilor (cheile)
"""

dict1 = {
    "Ana": 8,
    "Gigel": 10,
    "Dorel": 5
}

print(dict1.keys())

"""
7. Printeaza cei 3 elevi si notele lor.
Exemplu: "Ana a luat nota 8".
Doar nota o vei lua folosindu-te de cheie.
"""
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")

"""
8. Dorel a facut contestatie si a primit 6.
a. Modifica nota lui Dorel in 6.
b. Printeaza nota dupa modificare.
"""

# a
# Varianta 1
dict1["Dorel"] = 6

# Varianta 2
dict1.update({"Dorel": 6})

# b
print(dict1["Dorel"])

"""
9. Gigel se transfera din clasa.
a. Cauta o functie care sa il stearga. Afiseaza dictionarul dupa stergere
b. Vine un coleg nou, Ionica. Adauga-l in dictionar si pune-i nota 9.
c. Printeaza noii elevi.
"""

# a
# Pentru a sterge perechea "Gigel": 10, dupa cheie,
# folosim metoda pop() disponibila pe dictionar
dict1.pop("Gigel")

# afisam dictionarul
print(dict1)

# b
# Varianta 1
dict1["Ionica"] = 9

# Varianta 2
dict1.update({"Ionica": 9})

# c
# Afisam dictionarul actualizat
print(dict1)

# --------- SETURI ---------

"""
10. Se dau urmatoarele seturi:
zile_sapt = {"luni", "marti", "mercuri", "joi", "vineri", "sambata", "duminica"}
weekend = {"sambata", "duminica"}

a. Adauga in zile_sapt "luni".
b. Afiseaza zile_sapt. Ce observi?
"""
zile_sapt = {"luni", "marti", "mercuri", "joi", "vineri", "sambata", "duminica"}
weekend = {"sambata", "duminica"}

# a
# Pentru a adauga un nou element intr-un set, ne folosim
# de metoda ajutatoare add()
zile_sapt.add("luni")

# b

# afisam setul zile_sapt
print(zile_sapt)

# Observam ca acesta este neschimbat.
# Acest lucru se intampla deoarece "luni" exista deja in set, inainte de adaugare,
# si seturile nu permit elemente duplicate

"""
11. Folosind seturile de la exercitiul 10:
a. Foloseste un if si verifica:
 - daca weekend este un subset al zilelor din saptamana
 - daca weekend nu este un subset al zilelor din saptamana
Afiseaza un mesaj sugestiv in fiecare caz.
"""

if weekend.issubset(zile_sapt):
    print("Setul weekend este un subset al setului zile_sapt")
else:
    print("Setul weekend NU este un subset al setului zile_sapt")

"""
12. Folosind seturile de la exercitiul 10, afiseaza diferentele dintre cele 2 seturi.
"""

# Pentru a afisa diferentele intre doua seturi, ne folosim de
# metoda ajutatoare de pe seturi, numita difference()
# Sintaxa: set1.difference(set2) -> elementele ce sunt in set1 si nu sunt in set2

# Elementele ce sunt in zile_sapt si nu sunt in weekend
print(zile_sapt.difference(weekend))

# Elementele ce sunt in weekend si nu sunt in zile_sapt
print(weekend.difference(zile_sapt))

"""
13. Folosind seturile de la exercitiul 10, afiseaza intersectia elementelor dintre cele 2 seturi
"""

# Pentru a afisa intersectia intre doua seturi, ne folosim de
# metoda ajutatoare de pe seturi, numita intersection()

# Afisam elementele care se gasesc atat in setul zile_sapt, cat si in setul weekend
print(zile_sapt.intersection(weekend))

# --------- EXERCITII RECOMANDATE - STUDIU INDIVIDUAL ---------

"""
1. Revizualizeaza sesiunile de pana acum si ia notite in caz ca ti-a scapat ceva.
"""

"""
2. Vizualizeaza din cursul PRIMII PASI IN PROGRAMARE sectiunile de mai jos:
- Structuri de date
- Flow Control
"""
