"""
INTRO OOP - EXERCITII WORKSHOP (Sesiunea 10)
"""

"""
Implementati urmatoarele clase, folosind notiuni OOP:
"""

"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria 
diametru() 
circumferinta()

"""
import math

class cerc:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare
    def descrie_cerc(self):
        print(f'Cercul are culoarea {self.culoare} si raza de {self.raza}.')

    def arie(self):
        return self.raza**2

    def diametru(self):
        return 2 * self.raza

    def circumferinta(self):
        return 2 * math.pi * self.raza
cerc1 = cerc(7, 'alba')
cerc1.descrie_cerc()
print("Aria cercului este:", cerc1.arie())
print("Diametrul cercului este:", cerc1.diametru())
print('Circumferinta cercului este:', cerc1.circumferinta())

"""
2. Clasa Dreptunghi
     Atribute: lungime, lățime, culoare
     Constructor pentru toate atributele
     Metode:
descrie()
aria()
perimetrul()
schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic. 
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul self.culoare.
Poți verifica schimbarea culorii prin apelarea metodei descrie().
"""
import math
