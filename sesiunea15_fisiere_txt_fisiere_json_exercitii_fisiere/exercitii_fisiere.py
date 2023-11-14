"""
Sesiunea 15 - Exercitii fisiere
"""

"""
1. 
a. Create a csv file, called "students.csv" and 
add the following text inside it:

id,fname,lname,age,grade
1,Maria,Popescu,31,7.5
2,Andrei,Ionescu,26,8.0
3,Adriana,Marinescu,21,7.5
4,Matei,Gheorghescu,42,8.5
5,Eusebiu,Pop,33,9.5
6,Ioana,Popa,29,9.0



b. Read the file using Python 'csv' standard library, and display
it in the terminal as a table, using the options
for string formatting from Python:

id	fname		lname		age	grade
---------------------------------------------------
1	Maria		Popescu		31	7.5
2	Andrei		Ionescu		26	8.0
3	Adriana		Marinescu		21	7.5
4	Matei		Gheorghescu	42	8.5
5	Eusebiu		Pop			33	9.5
6	Ioana		Popa			29	9.0
"""

"""
2. Read again the information from the csv file above, store it 
all in a list of data, and then write a new file,
called "students.json", which will contain a valid JSON object.
Use the following format for each student
(and use Python's standard JSON module):

[
	{
		"id": 1,
		"fname": "Maria",
		"lname": "Popescu",
		"age": 31,
		"grade": 7.5	
	},
	...
]

"""

"""
3. 
a. Create a class called Student, based on the data above.
b. Read the JSON file you created, and load all the data into a list
of Student objects.
c. Add a few more Student objects to the list, and then write the new
list in a new JSON file.
"""


import csv
# with open(file="students.csv", mode="w", newline="") as file:
#         w = csv.writer(file)
#         w.writerows([
#                 ["ID", "first name", "last name", "age", "grade"],
#                 [1, "Maria", "Popescu", 31, 7.5],
#                  [2, "Andrei", "Ionescu", 26, 8.0],
#                 [3, "Adriana", "Marinescu", 21, 7.5],
#                 [4, "Matei", "Gheorghescu", 42, 8.5],
#                  [5, "Eusebiu", "Pop", 33, 9.5],
#                 [6, "Ioana", "Popa", 29, 9.0]
#             ])
# with open(file="students.csv", mode="r") as file:
#         r = csv.reader(file)
#         header = next(r)
#         print(f' {header[0]:^6}  {header[1]:<12}  {header[2]:<14}  {header[3]:^6}  {header[4]:^6}')
#         print("----------------------------------------------------------")
#
#         for row in r:


        #print(f' {row[0]:^6}  {row[1]:<12}  {row[2]:<14}  {row[3]:^6}  {row[4]:^6}')
        #
        # Putem formata cum arata diferite variabile incluse intr-un F-string
        # # < --> aliniere la stanga
        # # ^ --> aliniere in centru
        # # > --> aliniere la dreapta
        #
        # # Ex formatare string
        #
        # nume = "Pop"
        # prenume = "Maria"
        # print(f"{nume}-{prenume}-")
        # print(f"{nume:^10}-{prenume:>10}-")

import json
with open(file="students.json", mode="w") as file:
    return json.load(file)

with open("students.csv", mode="r") as csv_file, open("students.json", mode="w") as json_file:
    reader = csv.DictReader(csv_file)  # reader - obiect iterabil
    rows = list(reader)

    json.dump(rows, json_file, indent=4)

with open("students.json",mode="r") as json_file:
    content = json.load(json_file)
    print(content)

# 1. Creare clasa Student
#   - doar constructorul definit cu atributele necesare

# 2. Citim informatiile din fisierul JSON -> o lista cu dictionare
# 3. Iteram prin lista de dictionare
# 4. Luam fiecare dictionar in parte  -> il convertim la un obiect din clasa
# Student
# 5. Acel obiect de tip Student il adaugam intr-o lista cu obiecte tip Student

# 6. cream noi obiecte din clasa Student (2-3)
# 7. Adaugam noile obiecte create in lista cu obiecte tip Student
# 8. Deschidem fisierul JSON in mode w
# 9. Adaugam noua lista de studenti in fisierul JSON (suprascriere)

class Student:
    def __init__(self, ID, firstname, lastname, age, grade):
        self.ID = ID
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.grade = grade

with open(file="students.json", mode="r") as file:
    reader = csv.DictReader(csv_file)
    rows = list(reader)
    for row in rows:
        print(rows)

student1 = Student(ID = 7, firstname= 'Andreea', lastname= 'Ioani', age= 28, grade = 8)
student2 = Student(ID = 8, firstname= 'Mihaela', lastname= 'Bica', age= 27, grade = 9)

with open("students.json",mode="w") as json_file:
    json.dump(rows, json_file, indent=4)


    class Student:
        def __init__(self, student_id, fname, lname, age, grade):
            self.student_id = student_id
            self.fname = fname
            self.lname = lname
            self.age = age
            self.grade = grade


    with open(file="students.json", mode="r") as file:
        students_list = json.load(file)
        print(students_list)

    students_objects = []
    for student_dict in students_list:
        print(student_dict)
        student_obj = Student(
            student_id=student_dict["ID"],
            fname=student_dict['first name'],
            lname=student_dict['last name'],
            age=student_dict['age'],
            grade=student_dict['grade']
        )
        students_objects.append(student_obj)

    print(students_objects)

    student1 = Student(7, "Alex", "Gabor", 33, 7.0)
    student2 = Student(8, "Dumi", "Caslis", 29, 10.0)
    students_objects.append(student1)
    students_objects.append(student2)

    new_students_list = []
    for student_object in students_objects:
        print(student_object)
        student_dict = {
            "ID": student_object.student_id,
            "first name": student_object.fname,
            "last name": student_object.lname,
            "age": student_object.age,
            "grade": student_object.grade
        }
        new_students_list.append(student_dict)

    print(new_students_list)
    with open(file="students.json", mode="w") as file:
        json.dump(new_students_list, file, indent=4)