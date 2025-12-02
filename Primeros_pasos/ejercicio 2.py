#***********  Zona de Función  ***********#
def capturar_letras():
    while True:
     print("Digite la letra A para Actualziar Sistema")
     print("Digite la letra E para Eliminar Catalogo")
     print("Digite la letra C para Crear Productos")
     print("Digite la letra S para salir del programa")
    letra=str(input("Seleccione una opción: "))
    return letra


def validar_letra(dato_letra):
    if dato_letra== "A" or dato_letra== "a":
        mensaje = "Actualizando..."
    elif dato_letra== "E" or dato_letra=="e":
        mensaje = "Eliminando Catalogo..."
    elif dato_letra== "C" or dato_letra== "c":
        mensaje = "Creando Productos..."
    elif dato_letra== "S" or dato_letra== "s":
        mensaje = "Saliendo..."


def imprimir_mensaje(dato_mensaje):
    print("Estás " + dato_mensaje)
    
    
#**********  Codigo Principal de Python  **********#
dato_letra = capturar_letras()
dato_mensaje = validar_letra(dato_letra)
imprimir_mensaje(dato_mensaje)
