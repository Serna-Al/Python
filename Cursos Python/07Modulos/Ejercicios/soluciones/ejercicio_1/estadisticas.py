################### EJERCICIO 1 #####################

# 1.Crea un archivo llamado "matematicas.py" y define una función llamada "calcular_promedio" que reciba una lista de números como argumento y retorne el promedio de los números en la lista.
# 2.Crea otro archivo llamado "estadisticas.py" y importa el módulo "matematicas" con la sentencia "import matematicas"
# 3.Crea una función en el archivo "estadisticas.py" llamada "estadisticas_basicas" que reciba una lista de números como argumento. Dentro de esta función, utiliza la función "calcular_promedio" del módulo "matematicas" para calcular el promedio de los números en la lista.
# 4.Crea un archivo llamado "main.py" e importa el módulo "estadisticas" con la sentencia "import estadisticas"
# 5.Crea una lista de números en el archivo "main.py" y llama a la función "estadisticas_basicas" del módulo "estadisticas" pasando la lista como argumento.
# 6.Imprime el resultado retornado por la función "estadisticas_basicas".

import matematicas

def estadisticas_basicas(numeros : int) -> float:
   return matematicas.calcular_promedio(numeros)
