"""
INTERACTIUNEA CU FISIERE
"""

# # creare fisier nou numit "dummy.txt"
# fisier_nou = open(file="dummy.txt", mode="w")
#
# # putem folosi metoda write pentru a adauga continut
# # in fisierul text deschis in mode-ul write
# # metoda write primeste ca parametru un string care va
# # contine tot textul ce dorim sa il adaugam
# # fisier_nou.write("Hello world\nHello world\nHello world\nHello world\nHello worldHello worldHello worldHello worldHello world")
#
#
# fisier_nou.writelines(["hello world\n", "hello there\n", "new line\n"])
# fisier_nou.close()
#
# # creare fisier intr-un folder existent
# # la acelasi nivel cu fisierul curent python
# fisier_nou2 = open(file="fisiere_text/cats.txt", mode="w")
#
# fisier_nou2.write("Hello cats!")
#
# fisier_nou2.close()


# blocul with
# with open(file="dummy.txt", mode="w") as fisier_nou:
#     fisier_nou.writelines(["hello world\n", "hello there\n"])
# print("hi")
#
#
# def scriere_in_fisier_txt(calea_fisier, informatii_as_list):
#     with open(calea_fisier, mode="w") as file:
#
#         # daca am deschis fisierul in modul "w",
#         # atunci vom putea doar sa scriem informatii in acesta.
#         # nu sunt permise alte operatii, cum ar fi citirea din fisier
#
#         # daca incercam sa citim continutul fisierului cand acesta
#         # a fost deschis in modul "w", vom obtine o eroare
#         # de tip UnsupportedOperation
#         # file.read()
#         file.writelines(informatii_as_list)
#
# scriere_in_fisier_txt("dummy.txt", ["Informatii\n", "noi\n"])
# scriere_in_fisier_txt("fisiere_text/cats.txt", ["Cat1\n", "Cat2\n"])
#
# with open("dummy.txt", mode="r") as f:
#     # metoda read() citeste si returneaza tot
#     # continutul din fisier sub forma de string
#     content = f.read()
#     print(content)
#     print(type(content)) # str

    # in momentul in care citim continutul dintr-un fisier,
    # indiferent de metoda aleasa pentru a citi informatiile,
    # se va retine unde s-a ramas cu citirea.

    # pentru ca am apelat mai sus metoda read() care imi returneaza
    # tot continutul din fisierul deschis, mai apoi,
    # indiferent de ce alte metode mai apelez pentru a citi informatii,
    # acestea nu o sa mai returneze nimic
#     print(f.readlines())
#
# with open("dummy.txt", mode="r") as f:
#
#     # metoda readlines() o folosim pentru
#     # a citi informatii dintr-un fisier si a le primi
#     # sub forma de lista (in care fiecare element este
#     # o linie din fisierul txt, sub forma de string)
#     print(f.readlines())

    # similar cu situatia din blocul with de mai sus,
    # deja s-a citit tot continutul din fisier,
    # astfel ca, indiferent de metoda folosita pentru citire,
    # nu mai sunt linii de citit din fisier si de returnat

    # in cazul nostru, metoda readline() a returnat un string gol
#     print(f.readline())
#
# with open(file="dummy.txt", mode="r") as f:
#     print(f.readline())
#     print(f.readline())
#
# with open(file="dummy.txt", mode="r") as f:
#     lines = f.readlines()
#     print(lines)

    # daca incercam sa scriem intr-un fisier
    # deschis in modul "r", vom avea eroare UnsupportedOperation
    # f.write("ceva") # -> Eroare
    # for line in lines:
    #     # procesam/interactionam/facem verificari pentru fiecare linie
    #     if len(line) == 4:
    #         print(line)

# TODO: Exploreaza si modul de deschidere append (mode="a")


"""
1. Create a text file called “hello.txt” and add the following text inside of it:
Python                                                                                              
Java
Javascript                                                                                              
C/C++/C#
PHP
Node.js
Write a short program to read and display the text file
"""

programming_languages = [
    "Python"
    "Java"
    "Javascript"                                                                                              
    "C/C++/C#"
    "PHP"
    "Node.js"
]

with open("hello.txt", mode="w+") as file:
    for p in programming_languages:
        file.write(p + "\n")
with open("hello.txt", mode="r") as file:
    text = file.read()
    print(text)

"""
2.
Write a short program to append the following lines to “hello.txt” (you will use a list of strings and a for-loop):
Go                                                                                              
Kotlin
Swift
Display the new contents of the file.
"""

words = ["Go","Kotlin", "Swift"]
with open("hello.txt", mode="a") as file:
    file.write("\n")
    for word in words:
        file.write(word +"\n")

with open("hello.txt", mode="r") as file:
    text = file.read()
    print(text)

"""
4. Write a short program that reads the “hello.txt” file and 
displays every other line (only odd lines).
"""

with open("hello.txt", mode="r") as f:
    lines = f.readlines()
    for i in range(0, len(lines), 2):
        print(lines[i])

"""
5.
Write a program that generates 26 text files, called `A.txt`, `B.txt`, … `Z.txt`. 
Each file will contain the sentences below:
My name is letter X.
I am the 24th letter of the alphabet.
Make sure you use the correct ending for the letter’s number.
(e.g. 1st, 2nd, 3rd, etc.)
"""
import string
# loop through all the uppercase letters in the alphabet
for letter in string.ascii_uppercase:
    # get the index of the letter in the alphabet (0-25)
    index = ord(letter) - ord('A')
    # calculate the ordinal number of the letter
    if index == 0:
        ordinal = '1st'
    elif index == 1:
        ordinal = '2nd'
    elif index == 2:
        ordinal = '3rd'
    else:
        ordinal = f"{index+1}th"
    # create the file name and open the file
    file_name = f"{letter}.txt"
    with open(file_name, 'w') as file:
        # write the sentences to the file
        file.write(f"My name is letter {letter}.\n")
        file.write(f"I am the {ordinal} letter of the alphabet.\n")





