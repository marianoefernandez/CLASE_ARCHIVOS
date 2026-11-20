from archivos import *
from salidas import mostrar_lista_diccionarios,mostrar_matriz
from funciones import codificar_dato

#JSON
#1.Leer un archivo .json
# lista_usuarios = leer_json("usuarios.json")
# mostrar_lista_diccionarios(lista_usuarios,"USUARIOS","ERROR AL LEER LA LISTA")

#2.Guardar un archivo .json

# alumnos = [
#     {"nombre": "Santiago", "apellido": "Pérez", "legajo": 10001, "carrera": "Ingeniería en Sistemas", "anio": 1, "nota_final": 8.5},
#     {"nombre": "Martina", "apellido": "Gómez", "legajo": 10002, "carrera": "Administración", "anio": 2, "nota_final": 9.0},
#     {"nombre": "Lucas", "apellido": "Rodríguez", "legajo": 10003, "carrera": "Ingeniería en Sistemas", "anio": 3, "nota_final": 7.0},
#     {"nombre": "Valentina", "apellido": "Fernández", "legajo": 10004, "carrera": "Contador Público", "anio": 1, "nota_final": 8.0},
#     {"nombre": "Mateo", "apellido": "López", "legajo": 10005, "carrera": "Diseño Gráfico", "anio": 2, "nota_final": 6.5}
# ]

# guardar_json("alumnos_2.json",alumnos)

#EJEMPLO FINAL --> Actualizar una lista de usuarios
#1. LEO EL JSON
# lista_usuarios = leer_json("usuarios.json")

# #2.Creo un nuevo usuario --> DANDO DE ALTA UN NUEVO USUARIO
# usuario =     {
#         "nombre_usuario": "admin_utn",
#         "clave": codificar_dato("mariano123"),
#         "rol": "administrador"
#     }

# #3.Guardar ese usuario a la lista
# lista_usuarios.append(usuario)

# #4.Actualizo al archivo los datos modificados (persista la informacion en el archivo)
# guardar_json("usuarios.json",lista_usuarios)

#CSV

#LEER CSV MATRIZ
# matriz_ventas = leer_csv_matriz("ventas_octubre.csv")
# mostrar_matriz(matriz_ventas,"MATRIZ VENTAS")

#GUARDAR CSV MATRIZ
#Ene  Feb  Mar  Abr  May
matriz_ventas = [
    [120, 115, 130, 125, 140],  # Alfajor
    [ 85,  90,  80,  95, 100],  # Gaseosa
    [ 60,  55,  65,  70,  75],  # Agua
    [ 45,  50,  40,  48,  55],  # Papas fritas
    [ 90,  85,  95, 100, 105],  # Chicles
    [ 30,  35,  28,  32,  38],  # Cigarrillos
    [ 75,  70,  80,  78,  85],  # Galletitas
    [110, 105, 120, 115, 125],  # Chocolate
    [ 25,  30,  22,  27,  33],  # Café
    [ 50,  45,  55,  52,  60],  # Caramelos
]

guardar_csv_matriz("Enero,Febrero,Marzo,Abril,Mayo","ventas_meses.csv",matriz_ventas)