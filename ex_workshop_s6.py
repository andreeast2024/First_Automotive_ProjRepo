"""
CICLURI REPETITIVE - EXERCITII WORKSHOP (Sesiunea 6)
"""

"""
1. Avand lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Foloseste un for ca sa interezi prin toata lista si sa afisezi 'Masina mea preferata este x':

a. Fa acelasi lucru cu un for each.
b. Fa acelasi lucru cu un while.
"""

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masina_preferata = input("Masina preferata este: ")
for masina in masini:
    if masina != masina_preferata:
        print(f"Masina ta preferata este {masina_preferata}")
        continue
    else:
        print(f"Masina nu se afla in lista")
"""
2. Folosind aceeasi lista ca la exercitiul 1:

- foloseste un for else:
    - in for: modifica elementele din lista astfel incat sa fie scrise cu majuscule,
    exceptand primul si ultimul.
    - in else: printeaza lista
"""

"""
3. Folosind aceeasi lista ca la exercitiul 1:
Vine un cumparator care doreste sa cumpere Mercedes.
Itereaza prin lista cu masini prin modalitatea aleasa de tine.
Daca masina e 'Mercedes':
- printeaza 'Am gasit masina dorita de dvs'
- iesi din ciclu folosind un cuvant cheie care face acest lucru
altfel:
- printeaza 'Am gasit masina X. Mai cautam.'
"""

"""
4. Folosind aceeasi lista ca la exercitiul 1:
Vine un cumparator bogat dar indecis.
Ii vom prezenta toate masinile, cu exceptia Trabant si Lastun.
Daca masina e Trabant sau Lastun:
- Foloseste un cuvant cheie sa dea skip la ce urmeaza (nu trebuie else)
- Printeaza "S-ar putea sa va placa masina X".
"""
