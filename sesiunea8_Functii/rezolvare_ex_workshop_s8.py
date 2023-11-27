"""
REZOLVARE - FUNCTII - EXERCITII WORKSHOP (Sesiunea 8)

! Pentru toate exercițiile. Apelați funcția de cel puțin 2 ori cu valori diferite pentru a testa.
 Dacă funcția are return, printează răspunsul.

Pentru a folosi functiile matematice, puteti pune la inceputul programului:
import math

Iar mai apoi folositi functiile necesare, precum:
math.sqrt(x)  – calculeaza radical din x
math.cos(x) – calculeaza cosinusul lui x
"""
import math

"""
1. Scrieţi o funcţie care primeşte ca parametru lungimea laturii unui pătrat şi returnează aria sa.
"""


def calculeaza_arie_patrat(latura):
    arie = latura * latura
    return arie


print(calculeaza_arie_patrat(2))
print(calculeaza_arie_patrat(5))

"""
2. Scrieţi un subprogram care primeşte ca parametru lungimea laturii unui pătrat
şi returnează atât lungimea diagonalei, cât şi perimetrul pătratului.
"""


def calc_diag_si_perimetru_patrat(latura):

    # varianta 1 pentru calcul diagonala
    # diagonala = math.sqrt(latura**2 + latura**2)

    # varianta 2 pentru calcul diagonala
    diagonala = math.hypot(latura, latura)

    perimetru = latura * 4
    return diagonala, perimetru


print(calc_diag_si_perimetru_patrat(2))
print(calc_diag_si_perimetru_patrat(4))

"""
3. Scrieţi o funcţie care primeşte ca parametri de intrare lungimile celor două catete
ale unui triunghi dreptunghic şi returnează lungimea ipotenuzei.
"""


def calculeaza_ipotenuza(c1, c2):
    ipotenuza = math.hypot(c1, c2)
    return ipotenuza


print(calculeaza_ipotenuza(2, 2))
print(calculeaza_ipotenuza(3, 4))

"""
4. Scrieţi o funcţie care primeşte 3 parametri de tip real, cu semnificaţia de lungimi pentru 3 segmente. 
Funcţia va returna 1 dacă cele trei segmente pot forma un triunghi şi 0, în caz contrar.
"""


def este_triunghi(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0
    if a + b > c and a + c > b and b + c > a:
        return 1
    return 0


print(este_triunghi(3, 4, 5))
print(este_triunghi(4, 3, 7))
print(este_triunghi(-4, 3, 7))
print(este_triunghi(4, 0, 7))
