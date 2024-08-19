############### 1. CREACION DE LISTAS ####################

# 1. Lista vacia
lista_vacia : list = []
lista_vacia : list = list()

# 2. Lista con elementos
motocicletas : list = ['honda','yamaha', 'suzuki','honda']

################ 2. INSERCIONES Y ACTUALIZACIONES #############
motocicletas.append('ducati')
motocicletas.insert(0,'daelin')
motocicletas[1] = 'bmw'
################ 3. BORRADOS ########################
"""""
elemento_cero = motocicletas.pop(0) 
ultimo_elemento = motocicletas.pop()  
motocicletas.remove('Yamaha') 
motocicletas.clear() 
"""

############### 4. SORT ##############
vocales = ['e','i','o','u','a']
vocales.sort() ##Ordena las listas ##
vocales.sort(reverse=True) ## Ordena las listas al reves ##
print(vocales)

############### 5. ACCESO A LAS LISTAS ###################
numeros = [2,3,1,5,4]
primer_elemento = numeros[0]
primeros_elementos = numeros [0:2]
ultimo_elemento = numeros[-1]

todos_elementos = numeros[::1]
numeros_impares = numeros[::2]

########### OTROS METODOS #############

comidas = ['pizza','tacos','kebab']
comidas_copia = comidas.copy()
longitud_comida = len(comidas)
pizza_cuenta = comidas.count('kebab')
