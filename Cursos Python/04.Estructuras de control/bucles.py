######### BUCLES FOR IN ##############

numeros = list(range(0,11))
numeros_copia = []
for numero in numeros:
    numeros_copia.append(numero+1)


lista_palabras = ['r2d2.coder', 'instragram', 'tiktok']
for palabra in lista_palabras:

############ BUCLES WHILE ############
     
 suma = 50

while suma > 0:
     suma = suma - 1
    

############ SENTENCIAS BREAK, PASS Y CONTINUE #############
     
suma = 50 
     #Break: Detiene la ejecucion del bucle.
while suma > 0:
     suma = suma -1
     print(suma)
     if suma == 20:
       break


#Pass: Se utiliza para dejar vacio un trozo de codigo que todavia no queremos especificar.
numeros = list(range(0,1000))
for numero in numeros:
   pass

print('hola mundo')

#Continue: Pasa a la siguiente iteracion del bucle.
suma = 50

while suma > 0:
   suma = suma -1 
   if suma % 2 != 0:
       continue
   else:
      print(suma)
       



