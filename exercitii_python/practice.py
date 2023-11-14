# INTRO OOP

# definirea clasei
class Car:
    # atributele ale clasei
    make = 'Dacia'
    model = None
    year = 2022
    color = None
    price = 10000

    # metodele
    def accelerate(self):
        print("Vrum vrrum")

    def stop(self):
        print("STOP")

    def describe(self):
        print(f"Masina a fost fabricata in anul {self.year}")
        print(f"Masina are culoarea {self.color}")

    def testdrive(self):
        # apelez metoda accelerate
        self.accelerate()
        # apelez metoda stop
        self.stop()

# crearea obiectelor din clasa Car

# am creat un obiect din clasa Car
# si l-am salvat intr-o variabila numita car1
# am instantiat clasa Car si am salvat obiectul in
# variabila numita car1
car1 = Car()

# accesam atributul make
print(car1.make)

# schimbam valorile atributelor
print(car1.model)
car1.model = "Logan"
print(car1.model)

# apelam/invocam metoda accelerate disponibila
# pe obiectul car1
car1.accelerate()

# apelam/invocam metoda stop disponibila
# pe obiectul car1
car1.stop()

# am creat un alt obiect din clasa Car
# si l-am salvat intr-o alta variabila numita car2
car2 = Car()
print(car2.make)
print(car2.model)

car2.accelerate()
car2.stop()
car2.describe()

# schimbam culoarea masinii
car2.color = "rosu"
car2.describe()
car2.testdrive()

# my_list = [1, 2, 3]
# my_list.append(3)
# len(my_list)


# CONSTRUCTOR

class Car:
    # atributele ale clasei
    make = 'Dacia'

    def __init__(self, model, year, color, price):
        # aici se definesc
        # atribute pe obiect
        # adica atribute specifice fiecarui obiect in parte

        # ca atribute pe obiect, dorim sa avem
        # modelul, anul, culoarea si pretul
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    # metodele
    def accelerate(self):
        print("Vrum vrrum")

    def stop(self):
        print("STOP")

    def describe(self):
        print(f"Masina a fost fabricata in anul {self.year}")
        print(f"Masina are culoarea {self.color}")

    def testdrive(self):
        # apelez metoda accelerate
        self.accelerate()
        # apelez metoda stop
        self.stop()


car3 = Car("Spring", 2023, "alb", 15000)

# accesam un atribut de pe obiect
print(car3.model)
print(car3.color, car3.year, car3.price)

print(car3.make)

# atributele setate pe clasa, pot sa fie accesate
# direct de pe numele clasei,
# adica nu avem nevoie de un obiect
print(Car.make)


# definire clasa Complex
class Complex:

    def __init__(self, real, imag):
        self.r = real
        self.i = imag


z = Complex(3.0, -4.5)
print(z.r)
print(z.i)

y = Complex(real=5.0, imag=-3.6)
print(y.r)
print(y.i)

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
