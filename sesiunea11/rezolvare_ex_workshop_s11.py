"""
REZOLVARE PILONI OOP - EXERCITII WORKSHOP (Sesiunea 11)
"""

"""
EX1: MOSTENIRE
a. Defineste o clasa numita Persoana.
Aceasta clasa va avea urmatoarele atribute (in constructor):
- nume
- varsta

Implementeaza metoda descrie(), care va afisa mesajul:
'Persoana {nume} are {varsta} ani.'

b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
Aceasta clasa va lua in constructor inca doi parametri,
salariu si post.
Defineste metoda afiseaza_salariu, care returneaza
atributul salariu.

c. Creeaza un obiect de tip clasa Persoana.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metoda descrie.

d. Creeaza un obiect de tip Angajat.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metodele disponibile pe aceasta.

e. Extinde metoda descrie din clasa Angajat,
astfel incat sa se afiseze
si o propozitie care contine atributele salariu si post.
"""


class Persoana:

    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta

    def descrie(self):
        print(f"Persoana {self.nume} are {self.varsta} ani.")


class Angajat(Persoana):

    def __init__(self, nume, varsta, salariu, post):
        super().__init__(nume, varsta)
        self.salariu = salariu
        self.post = post

    def afiseaza_salariu(self):
        return self.salariu


persoana1 = Persoana(nume="Pop Maria", varsta=25)
print(persoana1.nume)
print(persoana1.varsta)
persoana1.descrie()

angajat1 = Angajat(nume="Pop Marius", varsta=30, salariu=5000, post="programator")
print(angajat1.nume)
print(angajat1.varsta)
print(angajat1.salariu)
print(angajat1.post)

angajat1.descrie()
print(angajat1.afiseaza_salariu())

"""
2. a. Defineste o clasa numita Person, cu urmatoarele:
- caracteristici/atribute in constructor: nume, varsta, inaltime
- metode: doarme, citeste, lucreaza
- metoda descrie care afiseaza un mesaj sugestiv cu toate atributele disponibile
b. Accesati toate atributele disponibile pe un obiect din clasa Person
c. Accesati/apelati toate metodele disponibile pe un obiect din clasa Person
d. Defineste o clasa numita Student, care va mosteni din clasa Person, cu urmatoarele:
- caracteristici: nume_facultate, an_studiu
- metode: descrie - va trebui sa extindeti metoda descrie din clasa de baza
si sa mai afisati un mesaj sugestiv cu noile atribute
e. Accesati toate atributele disponibile pe un obiect din clasa Student
f. Accesati toate metodele disponibile pe un obiect din clasa Student
"""


class Person:

    def __init__(self, nume, varsta, inaltime):
        self.nume = nume
        self.varsta = varsta
        self.inaltime = inaltime

    def doarme(self):
        print("doarme")
 

    def descrie(self):
        print(f"Persoana {self.nume} are {self.varsta} ani si inaltimea de {self.inaltime} cm.")


person2 = Person(nume="Anghelescu George", varsta=27, inaltime=187)
print(person2.nume)
print(person2.varsta)
print(person2.inaltime)

person2.descrie()
person2.doarme()
person2.citeste()
person2.lucreaza()


class Student(Person):

    def __init__(self, nume, varsta, inaltime, nume_facultate, an_studiu):
        super().__init__(nume, varsta, inaltime)
        self.nume_facultate = nume_facultate
        self.an_studiu = an_studiu

    def descrie(self):
        super().descrie()
        print(f"Studiaza la facultatea {self.nume_facultate} si e in anul {self.an_studiu}.")


student = Student(
    nume="Ionescu Maria",
    varsta=20,
    inaltime=156,
    nume_facultate="UMF Cluj",
    an_studiu=2
)

print(student.nume)
print(student.varsta)
print(student.inaltime)
print(student.nume_facultate)
print(student.an_studiu)
student.doarme()
student.lucreaza()
student.citeste()
student.descrie()

# POLIMORFISM

# Exemplu de functie built-in polimorfica
print(len("abc"))
print(len([1, 2, 3, 4]))

# functia print este o functie polimorfica
print("hello")
print("hello", "world")
print("hello", "world", sep=",")
print("hello", "world", end="*")


# Exemplu de class methods polimorfice
class Romania:
    def language(self):
        print("Romanian")


class USA:
    def language(self):
        print("English")


obj_ro = Romania()
obj_usa = USA()

obj_ro.language()
obj_usa.language()

"""
EX2: POLIMORFISM

a. Defineste o clasa Pasare care implementeaza metoda 
zboara.
In metoda zboara, afiseaza mesajul 'Majoritatea pasarilor
pot zbura.'

b. Defineste o clasa Strut, care mosteneste din clasa 
Pasare.
Defineste metoda zboara, si afiseaza mesajul 
'Strutii nu pot zbura."
(Nu extindem metoda din clasa de baza, 
ci o suprascriem -> OVERRIDING)

c. Defineste clasa Rata, care mosteneste din clasa Pasare.
Defineste metoda zboara, si afiseaza mesajul 
"Ratele pot zbura."

d. Instantiaza cele 3 clase si apeleaza metoda zboara
pe fiecare obiect.
POLIMORFISM => aceeasi metoda (acelasi nume) -> 
comportament diferit.
"""

# a.
class Pasare:

    def zboara(self):
        print("Majoritatea pasarilor pot zbura.")

# b
class Strut(Pasare):

    def zboara(self):
        print("Strutii nu pot zbura")

# c.
class Rata(Pasare):

    def zboara(self):
        print("Ratele pot zbura")

# d
pasare = Pasare()
strut = Strut()
rata = Rata()

pasare.zboara()
strut.zboara()
rata.zboara()

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Ham ham")

    def sleep(self):
        print('ZZZZ')


class Cat(Animal):

    def sound(self):
        print("Miau miau")

    def sleep(self):
        print("Prrrr")


cat = Cat()
dog = Dog()

"""
EX3: ABSTRACTIZARE
a. Defineste interfata Car. Aceasta va avea o metoda
abstracta numita car_model.

b. Defineste clasele Tesla si BMW, care implementeaza
interfata Car.
Metoda car_model trebuie sa afiseze un mesaj legat
de modelul masinii.

Instantiaza clasele Tesla si BMW si invoca metoda 
car_model pe fiecare din acestea.
"""
from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def car_model(self):
        pass


class Tesla(Car):

    def car_model(self):
        print("Tesla")


class BMW(Car):

    def car_model(self):
        print("BMW")


tesla = Tesla()
bmw = BMW()

tesla.car_model()
bmw.car_model()
# INCAPSULARE

# Cand vorbim de clase, putem avea atribute si metode:
# 1. PUBLICE
# 2. PROTECTED
#   - pentru a face un atribut sau o metoda sa fie protected,
# ii punem un _ in fata (_get_results(), _name, _age etc.)
# 3. PRIVATE
#   - pentru a face un atribut sau o metoda sa fie private,
# ii punem 2 underscore-uri in fata (__get_results(), __name, __age etc.)

class Car:

    def __init__(self, brand):
        self.__brand = brand

    def run(self):
        print(f"Please run {self.__brand}")


car = Car("Dacia")

# print(car.__brand) # -> eroare
car.run()


class Car:
    __color = 'grey'

    def get_color(self):  # folosim getter sa afisam culoarea
        return self.__color.upper()

    def set_color(self, culoarea_dorita):  # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita


class CarPy:

    def __init__(self, color):
        self.__color = color

    # definim o proprietate care sa incapsuleze
    # atributul privat __color
    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print("Getter")
        return self.__color

    @color.setter
    def color(self, culoare_noua):
        print("Setter")
        self.__color = culoare_noua

    @color.deleter
    def color(self):
        print("Deleter")
        self.__color = None


car_py = CarPy(color="red")
# print(car_py.__color)

print(car_py.color)
car_py.color = "blue"
print(car_py.color)
del car_py.color
print(car_py.color)
"""
EX4: ENCAPSULARE
a. Defineste o clasa Produs.
Aceasta va avea in constructor urmatoarele atribute:
- nume
- pret
- discount - atribut privat

b. Defineste proprietatea discount:
- getter
- setter -> inainte de a seta o valoare pentru discount,
asigura-te ca acesta e cuprins intre 0-100.
- deleter
"""

class Produs:

    def __init__(self, nume, pret, discount):
        self.nume = nume
        self.pret = pret
        self.__discount = discount

    @property
    def discount(self):
        return self.__discount

    @discount.getter
    def discount(self):
        print("Getter")
        return self.__discount

    @discount.setter
    def discount(self, new_value):
        print("Setter")
        if 0 <= new_value <= 100:
            self.__discount = new_value
        else:
            print("Discount-ul trebuie sa fie intre 0 si 100.")

    @discount.deleter
    def discount(self):
        print("Deleter")
        self.__discount = 0


produs1 = Produs(nume="birou", pret=10000, discount=20)
print(produs1.nume)
print(produs1.pret)

print(produs1.discount)

# modificam valoarea proprietatii discount sa fie 50
produs1.discount = 50

print(produs1.discount)

produs1.discount = 110
print(produs1.discount)

del produs1.discount
print(produs1.discount)