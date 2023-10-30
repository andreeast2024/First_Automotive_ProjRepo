"""
REZOLVARE FUNCTII - EXERCITII WORKSHOP (Sesiunea 8)
"""

"""
Pentru toate exercitiile -apelati functia de cel putin 2 ori cu valori diferite
pentru a testa.
Daca funcția are return, printeaza raspunsul.                        
"""

"""
1.Functie care sa calculeze si sa returneze suma a doua numere.
"""


# definim o functie, numita calculate_sum, care ia doi parametri numiti a si b
def calculate_sum(a, b):
    # returnam rezultatul adunarii celor doi parametri
    # luati de functie, a si b
    return a + b


# invocam/apelam functia calculate_sum, cu argumentele 0 si 35
# adica dam valori pentru parametrii a si b.
# a va lua valoarea 0
# b va lua valoarea 35
print(calculate_sum(0, 35))

# invocam/apelam functia calculate_sum, cu argumentele 3 si 4
# adica dam valori pentru parametrii a si b si printam direct rezultatul.
# a va lua valoarea 3
# b va lua valoarea 4
print(calculate_sum(3, 4))


"""
2. Functie care sa returneze TRUE daca un numar este par, FALSE pentru impar
"""


# varianta 1
# definim o functie, numita, is_even, care ia un parametru numit number
def is_even(number):
    # verificam daca parametrul number este par
    if number % 2 == 0:
        # daca da, returnam True
        return True
    # daca nu, returnam False
    return False
# OBSERVATIE: daca se va intra in if (adica daca numarul este par), codul de dupa "return True"
# nu se va mai executa, si astfel putem sa ne lipsim de cuvantul cheie "else"


# varianta 2
# definim o functie, numita is_even, care ia un parametru numit number
# def is_even(number):
#     # vom returna direct rezultatul expresiei "number % 2 == 0"
#     return number % 2 == 0

# invocam/apelam functia is_even, cu argumentul 23
# adica dam valoare pentru parametrul number si printam direct rezultatul functiei apelate.
# number va lua valoarea 23.
print(is_even(23))

# invocam/apelam functia is_even, cu argumentul 12
# adica dam valoare pentru parametrul number si printam direct rezultatul functiei apelate.
# number va lua valoarea 12.
print(is_even(12))


"""
3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu)
"""


# definim o functie, numita count_chars, care ia 3 parametri numiti
# nume, prenume si nume_mijlociu
def count_chars(nume, prenume, nume_mijlociu):
    # functia va returna suma lungimilor parametrilor nume, prenume si nume_mijlociu
    return len(nume) + len(prenume) + len(nume_mijlociu)


# invocam/apelam functia count_chars, cu argumentele "Popa", "Ana" si "Maria"
# adica dam valori pentru parametri nume, prenume si nume_mijlociu
# si printam direct rezultatul functiei apelate.
# nume va lua valoarea "Popa"
# prenume va lua valoarea "Ana"
# nume_mijlociu va lua valoarea "Maria"
print(count_chars("Popa", "Ana", "Maria"))

# invocam/apelam functia count_chars, cu argumentele "Marinescu", "Ion" si "Viorel"
# adica dam valori pentru parametri nume, prenume si nume_mijlociu
# si printam direct rezultatul functiei apelate.
# nume va lua valoarea "Marinescu"
# prenume va lua valoarea "Ion"
# nume_mijlociu va lua valoarea "Viorel"
print(count_chars("Marinescu", "Ion", "Viorel"))


"""
4. Scrieti o functie care returneaza prima cifra a unui numar natural.
De exemplu, daca parametrul efectiv este 127,
functia va returna 1.
"""


# definim o functie numita get_first_digit, care va lua un parametru, number.
def get_first_digit(number):
    # pentru a lua prima cifra dintr-un numar natural (pozitiv),
    # putem converti acel numar la string, si apoi sa accesam prima cifra/caracter
    # folosindu-ne de index.
    # mai apoi, pentru a returna tot un numar/cifra, si nu un caracter, va trebui
    # sa facem conversia acelei cifre din format string in int si sa returnam rezultatul.
    number_as_str = str(number)
    first_digit_as_str = number_as_str[0]
    first_digit = int(first_digit_as_str)
    return first_digit


# apelam/invocam functia get_first_digit, cu argumentul 127
# ceea ce inseamna ca dam valoarea 127 pentru parametrul number
# si afisam direct rezultatul returnat de functia apelata
print(get_first_digit(127))


# apelam/invocam functia get_first_digit, cu argumentul 12745
# ceea ce inseamna ca dam valoarea 12745 pentru parametrul number
# si afisam direct rezultatul returnat de functia apelata
print(get_first_digit(12745))


"""
5. Sa se tipareasca toate numerele prime aflate intre doi intregi cititi.
Programul va folosi o functie care testeaza daca un numar este prim sau nu.
"""

# numar prim = numar care este divizibil/se imparte exact doar cu 1 si el insusi


# definim o functie, numita get_prime_numbers, care ia doi parametri: start si end
def get_prime_numbers(start, end):
    # iteram prin numerele din intervalul start, end + 1
    for number in range(start, end + 1):

        # pentru a verifica daca numarul "number" este prim,
        # trebuie sa verificam ca acesta se divide doar cu 1 si cu el insusi.
        # altfel spus, putem verifica ca numarul nu se divide cu oricare numar > 1 si < decat el insusi

        # pentru asta, parcurgem numerele din intervalul 2 (inclusiv) si number (exclusiv -> deci number - 1)
        for i in range(2, number):
            # verificam daca number este divizibil cu i
            if number % i == 0:
                # daca da, inseamna ca numarul "number" nu este prim
                # si atunci nu mai are rost sa continuam iterarea, ci putem
                # intrerupe ciclul repetitiv
                break
        else:
            # blocul else atasat unui for loop se executa doar daca
            # ciclul repetitiv la care este atasat nu a fost intrerupt fortat
            # adica a ajuns la final.
            # In cazul nostru, ciclu repetitv nu este intrerupt fortat doar
            # daca numarul "number" este prim
            # si astfel, in blocul else, putem afisa mesajul sugestiv cum ca
            # "number" este intr-adevar prim.
            print(f"Numarul {number} este prim.")


print(get_prime_numbers(1, 25))

"""
6. Scrieti un program care tipareste numerele intregi gasite intre doua valori citite,
numere care se divid cu suma cifrelor lor.
Programul va utiliza o functie care returneaza suma cifrelor unui numar intreg primit ca parametru.
"""


def is_div_by_digit_sum(start, end):
    # parcurgem toate numerele din intervalul start si end
    for number in range(start, end + 1):
        # calculam suma cifrelor numarului curent

        # definim o variabila, digits_sum, in care sa salvam,
        # suma tuturor cifrelor din numarul curent "number"
        digits_sum = 0

        # vom folosi un while pentru a lua fiecare cifra
        # in parte din "number" si a o adauga la suma

        # ca sa facem asta, va trebui sa prelucram o copie
        # a variabilei number, pentru ca se va modifica
        # iar cand iesim din while, avem nevoie de number nemodificat
        # pentru a face compararea
        number_copy = number
        while number_copy > 0:
            # pentru a lua ultima cifra dintr-un numar
            # putem sa calculam modulus 10 (restul impartirii la 10)
            # ex:  23 % 10 = 3; 145 % 10 = 5
            # adaugam ultima cifra in suma digits_sum
            ultima_cifra = number_copy % 10
            digits_sum += ultima_cifra

            # mai apoi, pentru a elimina ultima cifra din number,
            # avand in vedere ca deja am adunat-o in digits_sum,
            # putem suprascrie valoarea lui number_copy cu "number_copy // 10"

            # ne aducem aminte ca // semnifica operatia de floor division
            # care face impartirea si rotunjeste rezultatul fata de cel mai apropiat
            # intreg, astfel incat rezultatul rotunjit <= intregul rezultatului
            # exemplu: 23 // 10 = 2; 145 // 10 = 14

            # aceasta este de asemenea, si conditia de iesire din while
            number_copy = number_copy // 10

        if number % digits_sum == 0:
            print(number)


is_div_by_digit_sum(1, 40)


