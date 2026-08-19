import sqlite3

from base_datos import conectar
from modelos import Alumno

def crear_alumno_desde_registro(registro):
    alumno = Alumno(
        registro["id"],
        registro["nombre"],
        registro["curso"],
        registro["precio"]
    )

    return alumno


def ver_alumnos():
    conexion = None

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT id, nombre, curso, precio FROM alumnos"
        )

        registros = cursor.fetchall()

        print("")
        print("=== ALUMNOS REGISTRADOS ===")

        if len(registros) == 0:
            print("No hay alumnos registrados.")
            return

        for registro in registros:
            alumno = crear_alumno_desde_registro(registro)

            print("---------------------------------------------------")
            alumno.mostrar_informacion()

    except sqlite3.Error as error:
        print("Ocurrió un error al consultar los alumnos.")
        print("Detalle: ", error)

    finally:
        if conexion is not None:
            conexion.close()


def registrar_alumno():
    conexion = None

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        nombre = input("Ingrese el nombre del alumno: ").strip()
        curso = input("Ingrese el curso: ").strip()

        if nombre == "":
            print("Error: el nombre no puede estar vacío.")
            conexion.close()
            return

        if curso == "":
            print("Error: el curso no puede estar vacío.")
            conexion.close()
            return

        try:
            precio = float(input("Ingrese el precio del curso: "))

        except ValueError:
            print("Error: debe ingresar un número válido.")
            conexion.close()
            return

        if precio <= 0:
            print("Error: el precio debe ser mayor que 0.")
            conexion.close()
            return

        cursor.execute(
            """INSERT INTO alumnos(nombre, curso, precio)
            VALUES (?, ?, ?)
            """,
            (nombre, curso, precio)
        )

        conexion.commit()

        print("Alumno registrado correctamente.")

    except sqlite3.Error as error:
        print("Ocurrió un error al registrar el alumno.")
        print("Detalle: ", error)

        if conexion is not None:
            conexion.rollback()

    finally:
        if conexion is not None:
            conexion.close()



def buscar_alumno():
    conexion = conectar()
    cursor = conexion.cursor()

    busqueda = input("Ingrese el nombre del alumno a buscar: ").strip()

    if busqueda == "":
        print("Error: debe escribir un nombre.")
        conexion.close()
        return

    cursor.execute(
        "SELECT id, nombre, curso, precio FROM alumnos WHERE nombre LIKE ?",
        ("%" + busqueda + "%",)
    )

    resultados = cursor.fetchall()

    conexion.close()

    if len(resultados) == 0:
        print("No se encontró ningún alumno.")
        return

    print("")
    print("=== RESULTADOS DE BÚSQUEDA ===")

    for registro in resultados:
        alumno = crear_alumno_desde_registro(registro)

        print("-----------------------------------------------------")
        alumno.mostrar_informacion()


def editar_alumno():
    conexion = None

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            alumno_id = int(input("Ingrese el ID del alumno a editar: "))

        except ValueError:
            print("Error: debe ingresar un número entero.")
            conexion.close()
            return

        cursor.execute(
            "SELECT id, nombre, curso, precio FROM alumnos WHERE id =?",
            (alumno_id,)
        )

        alumno = cursor.fetchone()

        if alumno is None:
            print("No se encontro ningun alumno con esa ID.")
            conexion.close()
            return

        print("")
        print("=== ALUMNO ENCONTRADO ===")
        print("ID: ", alumno["id"])
        print("Nombre: ", alumno["nombre"])
        print("Curso: ", alumno["curso"])
        print("Precio: ", alumno["precio"])

        nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()
        nuevo_curso = input("Ingrese el nuevo curso: ").strip()

        if nuevo_nombre == "":
            print("Error: el nombre no puede estar vacío.")
            return

        if nuevo_curso == "":
            print("Error: el curso no puede estar vacío.")
            return

        try:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))

        except ValueError:
            print("Error: debe ingresar un número válido.")
            return

        if nuevo_precio <= 0:
            print("Error: el precio debe ser mayor que 0.")
            return

        cursor.execute(
            """
            UPDATE alumnos
            SET nombre = ?, curso = ?, precio = ?
            WHERE id = ?
            """,
            (
                nuevo_nombre,
                nuevo_curso,
                nuevo_precio,
                alumno_id
            )
        )

        conexion.commit()

        print("Alumno aztualizado correctamente.")

    except sqlite3.Error as error:
        print("Ocurrió un error al actualizar el alumno.")
        print("Detalle: ", error)

        if conexion is not None:
            conexion.rollback()

    finally:
        if conexion is not None:
            conexion.close()


def eliminar_alumno():
    conexion = None

    try:
        conexion = conectar()
        cursor = conexion.cursor()

        try:
            alumno_id = int(input("Ingrese el ID del alumno a eliminar: "))

        except ValueError:
            print("Error: debe ingresar un número entero.")
            return

        cursor.execute(
            "SELECT id, nombre, curso, precio FROM alumnos WHERE id =?",
            (alumno_id,)
        )

        alumno = cursor.fetchone()

        if alumno is None:
            print("No se encontró ningún alumno con ese ID.")
            return

        print("")
        print("=== ALUMNO ENCONTRADO ===")
        print("ID: ", alumno["id"])
        print("Nomrbre: ", alumno["nombre"])
        print("Curso: ", alumno["curso"])
        print("Precio: ", alumno["precio"])

        confirmacion = input(
            "¿Seguro que desea eliminar este alumno? (s/n): "
        ).strip().lower()

        if confirmacion != "s":
            print("Eliminación cancelada.")
            return

        cursor.execute(
            "DELETE FROM alumnos WHERE id = ?",
            (alumno_id,)
        )

        conexion.commit()

        print("Alumno eliminado correctamente.")

    except sqlite3.Error as error:
        print("Ocurrió un error al eliminar el alumno.")
        print("Detalle: ", error)

        if conexion is not None:
            conexion.rollback()

    finally:
        if conexion is not None:
            conexion.close()