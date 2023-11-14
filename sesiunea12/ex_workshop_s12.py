# """
# 1. Defineste o clasa abstracta FormaGeometrica:
#
# - Conține un field PI=3.14 (atribut pe clasa)
# - Conține o metodă abstractă aria
# - Conține o metodă a clasei descrie()
#     - aceasta printează pe ecran ‘Cel mai probabil am colturi’
# """
# from abc import ABC, abstractmethod
#
# class FormaGeometrica(ABC):
#     PI = 3.14
#     @abstractmethod
#     def aria(self):
#         pass
#     @classmethod
#     def describe(cls):
#         print("Cel mai probabil am colturi")
#
#
#
#
#
#
#
# """
# 2. Defineste o clasa Patrat, care mosteneste FormaGeometrica
#
# - In constructor, defineste atributul latura
#     - latura este proprietate privata
#     - implementeaza getter, setter, deleter pentru latura
# - Implementeaza metoda ceruta de interfața
# """
# class Patrat(FormaGeometrica):
#
#     def __init__(self, latura):
#         self.__latura = latura
#
#     @property
#     def latura(self):
#         return self.__latura
#     @latura.setter
#     def latura(self, new_latura):
#         if new_latura > 0:
#             self.__latura = new_latura
#         else:
#              print(f"Setter: Noua valoare este {new_latura}")
#
#     @latura.deleter
#     def latura (self):
#       del self.__latura
#     def aria(self):
#         return (self.latura ** 2)
#
# patrat = Patrat( latura = 5)
# print("Latura patratului:", patrat.latura)
# print("Aria patratului: ", patrat.aria())
#
#
#
# """
# 3. Defineste o clasa Cerc, care mosteneste FormaGeometrica
#
# - In constructor, defineste atributul raza
#     - raza este proprietate privata
#     - implementează getter, setter, deleter pentru rază
# - Implementeaza metoda ceruta de interfata - în calcul foloseste field PI
# mostenit din clasa parinte
# - Defineste metoda descrie() in clasa Cerc - printeaza ‘Eu nu am colturi’
# """
# class Cerc(FormaGeometrica):
#     def __init__(self, raza):
#         self.__raza = raza
#
#     @property
#     def raza(self):
#         return self.__raza
#
#     @raza.setter
#     def raza(self, new_raza):
#         if new_raza> 0:
#             self.__raza = new_raza
#         else:
#             print(f"Setter: Noua valoare este {new_raza}")
#
#     @raza.deleter
#     def raza(self):
#         del self.__raza
#
#     def aria(self):
#         return self.PI * self.raza ** 2
#
#         def describe(self):
#             print("Eu nu am colturi")
#
# cerc = Cerc(raza = 5)
# print("Raza cercului :", cerc.raza)
# print("Aria cercului: ", cerc.aria())
# cerc.describe()
#
#
# """
# 4. Creeaza un obiect de tip Patrat si joaca-te cu metodele lui
# Creeaza un obiect de tip Cerc si joaca-te cu metodele lui
# """
# patrat1 = Patrat(latura = 8)
# print(patrat1.aria())
# cerc1 = Cerc(raza = 9)
# print(cerc1.aria())


"""
EX5: Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""
from abc import ABC, abstractmethod

class AbstractVideo(ABC):
    @abstractmethod
    def show_details(self):
        pass

    def play(self):
    print("Video is playing")




"""
EX6: Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""

class Videoclip(AbstractVideo):
    @abstractmethod
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        pass

    @classmethod
    def show_details(cls):

        print("{self.title} has a duration of {self.duration} minutes")

videoclip = Videoclip(title = "Smiley", duration = 5)
print(videoclip.title)
print(videoclip.duration)


"""
EX7:
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""
#a.
class Movie(Videoclip):
    def __init__(self, genre, director, actors):
        self.genre = genre
        self.__director = director
        self.actors = actors
#b.
movie = Movie(genre = "comedy", director = "Sam", actors = "Tom Hardy, Alicia Sylverstone")
print(movie.genre)
print(movie.actors)

print(" Is directed by {self.director} and the actors are  {self.actors} ")

#c.
super.__init__(self, genre, director,actors)
@property
    def director(self):
        print("Getter")
        return self.__director


    @director.setter

    def director(self, new_director):
        print("Setter")

        self.__director = new_director


    @director.deleter
    def director(self):
    print("Deleter")
    self.__director = None











