def calcular_promedio(numeros : list) -> float:
    numeros_acumulados : float = 0
    for numero in numeros:
        numeros_acumulados = numeros_acumulados + numero
        promedio : float = numeros_acumulados / len(numeros)
    return promedio

