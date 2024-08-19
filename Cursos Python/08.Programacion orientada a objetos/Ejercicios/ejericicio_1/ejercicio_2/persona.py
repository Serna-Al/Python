class persona:
    __nombre : str
    __apellido : str
    __edad : int

    def __init__(self, nombre, apellido, edad) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, value):
        self.__nombre = value

    


