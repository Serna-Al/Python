# 1. Longitud de un string
saludo = 'hola mundo'
longitud_saludo = len(saludo)

# 2. Quitar espacios en blanco al principio y al final

string_espacios = '              esto es un spring            '
string_sin_espacios = string_espacios.strip()
print(string_sin_espacios)

# 3. Reemplazar partes de un string por otro.
mensaje_cifrado = 'PEESTOPEESPEUNPEMENSAJEPECIFRADO'
mensaje_descifrado = mensaje_cifrado.replace('PE',' ')
print(mensaje_descifrado)

# 4. Poner un string en mayusculas o minusculas.
minuscula = 'vamos a gritar un poco'
grito = minuscula.upper()
print(grito)

mayuscula = 'hablemos mas bajito'
susurro = mayuscula.lower()
print(susurro)

# 5. Comprobar si un string tiene prefijos o sufijos
url = 'www.r2d2.com'

prefijo = url.startswith('www')
sufijo = url.endswith('.com')

print(prefijo)
print(sufijo)
# 6. Encontrar la aparicion de caracteres dentro de un string 
indice = url.find('r2d2')
print(indice)

# 7. Contaminacion de strings y f-strings

nombre ="Alberto"
edad = 24
cargo = 'Ingeniero'

saludo = 'Mi nombre es ' + nombre + ' tengo una edad de ' + str(edad) + 'y soy ' + cargo
saludo_2 = f'Mi nombre es {nombre} tengo una edad de {edad} y soy {cargo}'
print(saludo_2)