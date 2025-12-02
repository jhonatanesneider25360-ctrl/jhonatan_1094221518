#***********  Zona de Función  ***********#
def cantidad_numero():
    numero = int(input("Digite un numero del 1 al 12: "))
    return numero
def suma_num(num_dos):
   suma = int(input("Digite otro numero del 1 al 12: "))
   return suma
for i in range(0,12):
    numero=int(input())
    suma=suma+numero
def imprimir_numero(dato_numero):
 print("La sumatoria total es: " + str(suma))
 
   
#***********  Codigo Principal de Python  ***********#
num_dos = cantidad_numero()
dato_num = suma_num(num_dos)
imprimir_numero(dato_num)