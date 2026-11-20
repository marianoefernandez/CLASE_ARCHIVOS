import os
from funciones import *

#OPERACIONES DE ESCRITURA

NOMBRE_ARCHIVO = "archivo_importante.txt"

nombres = ["Santiago", "Martina", "Lucas", "Valentina", "Mateo", "Camila", "Benjamin", "Sofia", "Tomas", "Julieta", "Facundo", "Agustina", "Nicolas", "Lucia", "Franco", "Catalina", "Joaquin", "Emilia", "Lautaro", "Micaela", "Thiago", "Florencia", "Gabriel", "Milagros", "Federico"]

#1)Apertura --> Abro el archivo de mi disco duro y lo guardo en la memoria ram, todo esto posible gracias al objeto file
#2)Manipulación --> Realizar operaciones de (escritura, lectura o anexo) dentro del archivo
#3)Cierre --> Liberar esos recursos que guarde en la ram para que la memoria se libere. (La realidad es que al programador muchas veces se le olvida cerrar el archivo)

#Cuando estamos escribiendo un archivo si el archivo no existe, LO CREA y si el archivo existe LO MODIFICA, eliminando (PARA SIEMPRE) el contenido anterior --> MUCHO OJO CON ESTO.

#Otro problema de la escritura del archivo es que si yo tengo un error y escribo un archivo infinito puedo llenar todo mi disco duro.

#COMO BUENA PRACTICA, RECOMENDAMOS PEDIRLE UNA CONFIRMACION AL USUARIO SI REALMENTE QUIERE PISAR ESE ARCHIVO --> (No siempre, solo cuando el nombre del archivo lo ingresa el usuario)

# with open(NOMBRE_ARCHIVO,"w",encoding="utf-8") as archivo:
#     #EL METODO WRITE me permite escribir dentro el archivo
#     archivo.write("HOLA MUNDO")
#     # archivo.write("\nHOLA DIV 113")
#     # archivo.write("\nHOLA MARIANO")

#     #WRITELINES --> ESCRIBE UNA LISTA DE STR DENTRO DEL ARCHIVO
#     # archivo.writelines(nombres)

#LAS OPERACIONES DE ESCRITURA SON PELIGROSAS, HAY DOS COSAS A TENER EN CUENTA

#1.Si el nombre del archivo lo pone el usuario, como buena practica hay que pedirle una confirmacion antes de pisar la informacion, porque si el archivo ya existe, lo modifica, sobreescribiendo todo lo que habia y la información se pierde.

# ubicacion_archivo = input("Ingrese la ubicacion del archivo a escribir:")
# texto = input("Ingrese el texto a escribir: ")
# respuesta = "si"

# if os.path.exists(ubicacion_archivo):
#     print("LA UBICACION YA EXISTE")
#     respuesta = input("Desea modificar el archivo de todos modos? (ESTA ACCION NO SE PUEDE CANCELAR: )")

# if respuesta == "si":
#     with open(ubicacion_archivo,"w",encoding="utf-8") as archivo:
#         archivo.write(texto)
# else:
#     print("OPERACION CANCELADA")

#2.Yo al crear un archivo y escribirlo pongo en riesgo a mi disco duro si me mando alguna.

#Por ejemplo si quiero escribir algo y pongo un bucle infinito (Voy a llenar mi disco duro) --> ADVERTENCIA NO LO PRUEBEN

# with open("virus.txt","w",encoding="utf-8") as archivo:
#     texto = "X" * 10000000
#     archivo.write(texto)

#OTRO TIPO DE PELIGROS ES ESCRIBIR UN ARCHIVO EN UN BUCLE INFINITO --> NO LO PRUEBO POR OBVIAS RAZONES

# print("FIN")
