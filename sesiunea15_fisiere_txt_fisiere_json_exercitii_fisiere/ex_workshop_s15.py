"""
Interactiunea cu fisiere - EXERCITII WORKSHOP (Sesiunea 15)
"""

"""
1. 
a. Creeaza un fisier txt, numit 'persons.txt' care contine pe fiecare linie,
un nume si o varsta.
b. Implementeaza o clasa Person care sa reprezinte o persoana
cu atributele nume si varsta.
c. Cititi datele din fisier si creati obiecte de tip Person
(pune toate obiectele create intr-o lista).
d. Afiseaza numele si varsta fiecarei persoane.
"""
 # a.
with open("persons.txt","w", newline="") as file:
    w = file.writelines([
        "Adrian 38\n",
        "Alex 42\n",
        "Dumi 29\n",
        "Oana 24\n"
    ])
#b.
class Person:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

#c.
with open("persons.txt","r") as file:
    r = file.readlines()

persons_list = []
for person in r:
    persons_list1 = person.split()
    person_obj = Person(
        nume = persons_list1[0],
        varsta = persons_list1[1]
    )
    persons_list.append(person_obj)
#d
for person in persons_list:
    print(f'Nume: {person.nume} {person.varsta}')

"""
2. 
a. Creeaza un fisier JSON, cu informatii despre carti:
- practic va fi o lista, cu dictionare
- in fiecare dictionar vom avea informatiile despre o carte
- pentru fiecare carte vom avea urmatoarele informatii: titlu, autor, an

b. Implementeaza o clasa Book care sa reprezinte o carte (atribute: titlu, autor, an)
c. Citeste datele din fisierul JSON si creaza obiecte de tip Book
(pune toate obiectele create intr-o lista)
d. Afiseaza numele cartilor publicate dupa un anumit an.
"""
# a.
import json
with open("carti.json" , "w") as file:
    carti = {
        "titlu": "Batranul si Marea",
        "autor": "Ernest Hemingway",
        "an": 1900
    },{
        "titlu": "Alice in Wonderland",
        "autor": "Lewis Carol",
        "an": 1865
    }
    json.dump(carti, file, indent = 4)


# b.

class Book:
    def __init__(self, titlu, autor, an):
        self.titlu = titlu
        self.autor = autor
        self.an = an
#c.
with open("carti.json" , "r") as file:
    r = json.load(file)

book_list = []
for carte in r:
    lista_carti1 = Book(
        titlu = carte["titlu"],
        autor = carte["autor"],
        an = carte["an"]
    )
    book_list.append(lista_carti1)
#d

for book in book_list:
   if book.an == 1865:
       print(f'Cartile din anul {book.an} sunt {book.titlu}')

"""
3. 
a. Creati un fisier CSV cu informatii despre facturi (id, serie, numar, client, suma, status
(IMPORTANT: statusul poate sa fie "emisa" sau "incasata"
Asigura-te ca ai in fisierul tau CSV mai multe linii pentru acelasi client cu status diferit.
b. Implementeaza o clasa Factura care sa reprezinte o factura (atribute: id, serie, numar, client, suma, status)
c. Citeste datele din fisierul CSV si creeaza obiecte din clasa de tip Factura
(pune toate obiectele create intr-o lista)
d. Afiseaza informatiile despre facturile emise de un anumit client si doar cele cu statusul "incasata"
e. Avand in vedere facturile prelucrate la punctul d, afiseaza suma totala incasata de clientul respectiv.
"""
#a.
import csv
with open("facturi.csv", "w", newline = "") as file:
    w = csv.writer(file)
    w.writerows(
        [["id", "serie", "numar", "client", "suma","status"],
         ["FG", 4, 89, "Adrian Stefan", 1300, "incasata"],
         ["LG", 5, 90, "Oana Popescu", 1700, "emisa"],
         ["BG", 6, 91, "Alex Ioan", 2000, "incasata"],
         ["BG", 7, 92, "Alex Ioan", 2700, "incasata"],
         ["HD", 8, 93, "Marcel Toma", 2900, "emisa"]

    ])
#b.

class Factura:
    def __init__(self, id, serie, numar, client, suma, status):
        self.id = id
        self.serie = serie
        self.numar = numar
        self.client = client
        self.suma = suma
        self.status = status

#c.
lista_facturi = []
with open("facturi.csv", "r") as file:
    r = csv.reader(file)
    header = next(file)
    for factura in r:
        lista_facturi.append(factura)
print(lista_facturi)
lista_facturi1 = []
for factura in lista_facturi:
    factura_obj = Factura(
        id = factura[0],
        serie = factura[1],
        numar = factura[2],
        client = factura[3],
        suma = factura[4],
        status = factura[5]

    )
    lista_facturi1.append(factura_obj)
for factura in lista_facturi1:
    if factura.status == "incasata":
        print(f' Facturile incasate sunt {factura.client} ')

#e
suma_facturi = 0
client_cautat = "Oana Popescu"
for factura in lista_facturi1:
    if factura.status == "incasata" and factura.client == client_cautat:
        suma_facturi += int(factura.suma)
print(f'Suma totala incasa de {client_cautat} este {suma_facturi}')



"""
4. 
a. Creati un fisier JSON care contine informatii despre produse (id, nume, cantitate, pret (per buc)), nume_furnizor
b. Creati o clasa care reprezinta un produs, numita Product (cu atributele: id, nume, cantitate, pret, nume_furnizor)
c. Citeste datele din fisierul JSON si creeaza obiecte din clasa de tip Product
(pune toate obiectele create intr-o lista)
d. Construieste o lista cu produsele care nu mai sunt in stoc.
e. Construieste o lista cu produsele care sunt in stoc si au un anumit furnizor.
"""
#a
import json
with open("stock.json" , "w") as file:
    stock = {
        "id": "1",
        "nume": "Televizor",
        "cantitate": 10,
        "pret(per buc))": 2400,
        "nume_furnizor": "SONY"
    },{
        "id": "2",
        "nume": "Apple 15",
        "cantitate": 13,
        "pret(per buc))":5000,
        "nume_furnizor": "Apple"

    },{
        "id": "3",
        "nume": "Monitor",
        "cantitate": 0,
        "pret(per buc))": 1000,
        "nume_furnizor": "HP"
    }

    json.dump(stock, file, indent = 4)

#b

class Product:
    def __init__(self, id, nume, cantitate, pret, nume_furnizor):
        self.id = id
        self.nume = nume
        self.cantitate = cantitate
        self.pret = pret
        self.nume_furnizor = nume_furnizor

#c.
with open("stock.json" , "r") as file:
    r = json.load(file)

product_list = []
for product in r:
    product_list1 = Product(
        id = product["id"],
        nume = product["nume"],
        cantitate = product["cantitate"],
        pret = product["pret(per buc))"],
        nume_furnizor = product["nume_furnizor"]
    )
    product_list.append(product_list1)
#d.

stock_produse = []
for factura in product_list:
    if factura.cantitate == 0:
        stock_produse.append(factura)
        print(f'Produsele care au stocul {factura.cantitate} sunt {factura.nume}')

#e.
furnizor = "Apple"
stock_furnizor = []
for produs in product_list:
   if produs.nume_furnizor == furnizor and produs.cantitate > 0:
       stock_furnizor.append(produs)
       print(f'Produsele in stoc de la furnizorul {furnizor} sunt {produs.nume}, stoc {produs.cantitate }')





