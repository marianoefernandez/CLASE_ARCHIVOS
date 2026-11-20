import os
import json
from typing import Any
from funciones import separar_cadena,normalizar_lista_entera,verificar_matriz,unir_cadena

def leer_json(nombre_archivo:str) -> Any:
    if type(nombre_archivo) == str and os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:#A veces rompe el .json por poner el encoding utf-8, en caso de que les ocurra, sacar el encoding
            return json.load(archivo)
    else:
        return None

def guardar_json(nombre_archivo:str,objeto_json:Any,indentado:bool = True) -> bool:
    if type(nombre_archivo) == str and type(objeto_json) == list or type(objeto_json) == dict:
        with open(nombre_archivo,"w",encoding="utf-8") as archivo:
            if indentado:
                json.dump(objeto_json,archivo,indent=4)
            else:
                json.dump(objeto_json,archivo)
        return True
    else:
        return False

#CSV (MATRIZ)
#3.Leer un archivo .csv desde una matriz
def leer_csv_matriz(nombre_archivo:str) -> list:
    #Un csv tiene dos elementos
    #La cabecera (SIEMPRE LINEA 1)
    #Los datos (LINEA 2 en ADELANTE)
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r",encoding="utf-8") as archivo:
            matriz = []
            #Falsa lectura --> Leer la primer linea (sin guardarlo en ningun lado) para ignorar la cabecera
            archivo.readline()

            for linea in archivo:
                fila = separar_cadena(linea,",")
                normalizar_lista_entera(fila)
                matriz.append(fila)

            return matriz
    else:
        return None

#4.Guardar archivo .csv desde una matriz
def guardar_csv_matriz(cabecera:str,nombre_archivo:str,matriz:list) -> bool:
    if type(cabecera) == str and type(nombre_archivo) == str and verificar_matriz(matriz):
        with open(nombre_archivo,"w",encoding="utf-8") as archivo:
            archivo.write(f"{cabecera}\n")
            for fil in range(len(matriz)):
                linea = unir_cadena(matriz[fil],",")
                if fil != len(matriz) - 1:
                    archivo.write(f"{linea}\n")
                else:
                    archivo.write(f"{linea}")
        return True
    else:
        return False

#5.Leer un archivo .csv desde una lista de diccionario
#CSV (Listas de Diccionarios)
def leer_csv_alumnos():
    pass

#6.Leer un archivo .csv desde una lista de diccionario
def guardar_csv_alumnos():
    pass