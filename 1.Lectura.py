import os
import time

NOMBRE_ARCHIVO = "nombres.txt"

#Cuando manejo archivos tengo 3 etapas

#OPERACIONES DE LECTURA

#1)Apertura --> Abro el archivo de mi disco duro y lo guardo en la memoria ram, todo esto posible gracias al objeto file

#file --> Ubicacion del archivo que quiero abrir
#Esta misma puede ser la ruta "absoluta" o la ruta "relativa"
#absoluta --> /Users/mariano/Desktop/SEGUNDO CUATRIMESTRE 2026/ARCHIVOS/hola.txt
#relativa --> hola.txt
#relativa --> archivos/chau.txt
#Siempre recomiendo que usen la ruta relativa
#Cuando abro un archivo en modo lectura, si el ARCHIVO no EXISTE, el programa rompe

#Como buena practica cuando leo el archivo, no importa si se que el archivo existe

# if os.path.exists(NOMBRE_ARCHIVO):#Verificar de antemano si el archivo existe en la ubicacion que le paso
#     archivo = open(NOMBRE_ARCHIVO,"r",encoding="utf-8")
#     #2)Manipulación --> Realizar operaciones de (escritura, lectura o anexo) dentro del archivo

#     #READ PARA LEER TODO EL ARCHIVO
#     # print(f"PUNTERO ARCHIVO : {archivo.tell()}")
#     # #METODO READ --> Extraer la informacion de todo el archivo o parte de el y convertirlo a un string (mueve el puntero del archivo)

#     # texto = archivo.read()#Extraer toda la informacion del archivo y guardarlo en la variable texto
#     # print(f"Info del archivo --> {texto}")
#     # print(f"PUNTERO ARCHIVO : {archivo.tell()}")
#     # archivo.seek(5) #Mover la posicion del archivo libremente
#     # print(f"PUNTERO ARCHIVO : {archivo.tell()}")

#     #READ PARA LEER PARTE DEL ARCHIVO
#     #Imaginen que solo quiero leer los primeros 5 caracteres del archivo
#     # print(f"Antes del read --> {archivo.tell()}")
#     # parte_1 = archivo.read(5)#El parametro size me permite definir cuantos bytes (caracteres) voy a leer en mi archivo
#     # print(f"Despues del read --> {archivo.tell()}")
#     # print(f"parte 1 --> {parte_1}")
#     # parte_2 = archivo.read(5)#Leo 5 bytes mas
#     # print(f"parte 2 --> {parte_2}")

#     #READLINE --> Lee una linea del archivo, si me quedo sin lineas por leer ya no lee mas nada
#     # print(f"PRIMER LINEA --> {archivo.readline()}")
#     # print(f"SEGUNDA LINEA --> {archivo.readline()}")
#     # print(f"TERCER LINEA --> {archivo.readline()}")


#     # #READLINES --> Convertir la informacion del archivo en una lista
#     # lista_archivo = archivo.readlines()

#     # for i in range(len(lista_archivo)):
#     #     print(f"Nombre: {lista_archivo[i]}",end="")

#     #READLINES no es optimo para recorrer los elementos de mi archivo ya que gasta el doble de recursos en la ram, masomenos 15 mb para guardar la info del archivo y otros 15 mb para crear la lista que guarda la info del archivo --> 30 MB masomenos

#     #Utilizando esta otra forma, solo vamos a gastar los 15 mb reservados del archivo.

#     #EL OBJETO FILE ES ITERABLE --> lo puedo recorrer con el for
#     # for linea in archivo:
#     #     print(f"Nombre: {linea}",end="")

#     #No les recomiendo que utilicen el readlines si quieren mostrar la informacion de la lista en un for



#     #3)Cierre --> Liberar esos recursos que guarde en la ram para que la memoria se libere. (La realidad es que al programador muchas veces se le olvida cerrar el archivo)
#     archivo.close()#Libera los recursos del archivo en la memoria ram
#     del archivo
# else:
#     print("EL ARCHIVO NO EXISTE EN EL SISTEMA")

#SENTENCIA WITH --> CUANDO UTILIZAMOS EL WITH , PODEMOS ABRIR EL ARCHIVO Y OLVIDANOS DE CERRARLO YA QUE EL INTERPRETE LO HACE AUTOMATICAMENTE

NOMBRE_ARCHIVO_2 = "hola.txt"

if os.path.exists(NOMBRE_ARCHIVO_2):
    with open(NOMBRE_ARCHIVO_2,"r",encoding="utf-8") as archivo:
        print(f"Leo el contenido del archivo --> {archivo.read()}")
    del archivo
else:
    print("EL ARCHIVO NO EXISTE")

print("FIN DEL PROGRAMA")

#SI QUIERO ELIMINAR UN ARCHIVO EN MI PROGRAMA, SE PUEDE UTILIZAR UNA FUNCION LLAMADA REMOVE
# os.remove("lalala.txt")#ES PELIGROSA ESTA FUNCION