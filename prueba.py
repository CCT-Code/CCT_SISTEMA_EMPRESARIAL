from base_datos import conectar
from alumnos import (
    registrar_alumno,
    ver_alumnos,
    buscar_alumno,
    editar_alumno,
    eliminar_alumno
)


def main():
    while True:
        print("")
        print("=== SISTEMA CCT ===")
        print("1. Registrar alumno")
        print("2. Ver alumnos")
        print("3. Buscar alumno")
        print("4. Editar alumno")
        print("5. Eliminar alumno")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_alumno()

        elif opcion == "2":
            ver_alumnos()

        elif opcion == "3":
            buscar_alumno()

        elif opcion == "4":
            editar_alumno()

        elif opcion == "5":
            eliminar_alumno()

        elif opcion == "6":
            print("Cerrando Sistema CCT...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()