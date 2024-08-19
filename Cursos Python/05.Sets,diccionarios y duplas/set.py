############################# CREACION DE SET #############################
# 1. Set vacio
nuevo_set = set()

# 2. Inicializar un set con elementos
nuevo_set = {'uno','dos'}


# 2. Insertar y actualizar
nuevo_set.add('tres')
nuevo_set.update({'tres','cuatro'})
print(nuevo_set)

############################# 3. BORRADOS #############################
nuevo_set.discard('cinco')
nuevo_set.remove('uno')
nuevo_set.clear()

############################# 4. OPERACIONES DE SETS #############################
set_uno = {1,2,3,4}
set_dos = {5,6,7,8}

set_diferencia = set_uno.difference(set_dos)
set_diferencia_simetrica = set_uno.symmetric_difference(set_dos)
set_interseccion = set_uno.intersection(set_dos)
set_union = set_uno.union(set_dos)


############################# 5. OTROS METODOS #############################
no_tiene_interseccion = set_uno.isdisjoint(set_dos)
es_subconjunto = set_dos.issubset(set_uno)
es_superconjunto = set_uno.issuperset(set_dos)
print(set_union)

############################# 6. ACCESO A LOS SETS #############################
 
 #No hay forma de acceder a un conjunto indexado

for numero in set_uno:
    print(numero)