"""EX 2:
a. Defineste o clasa noua Dog.
b. Obiectele de tip Dog vor avea obligatoriu 2 atribute:
name si age.
c. Creeaza doua obiecte de tip clasa Dog, acceseaza atributele
si afiseaza-le.
d. Schimba atributul nume pentru unul din obiecte
si afiseaza-l din nou.
e. Creaza o metoda description, care returneaza
mesajul '{nume} is {age} years old'.
f. Folosind unul din obiecte
apeleaza metoda description, salveaza rezultatul
intr-o variabila si afiseaza variabila.
g. Clasa Dog este caracterizata si de atributul rasa.
Adauga acest atribut ca si un atribut al clasei (nu al obiectului)
h. Adauga o noua metoda in clasa Dog, numita speak,
care ia un parametru numit sound.
Metoda trebuie sa returneze mesajul "<name> says <sound>."
i. Apeleaza metoda speak pe unul din obiecte si afiseaza
rezultatul.
"""

class Dog:
    def__init__(self, name, age):
    self.name = name
    self.age = age
