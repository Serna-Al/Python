### TIPOS DE DATOS BASICOS ###

#Numeros (Entero, float, complejo))

contador : int = 0
numero_pi : float = 3,14
imaginario : complex = -5j 

#Booleanos

es_verdad : bool = True
es_mentira : bool = False
#String o cadenas de texto
mi_nombre = 'Mi nombre Alberto.'

##OPERADORES ARITMETICOS##

suma = 1 +1 
resta = 1-1
multiplicacion = 10 * 10
division = 18 / 5 ## Devuelve resultado con decimales##
division_sin_decimales = 18 // 5 ##Devuelve resultado sin decimales##
modulo = 18 % 5 ##Devuelve el restante de la division##
potencia = 2 ** 3

## OPERADORES RELACIONALES ##

mayor_que = 2 > 1
print(mayor_que) ##Depende de la funcion bool##
menor_que = 1 < 0
mayor_igual = 1>= 2
menor_igual = 1 <= 2
distinto_que = 1 != 2

### OPERADORES LOGICOS ### 

and_operacion = True and False 
or_operacion = True or False
not_operacion = not False

### OPERACIONES DE PERTENENCIA ###

in_operacion = 'hola' in 'hola mundo' 
not_in_operacion = 'adios' not in 'hola mundo' ##Estas operaciones devuelven un bool##

### OPERADORES DE IDENTIDAD ###

x = 1
y =x

is_operacion = x is y
not_is_operacion = x is y
