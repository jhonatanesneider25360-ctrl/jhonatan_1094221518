#**********  Zona de Función  ***********#
def tomar_numeros():
    numero = int(input("Escriba el numero: "))
    return numero


def validar_numero(dato_numero):
    if dato_numero > 0:
        mensaje = "El numero es Positivo."
    elif dato_numero==0:
        mensaje = "El numero es Neutro."
    else:
        mensaje = "El numero es Negativo."
    return mensaje


def imprimir_dato(dato_mensaje):
    print("El numero es: " + dato_mensaje)


#***********  Codigo Principal de Python  ***********#
dato_numero = tomar_numeros()
dato_mensaje = validar_numero(dato_numero)
imprimir_dato(dato_mensaje)
