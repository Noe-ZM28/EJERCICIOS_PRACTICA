# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# Desarrollar un programa que muestre en pantalla los números del 1 al 100.
# Sustituir los múltiplos de 3 por la palabra “Fizz”
# Sustituir los múltiplos de 5 por “Buzz”
# Sustituir los múltiplos de ambos por la palabra “FizzBuzz”.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def FizzBuzz(limite:int = 100) -> None:
    """
    Muestra en consola los números del 1 al límite ingresado.
    - En caso de ser multiplo de 3 imprime 'Fizz'.
    - En caso de ser multiplo de 5, imprime '“Buzz”.
    - En caso de ser multiplo de 15, imprime '“FizzBuzz”.

    Si no se ingresa un número, el límite por defecto es 100.

    Params:
        - limite (int): Parametro para indicar el limite de números a mostrar.
    Return:
        - None
    Raises:
        - None
    """

    for i in range(1, limite + 1, 1):

        if i % 15 == 0: i = f'{i} -> FizzBuzz'
        elif i % 3 == 0: i = f'{i} -> Fizz'
        elif i % 5 == 0: i = f'{i} -> Buzz'

        print(i)

FizzBuzz(1000)
