from mascota import Mascota

# Sintaxis:
# class Hijo(clase_padre1, clase_padre2, clase_padre3):
#
#   Atributos clase hija
#
#   def __init__(self, atributos):
#       super().__init__(atributos_padre)
#       asignación atributos clase hija
#
#   Getters y setters de atributos de la clase hija
#
#   Metodos de la clase hija y metodos sobrecargados


class Perro(Mascota):
    __color_pelo: str
    __raza: str
    __trofeos_ganados: dict

    def __init__(self, nombre, puntos_salud, nivel, edad, color_pelo, raza):
        super().__init__(nombre, puntos_salud, nivel, edad)
        self.__color_pelo = color_pelo
        self.__raza = raza
        self.__trofeos_ganados = {
            'Internacional': 0, 'Nacional': 0, 'Regional': 0
        }

    def get_color_pelo(self) -> str:
        return self.__color_pelo

    def set_color_pelo(self, value):
        self.__color_pelo = value

    def get_raza(self) -> str:
        return self.__raza

    def set_raza(self, value):
        self.__raza = value

    def get_trofeos_ganados(self) -> dict:
        return self.__trofeos_ganados.copy()

    def set_trofeos_ganados(self, value):
        self.__trofeos_ganados = value.copy()

    # Sobreescritura del método ganar_torneo, utilizamos la funcionalidad del padre y la extendemos para que la clase Perro pueda guardar
    # los torneos ganados.
    def ganar_torneo(self, tipo_torneo: str) -> None:
        super().ganar_torneo(tipo_torneo)
        if tipo_torneo in self.__trofeos_ganados.keys():
            self.__trofeos_ganados[tipo_torneo] += 1


luisito: Perro = Perro('Luisito', 100, 1, 1, 'Pelirrojo', 'Lulu Pomerania')
luisito.ganar_torneo('Internacional')
print(luisito.get_nivel())
print(luisito.get_trofeos_ganados())

