import matplotlib.pyplot as plt

# Datos de la tabla
ids_bug = ['BUG004', 'BUG001', 'BUG002', 'BUG003']
criticidades = ['Crítica', 'Alta', 'Alta', 'Media']

# Conteo de defectos por criticidad
conteo_criticidades = {'Crítica': 0, 'Alta': 0, 'Media': 0}
for criticidad in criticidades:
    conteo_criticidades[criticidad] += 1

# Creación del gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(conteo_criticidades.keys(), conteo_criticidades.values(), color=['red', 'orange', 'blue'])
plt.title('Cantidad de Defectos por Criticidad')
plt.xlabel('Criticidad')
plt.ylabel('Cantidad de Defectos')
plt.show()
