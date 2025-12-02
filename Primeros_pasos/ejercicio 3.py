#**********  Zona de Función  **********#
def tomar_numero():
    numero = int(input("Digite un numero: "))
    return numero


def num_digi(dato_numero):
    while dato_numero!=0:
        if dato_numero%2==0:
            mensaje = "El numero es par"
        else:
            mensaje = "El numero es impar"
        return mensaje


def imprimir_dato(dato_mensaje):
    print("El numero es " + dato_mensaje)
    
    print("Finalizó el programa")
    
    
#**********  Codigo Principal de Python  **********#
dato_numero = tomar_numero()
dato_mensaje = num_digi(dato_numero)
imprimir_dato(dato_mensaje)