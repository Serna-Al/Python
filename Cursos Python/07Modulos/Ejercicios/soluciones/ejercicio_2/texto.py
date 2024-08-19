import utilidades

def formatear_texto(texto : str, formato : str) -> str:
    if formato == "minusculas":
        return utilidades.minusculas(texto)
    elif formato == "mayuscuclas":
        return utilidades.mayusculas(texto)
    return print(f"El formato {formato} no existe")