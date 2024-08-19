import matplotlib.pyplot as plt

# Datos de la tabla
problemas = ['Registro - Usuario/Contraseña', 'Funcionalidades de cartelera', 'Reserva de boletos',
             'Funcionalidades de Alimentos', 'Actualización de datos de usuario',
             'Registro - Correo/Telefónico duplicado', 'Ingreso de datos inválidos al iniciar sesión',
             'Búsqueda de películas no existentes', 'Selección de cine con ubicación errónea',
             'Interrupción del proceso de reserva']
prioridades = ['Alta', 'Media', 'Alta', 'Media', 'Media', 'Alta', 'Media', 'Baja', 'Baja', 'Alta']

# Conteo de problemas por prioridad
conteo_prioridades = {'Alta': 0, 'Media': 0, 'Baja': 0}
for prioridad in prioridades:
    conteo_prioridades[prioridad] += 1

# Creación del gráfico de barras
plt.figure(figsize=(8, 6))
plt.bar(conteo_prioridades.keys(), conteo_prioridades.values(), color=['red', 'orange', 'green'])
plt.title('Distribución de Prioridades de Problemas Identificados')
plt.xlabel('Prioridad')
plt.ylabel('Cantidad de Casos de Prueba')
plt.show()