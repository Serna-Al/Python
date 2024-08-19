from vehiculo import vehiculo

class concesionaria:
    __inventario : list

    def __init__(self) -> None:
        self.__inventario = []

    def get_inventario(self):
        return self.__inventario.copy()

    def agregar_vehiculo(self, vehiculo_nuevo : vehiculo) -> None:
        self.__inventario.append(vehiculo_nuevo)

    def listar_vehiculo(self) -> None:
        for vehiculo in self.__inventario:
            print(f'Este vehiculo es de la marca {vehiculo.get_marca()}')
            print(f'Este vehiculo es el modelo {vehiculo.get_modelo()}')

