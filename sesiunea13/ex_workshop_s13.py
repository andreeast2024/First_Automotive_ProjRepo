"""
OOP

1. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""
class Angajat:
    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        print(f" Angajatul cu numele {self.nume} si prenumele {self.prenume} are un salariu de {self.salariu}")

    def nume_complet(self):
        print (f" Angajatul se numeste {self.nume} {self.prenume}")

    def salariu_lunar(self):
        print(f" Angajatul are salariul de {self.salariu}")

    def salariu_anual(self):
        print(f" Angajatul are salariul de {self.salariu * 12}")

    def marire_salariu(self, procent):
        marire_salariu = procent / 100 * self.salariu
        self.salariu = marire_salariu + self.salariu
        print(f" Angajatul {self.nume} a primit o marire de salariu de {self.salariu} ")

angajat1 = Angajat(nume = "Popescu", prenume= "Marian", salariu = 6000)
angajat1.salariu_anual()
angajat1.descrie()
angajat1.marire_salariu(20)
"""

 2. Clasa Factură
- Atribute: seria (va fi constantă, nu trebuie constructor, 
toate facturile vor avea aceeași serie), număr, nume_produs, cantitate, pret_buc
- Constructor: toate atributele in constructor (cu exceptia atributului serie)
- Metode:
schimbă_cantitatea(cantitate)
schimbă_prețul(pret)
schimbă_nume_produs(nume)
generează_factura() - va printa tabelar dacă reușiți

Factura seria x număr y
Data: generează automat data de azi
Produs | cantitate | preț bucată | Total 
Telefon |      7       |       700       | 49000     

Indiciu pentru dată: https://www.geeksforgeeks.org/get-current-date-using-python/
"""
from datetime import date
class Factura:

    serie = "J1234"
    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        print(f"Noua cantitate este {self.cantitate}")

    def schimba_pretul(self, pret):
        self.pret_buc = pret
        print(f"Noul pret este {self.pret_buc}")

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume
        print (f"Numele produsului este {self.nume_produs}")

    def genereaza_factura(self):
        data_azi = date.today()
        self.format_tabel = [["produs", "cantitate", "pret_bucata", "Total"], [self.nume_produs, self.cantitate, self.pret_buc, self.cantitate * self.pret_buc]]
        print(f"Factura seria: {self.serie} cu numarul {self.numar}\ndata:{data_azi}")
        for row in self.format_tabel:
            print('| {:^6} | {:^9} | {:^12} | {:^6}'.format(*row))

factura1 = Factura(numar = 1, nume_produs= "playstation", cantitate = 2, pret_buc = 10000)
factura1.genereaza_factura()

