"""
Interactiunea cu fisiere - EXERCITII WORKSHOP (Sesiunea 14)
"""

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
programmg_languages = [
    "Python",
    "Java",
    "Javascript",
    "C/C++/C#",
    "PHP",
    "Node.js"
]
with open("hello.txt", mode="w+") as file:
    for p in programmg_languages:
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

words = ["Go", "Kotlin", "Swift"]

with open("hello.txt", mode="a") as file:
    file.write("\n")
    for word in words:
        file.write(word + "\n")

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
