"""
1. Se dau doua liste:
lista_1 = [10, 20, 30, 40, 50, 10]
lista_2 = [1, 2, 3, 4, 5]
Pentru fiecare lista verifica daca primul si ultimul element sunt egale.
In functie de rezultat, afiseaza un mesaj.
"""

"""
2. Scrie un program care afiseaza de cate ori apare litera 'e' in
stringul str_1 = 'Emma is a sofware developer.'
"""

"""
3. Scrie un program in care citesti de la tastatura doua nr intregi,
numite base si exponent.
Afiseaza intr-un mesaj sugestiv, valoarea lui base la puterea exponent.
Atentie: indiferent daca utilizatorul a introdus un numar pozitiv sau negativ
ca si exponent, trebuie sa ridici base la puterea exponent pozitiv.
hint: exploreaza functia abs() si vezi cum o poti folosi
"""

"""
4. Scrie un program in care se citeste de la tastatura un string.
Daca string-ul are numar impar de caractere, afiseaza un string care
contine primul caracter, caracterul din mijloc si ultimul caracter
al string-ului citit de la tastatura.
Daca string-ul are numar par de caractere, afiseaza un string care contine doar primul
si ultimul caracter  al string-ului citit de la tastatura.
"""

"""
5. Se dau doua variabile:
str1 = 'Abc'
str2 = 'Xyz'
Creeaza o variabila string, str3 formata din:
- primul caracter din str1 cu litera mica
- primul caracter din str2 cu litera mare
- al doilea caracter din str1 cu litera mare
- al doilea caracter din str2 cu litera mare
- al treilea caracter din str1 cu litera mare
- al treilea caracter din str2 cu litera mica
"""

"""
6. Se da lista:
fruits = ["apple", "banana", "cherry"]
a. Schimba elementul 'apple' cu 'kiwi'.
b. Foloseste metoda append() pentru a adauga elementul 'oranges'.
c. Foloseste metoda insert() pentru a adauga elementul 'lemon' ca al doilea
element din lista.
d. Foloseste metoda remove() pentru a sterge elementul 'banana' din lista.
e. Foloseste un index negativ pentru a accesa ultimul element din lista.
f. Foloseste un index negativ pentru a accesa penultimul element din lista.
g. Afiseaza lungimea listei.
h. Foloseste slicing pe lista, astfel incat sa obtii o lista cu al doilea, al treilea
si al patrulea element.
"""

"""
7. Inverseaza lista my_list = [100, 200, 300, 400].
"""

"""
8. Lista de cumparaturi:
Se citeste de la tastatura o lista de cumparaturi. Utilizatorul introduce
lista de cumparaturi ca un string, cu alimentele separate prin virgula,
ATENTIE: fara spatii
Exemplu:rosii,castraveti,branza,oua
a. Sa se transforme string-ul citit de la tastatura intr-o lista. (vezi metode ajutatoare string).
b. Sorteaza lista de cumparaturi si printeaza lista sortata.
c. Adauga un aliment nou in lista de cumparaturi.
d. Sterge un aliment din lista de cumparaturi.
e. Modifica elementul de la pozitia 0 din lista.
f. Daca lista contine 'rosii' in ea, afiseaza mesajul "Aliment sanatos".
Daca nu, afiseaza mesajul "Iti recomandam rosiile de asemenea".
"""

"""
9. Se da lista fructe = ['capsuni', 'mere', 'lamai'].
Converteste lista la string si afiseaza string-ul. A se vedea metoda join(). (search on google)
"""

"""
10. Se da lista numere = [1, 2, 3, 4, 56, 22, 5].
Afiseaza elementul cu valoarea maxima din string. (google- functia max())
"""

"""
11. Se da lista preturi = [12.3, 34.5, 22].
Calculeaza suma elementelor din lista preturi. (google - functia sum())
"""

"""
12. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza valoarea cheii city.
b. Kelly a fost promovata. Salariul ei este acum de 10000 lei. Fa modificarea si in dictionar.
c. Sterge varsta din dictionar.
d. Adauga o noua pereche cheie-valoare in dictionar, cu cheia employment_date. Valoarea o alegi tu.
e. Verifica daca exista cheia 'country' in dictionar. Daca nu exista, adauga-o.
"""

"""
13. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza toate cheile din dictionar. (HINT: metoda keys())
b. Afiseaza toate valorile din dictionar. (HINT: metoda values())
c. Verifica lungimea dictionarului.
"""

"""
14. Gasirea unui element intr-un dictionar
Se da dictionarul:
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul introduce cheia cautata.
Verifica daca aceasta se gaseste sau nu in dictionar.
"""

"""
15. Adaugarea unui element intr-un dictionar
Se da dictionarul:
 persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul trebuie sa introduca cheia si valoarea pe care doreste sa
le adauge in dictionar.
Foloseste metoda update() (metoda ajutatoare pe dictionar)
"""

"""
16. Stergerea unui element din dictionar
 Se da dictionarul:
 persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}
Utilizatorul introduce cheia elementului de eliminat.
a. Elimina elementul, verificand prima data daca cheia se afla in dictionar,
si daca se afla, foloseste metoda del.
b. Elimina elementul, folosind metoda ajutatoare pop().
"""

"""
17. Concatenarea a doua dictionare.
Se dau doua dictioanare:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
Sa se concateneze cele doua dictionare folosind metoda update().
Observatie: Metoda update() o putem folosi pentru a adauga unul sau mai multe
perechi cheie:valoare in dictionar.
"""

"""
18. Se da urmatoarea lista cu dictionare:
lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
a. Adauga perechea {'c':'3'} in primul dictionar din lista.
b. Adauga un nou dictionar ca element in lista. Adauga-l la final.
c. Aduaga un nou dictionar ca element in lista, la indexul 1.
d. Verifica daca in al doilea dictionar din lista se gaseste cheia 'c'.
"""

"""
19.
Se citeste de la tastatura un numar.
a. Printeaza un mesaj sugestiv daca numarul este par sau nu.
b. Daca numarul este multiplu de 4, afiseaza un mesaj sugestiv.
"""

"""
20.
Se citesc de la tastatura doua numere, num si check. Verifica daca
num este divizibil cu check si afiseaza un mesaj corespunzator catre utilizator.
"""

"""
21. Se da dictionarul:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
a. Foloseste metoda get() pentru a printa valoarea cheii 'model'.
b. Schimba valoarea cheii 'year' in 1970.
c. Adauga perechea cheie:valoare 'color':'red' in dictionar.
Adaug-o folosind accesarea dictionarului prin cheie (car['color']) si dand o valoare.
Adaug-o folosind metoda update()
d. Foloseste metoda pop() pentru a sterge 'model' din dictionar.
e. Foloseste metoda empty() pentru a 'goli' dictionarul.
"""
