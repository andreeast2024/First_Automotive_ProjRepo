# functie simpla -> nu are parametri si nu returneaza nimic
def first_function():
    print("Hello World!")

    # FUNCTII

    # def function_name(parameters):
    #     # function body
    #     pass

    # functie simpla -> nu are parametri si nu returneaza nimic
    # definirea functiei
    def first_function():
        print("Hello World!")

    # apelarea/invocarea functiei
    first_function()
    first_function()
    first_function()
    first_function()
    first_function()

    """
    EX1: Defineste o functie care printeaza, pe rand,
    primele 10 numere (1, 10).
    """

    def get_ten_numbers():
        for num in range(1, 11):
            print(num)

    get_ten_numbers()

    def process_list(lista):
        pass

    process_list([1,2,3,5])