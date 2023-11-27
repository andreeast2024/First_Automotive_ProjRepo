"""
Singleton Design Pattern
"""
# ne permite sa gestionam numarul de obiecte
#care poate fi creat dintr-o clasa,
#astfel incat, de-a lungul programului,
#nu vom putea avea mai mult de o instanta a clasei respective

class SingletonClass:
    __instance = None
    sector = "IT"


    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


obj1 = SingletonClass("JavaScript")
obj2 = SingletonClass(name="Python")
print(obj1)
print(id(obj1))

print(obj2)
print(id(obj2))
print(obj1 is obj2)

print(__name__)

if __name__ == '__main__':
    print("fisierul este rulat ca modul de sine statator")
    print(obj1)
    print(id(obj1))

    print(obj2)
    print(id(obj2))
    print(obj1 is obj2)

    print(__name__)
else:
    print("fisierul a fost importat doar")


