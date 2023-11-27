# lst = ['a', 'b', 'c']
# for x in lst:
#     print(x)
#     # avem 3 iteratii: x = 'a', x = 'b', x = 'c'
#
# print(lst.__iter__())
# print(iter(lst))
#
# nums = [1, 2, 3]
#
# for num in nums:
#     print(num)
#     nums = [1, 2, 3]
#
#     i_nums = iter(nums)
#     print(i_nums)
#     print(next(i_nums))
#     print(next(i_nums))
#     print(next(i_nums))
#     print(next(i_nums))
#     print(next(i_nums))
#     # ITERATORI
#
#     # lst = ['a', 'b', 'c']
#     # for x in lst:
#     #     print(x)
#     #     # avem 3 iteratii: x = 'a', x = 'b', x = 'c'
#     #
#     # print(lst.__iter__())
#     # print(iter(lst))
#
#     # nums este o lista, lista este ITERABILA
#     # nums = [1, 2, 3]
#
#     i_nums = iter(nums)
#     print(i_nums)
#     print(next(i_nums))
#     print(next(i_nums))
#     print(next(i_nums))
#     print(next(i_nums)) # -> error StopIteration
#
#     # print(next(i_nums)) # 1
#     #
#     # for num in i_nums:
#     #     print(num) # 2 3
# """
# EX1: Implementeaza o clasa care sa fie atat iterabila cat si un iterator
# si sa aiba acelasi comportament ca si functia range din Python.
# """
# class MyRangeClass:
#
#     def __init__(self, start, end):
#         self.value = start # 1 2 3 4
#         self.end = end # 4
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # conditie in care sa aruncam exceptia StopIteration
#         if self.value >= self.end:
#             raise StopIteration
#         current_value = self.value # 1 2 3
#         self.value += 1
#         return current_value # 1 2 3
#
#
# for i in MyRangeClass(1, 4):
#     print(i) # 1 2 3
#
#
# def my_gen():
#     n = 1
#     print('This is printed first')
#
#     # Generator function contains yield statements
#     yield n
#
#     n += 1
#     print("This is printed second")
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n
#
# #
# # iterator_obj = my_gen()
# #
# # print(next(iterator_obj))
# # print(next(iterator_obj))
# # print(next(iterator_obj))
# # # print(next(iterator)) # -> error StopIteration
# # print(next(iterator_obj))
# # # GENERATORI
# #
# # def my_gen():
# #     n = 1
# #     print("This is printed first")
# #
# #     yield n
# #
# #     n += 1
# #     print("This is printed second")
# #     yield n
# #
# #     n += 1
# #     print("This is printed last")
# #     yield n
# #
# # iterator_obj = my_gen()
# #
# # print(next(iterator_obj))
# # print(next(iterator_obj))
# # print(next(iterator_obj))
# # # print(next(iterator_obj)) # -> error StopIteration
# #
# # for number in my_gen():
# #     print(number)
# #
# # def my_gen2(end):
# #     n = 1
# #     while n < end:
# #         yield n
# #         n += 1
# # for i in my_gen():
# #     print(i)
#
# """
# EX2: Creeaza un generator care face acelasi lucru ca si clasa MyRange
# implementata la exercitiul anterior.
# """
#
# def my_range_gen(start, end):
#     n = start
#     while n < end:
#         yield n
#         n += 1
# """
# EX3: Implementeaza un generator de numere pare care ne va da acces la toate
# numerele pare pana la un numar maxim luat ca si parametru.
# """
#
# #solution 1
# def get_even_numbers(end):
#     n = 0
#     while n < end:
#         if n % 2 == 0:
#             yield n
#         n += 1
#
# # solution 2
# def get_even_numbers(end):
#     n = 0
#     while n < end:
#         yield n
#         n += 2
#
# for j in get_even_numbers(10):
#     print(j)
# """
# EX2: Creeaza un generator care face acelasi lucru ca si
# clasa MyRangeClass
# implementata la exercitiul anterior.
# """
#
# def my_range_gen(start, end):
#     n = start
#     while n < end:
#         yield n
#         n += 1
#
# for i in my_range_gen(1, 4):
#     print(i)
# #CONTEXT MANAGERS
#
# with open("exemplu.txt", mode="w") as file:
#     file.write("Hello")
#
# with File("exemplu.txt", mode="w") as file:
#     file.write("Hello")
#
# class File:
#
#     def __init__(self, file_name, method):
#         self.file_obj = open(file_name, method)
#
#     def __enter__(self):
#         # logica care este folosita in momentul
#         # in care se intra in blocul with
#         return self.file_obj
#
#     def __exit__(self, type, value, traceback):
#         # logica care este folosita in momentul
#         # in care se iese din blocul with
#         self.file_obj.close()

# with File("exemplu.txt", method="w") as file:
#     file.write("Hello")
#
#     import time
#
#     start_time = time.time()
#     print(start_time)
#
#     end_time = time.time()
#     print(end_time - start_time)
#
#     with Timer():

# 1.	Iterators

# # Implementati un iterator numit ReverseIterator, care parcurge o colectie in sens opus. Exemplu de folosire:
# Exemplu de folosire:

note = [3, 7, 5, 8, 10]
rev_it = ReverseIterator(note)
print(next(rev_it))  # printeaza 10
print(next(rev_it))  # printeaza 8
print(next(rev_it))  # printeaza 5
s.a.m.d


note = [3, 7, 5, 8, 10]
my_grades_reversed = list(reversed(note))
print(my_grades_reversed)

print(list(my_grades_reversed))
print(next(my_grades_reversed))
print(next(my_grades_reversed))
print(next(my_grades_reversed))
print(next(my_grades_reversed))
print(next(my_grades_reversed))

for nota in my_grades_reversed:
    print(nota)
    print(iter(note))
# 2.	Generators
#
# Implementați un generator pentru loteria 6/49 și noroc:
# -	Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv)
# -	Ultima apelare va da un singur număr de “noroc” format din 7 cifre

