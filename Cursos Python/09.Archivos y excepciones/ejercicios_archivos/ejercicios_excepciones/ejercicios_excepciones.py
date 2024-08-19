################### EJERCICIOS DE EXCEPCIONES #####################

################### EJERCICIO 1 #####################

# Crea un script que lea un archivo de texto y cuente la cantidad de palabras en él. Utiliza un bloque try-except para manejar el caso en el que el 
# archivo especificado no existe o no se tiene acceso. En caso de que ocurra una excepción, el script debe imprimir un mensaje informando al usuario que el archivo no pudo ser abierto.

nombre_fichero = 'noexiste.txt'

try:
    with open(nombre_fichero) as fichero_abierto:
        contenido = fichero_abierto.read()
        contenido_parseado = contenido.replace('\n',' ')
        lista_palabras = contenido_parseado.split(' ')
        longitud_palabras = len(lista_palabras)
except FileNotFoundError: 
    print("El fichero no existe")
except PermissionError:
    print("El usuario no tiene permiso para abrir el fichero.")

################### EJERCICIO 2 #####################

# Crea un script que solicite al usuario que ingrese un número y luego imprima el resultado de dividir 10 por ese número. Utiliza un bloque try-except para manejar el caso 
# en el que el usuario ingresa un cero o un valor no numérico. En caso de que ocurra una excepción, el script debe imprimir un mensaje informando al usuario que el valor ingresado no es válido.


try: 
    numero = int(input('Introduzca un numero: '))
    resultado = 10 / numero
    print(resultado)
except ZeroDivisionError:
    print('El numero no puede ser 0.')

except ValueError:
    print('El input debe ser un numero.')


################### EJERCICIO 3 #####################

# Crea una clase "CuentaBancaria" que represente una cuenta bancaria con un saldo y un límite de extracción. Agrega un método "extraer" que permita al usuario retirar dinero de la cuenta. 
# Si el usuario intenta extraer más dinero del que tiene disponible en la cuenta (incluyendo el límite de extracción), lanza una excepción "SaldoInsuficiente" con un mensaje que 
# indique al usuario que no tiene suficientes fondos para realizar la transacción.

class SaldoInsuficiente(Exception):
    pass

class CuentaBancaria():
    __saldo : int
    __limite_extraccion : int

    def __init__(self, saldo, limite_extraccion) -> None:
        self.__saldo = saldo
        self.__limite_extraccion = limite_extraccion
    
    def extraer(self, cantidad : int): 
        if cantidad > self.__saldo or cantidad > self.__limite_extraccion:
            raise SaldoInsuficiente('La cantidad que intentas extraer supera tu saldo o el limite de extraccion.')
        else: 
            self.__saldo = self.__saldo - cantidad
            print(f"Acabas de extraer {cantidad}$ y te queda en la cuenta {self.__saldo}$")

cuenta = CuentaBancaria(500, 100)

while True:
    try: 
        dinero_extraer = int(input('Introduzca el saldo que quiere retirar: '))
        cuenta.extraer(dinero_extraer)
    except SaldoInsuficiente as e: 
        print(e)
    except ValueError:
        print('El saldo a extraer debe ser un numero.')

    