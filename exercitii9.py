#5. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.

def get_positive_numbers(lista):
    lista_nr_pozitive = []
    for numar in lista:

        if numar > 0:
            lista_nr_pozitive.append(numar)

    return lista_nr_pozitive
print(get_positive_numbers([-1,7,-6,9]))

