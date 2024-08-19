
"""
import matplotlib.pyplot as plt

# Datos de los casos de prueba
prioridades = ['Alta', 'Alta', 'Alta', 'Media', 'Media', 'Alta', 'Media', 'Baja', 'Baja', 'Alta']

# Datos de los bugs
criticidades = ['Alta', 'Alta', 'Alta', 'Media', 'Media', 'Alta', 'Media', 'Baja', 'Baja', 'Alta']

# Conteo de prioridades y criticidades
conteo_prioridades = {'Alta': 0, 'Media': 0, 'Baja': 0}
conteo_criticidades = {'Alta': 0, 'Media': 0, 'Baja': 0}

for prioridad in prioridades:
    conteo_prioridades[prioridad] += 1

for criticidad in criticidades:
    conteo_criticidades[criticidad] += 1

# Combinación de los conteos
conteo_combinado = {}
for prioridad, conteo_prioridad in conteo_prioridades.items():
    for criticidad, conteo_criticidad in conteo_criticidades.items():
        conteo_combinado[(prioridad, criticidad)] = conteo_prioridad + conteo_criticidad

# Creación del gráfico de pastel combinado
plt.figure(figsize=(8, 6))
plt.pie(conteo_combinado.values(), labels=conteo_combinado.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Prioridades y Criticidades')
plt.show()
"""
"""
import matplotlib.pyplot as plt

# Datos de la tabla
estados = ['Pasó', 'Pasó', 'Pasó', 'Pasó', 'Pasó', 'Pasó', 'Pasó', 'Pasó', 'Pasó', 'Falló']

# Conteo de casos de prueba en cada estado
conteo_estados = {}
for estado in estados:
    if estado in conteo_estados:
        conteo_estados[estado] += 1
    else:
        conteo_estados[estado] = 1

# Creación del gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(conteo_estados.values(), labels=conteo_estados.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Casos de Prueba por Estado')
plt.show()
"""
"""
import matplotlib.pyplot as plt

# Datos de la tabla
criticidades = ['Alta', 'Alta', 'Alta', 'Baja']

# Conteo de bugs en cada categoría de criticidad
conteo_criticidades = {}
for criticidad in criticidades:
    if criticidad in conteo_criticidades:
        conteo_criticidades[criticidad] += 1
    else:
        conteo_criticidades[criticidad] = 1

# Creación del gráfico de pastel
plt.figure(figsize=(8, 6))
plt.pie(conteo_criticidades.values(), labels=conteo_criticidades.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Criticidades de Bugs')
plt.show()
"""

import matplotlib.pyplot as plt

# Datos
positivos = 5
negativos = 5
aprobados = 9
fallidos = 1
bugs = 4

# Crear el gráfico de dona
labels = ['Casos Positivos', 'Casos Negativos', 'Casos Aprobados', 'Casos Fallidos', 'Bugs Encontrados']
sizes = [positivos, negativos, aprobados, fallidos, bugs]
colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightsalmon', 'lightgrey']

plt.figure(figsize=(8, 6))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140, pctdistance=0.85)
plt.gca().add_artist(plt.Circle((0,0),0.70,fc='white'))
plt.title('Gráfico de Dona')
plt.show()

