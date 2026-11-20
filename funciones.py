import random
import hashlib

def codificar_dato(dato:str):
    return hashlib.sha256(dato.encode('utf-8')).hexdigest()

def crear_cadena_aleatoria(cantidad_caracteres:int = 6) -> str:
    cadena_nueva = ""

    for vueltas in range(cantidad_caracteres):
        numero_random = random.randint(65,90)
        caracter_random = chr(numero_random)
        cadena_nueva += caracter_random

    return cadena_nueva

def verificar_array(array:list) -> bool:
    return type(array) == list and len(array) > 0

def verificar_matriz(matriz:list) -> bool:#MEJORARLA
    return type(matriz) == list and len(matriz) > 0

def obtener_cantidad_columnas(matriz:list) -> int:
    cantidad_columnas = 0
    if verificar_matriz(matriz):
        cantidad_columnas = len(matriz[0])

    return cantidad_columnas

def verificar_numero(caracter_ascii:int) -> bool:
    return caracter_ascii >= 48 and caracter_ascii <= 57

def normalizar_lista_entera(lista:list) -> bool:
    if verificar_array(lista):
        for i in range(len(lista)):
            if type(lista[i] == str and verificar_numero(ord(lista[i]))):
                lista[i] = int(lista[i])
        return True
    else:
        return False

def reemplazar_caracteres(cadena_original:str,caracter_viejo:str,caracter_nuevo:str) -> str:
    cadena_nueva = ""
    
    for i in range(len(cadena_original)):
        if cadena_original[i] == caracter_viejo:
            cadena_nueva += caracter_nuevo
        else:
            cadena_nueva += cadena_original[i]
    
    return cadena_nueva

#Split casero --> Tarea --> debuggear esta funcion para entenderla mas en profundidad
def separar_cadena(cadena:str,separador:str) -> list:
    lista_separada = []
    cadena_nueva = ""
    if type(cadena) == str and (type(separador) == str and len(separador) == 1):
        for i in range(len(cadena)):
            if cadena[i] == separador:
                lista_separada.append(cadena_nueva)
                cadena_nueva = ""
            else:
                cadena_nueva += cadena[i]
        lista_separada.append(cadena_nueva)
    
    return lista_separada

#Join casero
def unir_cadena(lista:list,separador:str) -> str:
    cadena_nueva = ""
    
    for i in range(len(lista)):
        if i == len(lista) - 1:
            cadena_nueva += f"{str(lista[i])}"
        else:
            cadena_nueva += f"{str(lista[i])}{separador}"
        
    return cadena_nueva

# nombres = "Mariano-Juan-Carlos"
# lista_nombres = separar_cadena(nombres,"-")
# print(lista_nombres)

# nombres = ["Ana","Mariano","Jose"]
# print(unir_cadena(nombres,"-"))