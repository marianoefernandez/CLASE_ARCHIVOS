#OPERACIONES DE ANEXAR

#1)Apertura --> Abro el archivo de mi disco duro y lo guardo en la memoria ram, todo esto posible gracias al objeto file
#2)Manipulación --> Realizar operaciones de (escritura, lectura o anexo) dentro del archivo
#3)Cierre --> Liberar esos recursos que guarde en la ram para que la memoria se libere. (La realidad es que al programador muchas veces se le olvida cerrar el archivo)

#Las operaciones de anexo (a), me permiten realizar operaciones de ESCRITURA sin tener que pisar o sobreescribir la informacion

#NOTA --> SE UTILIZAN LAS MISMAS OPERACIONES QUE EN LA ESCRITURA (write y el writelines)

#Si el archivo no existe, lo crea y funciona exactamente igual que la operación de escritura con el tipo "w"
#Si el archivo existe, no pisa ni sobreescribe la informacion, agrega el nuevo texto al final del archivo

#EJEMPLO 1 --> Cuando el archivo no existe.

# with open("anexar.txt","a",encoding="utf-8") as archivo:
#     archivo.write("Hola Mundo")

#EJEMPLO 2 --> Cuando el archivo existe.

with open("hola.txt","a",encoding="utf-8") as archivo:
    print(f"POS DEL ARCHIVO: {archivo.tell()}")
    archivo.write("\nHOLA DIV 113")