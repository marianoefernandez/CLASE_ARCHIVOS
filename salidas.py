from funciones import verificar_array,verificar_matriz,obtener_cantidad_columnas

def mostrar_diccionario(diccionario:dict,mensaje_error:str = "ERROR. El diccionario no se puede mostrar") -> None:
    if type(diccionario) == dict:
        for clave in diccionario:
            print(f"{clave} : {diccionario.get(clave)}")
    else:
        print(mensaje_error)

def mostrar_lista_diccionarios(lista_diccionarios:list,titulo:str = "",mensaje_error:str = "Error, el array esta vacio") -> None:
    if verificar_array(lista_diccionarios):
        print(f"{titulo}\n")
        for i in range(len(lista_diccionarios)):
            mostrar_diccionario(lista_diccionarios[i])
            print("\n")
    else:
        print(mensaje_error)

# def mostrar_matriz(matriz:list,titulo:str = "",mensaje_error:str = "LA MATRIZ ESTA VACIA") -> None:
#     print(titulo)
#     if verificar_matriz(matriz):
#         for fil in range(len(matriz)):
#             for col in range(obtener_cantidad_columnas(matriz)):
#                 print(f"{matriz[fil][col]}",end=" ")
#             print("")
#     else:
#         print(mensaje_error)

#VERSION PRO
def mostrar_matriz(matriz:list,titulo:str = "") -> None:
    print(titulo)
    ancho = 0
    for fil in range(len(matriz)):
        for col in range(obtener_cantidad_columnas(matriz)):
            if len(str(matriz[fil][col])) > ancho:
                ancho = len(str(matriz[fil][col]))
    for fil in range(len(matriz)):
        for col in range(obtener_cantidad_columnas(matriz)):
            print(f"{matriz[fil][col]:>{ancho}}",end=" ")
        print("")