import sqlite3

Nombre_Base_De_Datos = "Diccionario de Slang Panameño"

def obtener_conexion():
    return sqlite3.connect(Nombre_Base_De_Datos)

def crear_tablas():
    tablas = [
        """
        CREATE TABLE IF NOT EXISTS diccionario(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            palabra TEXT NOT NULL,
            significado TEXT NOT NULL
        );
        """
    ]
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    for tabla in tablas:
        cursor.execute(tabla)

def principal():
    crear_tablas()
    menu = """
a) Agregar Nueva Palabra
b) Editar Palabra Existente
c) Eliminar Palabra Existente
d) Ver Listado De Palabras
e) Buscar Significado De Palabra
f) Salir
Elige: """

    eleccion = ""
    while eleccion != "f":
        eleccion = input(menu)
        if eleccion == "a":
            palabra = input("Ingresa la palabra: ")

            posible_significado = buscar_significado_palabra(palabra)
            if posible_significado:
                print(f"La palabra '{palabra}' ya existe")
            else:
                significado = input("Ingresa el significado: ")
                agregar_palabra(palabra, significado)
                print("Palabra agregada")
        if eleccion == "b":
            palabra = input("Ingresa la palabra que quieres editar: ")
            nuevo_significado = input("Ingresa el nuevo significado: ")
            editar_palabra(palabra, nuevo_significado)
            print("Palabra actualizada")
        if eleccion == "c":
            palabra = input("Ingresa la palabra a eliminar: ")
            eliminar_palabra(palabra)
        if eleccion == "d":
            palabras = obtener_palabras()
            print("=== Lista de palabras ===")
            for palabra in palabras:

                print(palabra[0])
        if eleccion == "e":
            palabra = input(
                "Ingresa la palabra de la cual quieres saber el significado: ")
            significado = buscar_significado_palabra(palabra)
            if significado:
                print(f"El significado de '{palabra}' es:\n{significado[0]}")
            else:
                print(f"Palabra '{palabra}' no encontrada")

def agregar_palabra(palabra, significado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "INSERT INTO diccionario(palabra, significado) VALUES (?, ?)"
    cursor.execute(sentencia, [palabra, significado])
    conexion.commit()

def editar_palabra(palabra, nuevo_significado):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "UPDATE diccionario SET significado = ? WHERE palabra = ?"
    cursor.execute(sentencia, [nuevo_significado, palabra])
    conexion.commit()

def eliminar_palabra(palabra):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sentencia = "DELETE FROM diccionario WHERE palabra = ?"
    cursor.execute(sentencia, [palabra])
    conexion.commit()

def obtener_palabras():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT palabra FROM diccionario"
    cursor.execute(consulta)
    return cursor.fetchall()

def buscar_significado_palabra(palabra):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    consulta = "SELECT significado FROM diccionario WHERE palabra = ?"
    cursor.execute(consulta, [palabra])
    return cursor.fetchone()

if __name__ == '__main__':
    principal()