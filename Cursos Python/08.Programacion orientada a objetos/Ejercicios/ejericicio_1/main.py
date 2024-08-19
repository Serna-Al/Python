from concesionaria import concesionaria, vehiculo

concesionaria_uno = concesionaria()
bmw = vehiculo('bmw','X4', 2020,'negro')
ferrari = vehiculo('ferrari','el mejor',2023,'rojo')

concesionaria_uno.agregar_vehiculo(bmw)
concesionaria_uno.agregar_vehiculo(ferrari)

concesionaria_uno.listar_vehiculo()