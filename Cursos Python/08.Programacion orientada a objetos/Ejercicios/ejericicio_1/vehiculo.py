class vehiculo:
    def __init__(self, marca, modelo, año, color) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__color = color

    def get_marca(self):
        return self.__marca

    def set_marca(self, value):
        self.__marca = value

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, value):
        self.__modelo = value

    def get_año(self):
        return self.__año

    def set_año(self, value):
        self.__año = value

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value

    def encender(self):
        print('El vehículo ha sido encendido')

    def apagar(self):
        print('El vehículo ha sido apagado')



        
