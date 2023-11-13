# 2. a. Defineste o clasa numita Person, cu urmatoarele:
# - caracteristici/atribute in constructor: nume, varsta, inaltime
# - metode: doarme, citeste, lucreaza
# - metoda descrie care afiseaza un mesaj sugestiv cu toate atributele disponibile
# b. Accesati toate atributele disponibile pe un obiect din clasa Person
# c. Accesati/apelati toate metodele disponibile pe un obiect din clasa Person
# d. Defineste o clasa numita Student, care va mosteni din clasa Person, cu urmatoarele:
# - caracteristici: nume_facultate, an_studiu
# - metode: descrie - va trebui sa extindeti metoda descrie din clasa de baza
# si sa mai afisati un mesaj sugestiv cu noile atribute
# e. Accesati toate atributele disponibile pe un obiect din clasa Student
# f. Accesati toate metodele disponibile pe un obiect din clasa Student
# """

class Person:
    def__init__(self, nume, varsta, inaltime):
        self.nume = nume
        self.varsta = varsta
        self.inaltime = inaltime
    def.doarme(self):
        print("doarme")
    def.citeste(self):
        print("citeste")
    def.lucreaza(self):
        print("lucreaza")
    def.descrie(self):
        print(f'Persoana {self.nume} are varsta {self.varsta} si inaltimea {self.inaltime} cm ')
        
    person1 = Person(nume = "Anghelescu George", varsta = 27, inaltime = 187)
    
print(person1.nume)
print(person1.varsta)
print(person1.inaltime)

person1(descrie)
person1(doarme)
person1(citeste)
person1(lucreaza)

class Student(Person):
    def__init__(self, nume, varsta, inaltime, nume_facultate, an_studiu):
        super().__init__(nume, varsta, inaltime)
        self.nume_facultate = nume_facultate
        self.an_studiu = an_studiu
        
    def descrie(self):
        super().descrie()
         print(f"Studiaza la facultatea {self.nume_facultate} si e in anul {self.an_studiu}.")

student = Student(nume= "Ionescu Maria",
    varsta= 20,
    inaltime = 156,
    nume_facultate = "UMF Cluj",
    an_studiu = 2
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
    def__init__(self, nume, pret, discount):
        self.nume = nume
        self.pret = pret
        self.discount = discount
    def__init__(self, nume, pret, discount):
        self.__nume = nume
        self.__pret = pret
        


