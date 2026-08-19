from base_datos import conectar
from modelos import Alumno


conexion = conectar()
cursor = conexion.cursor()

cursor.execute(
    "SELECT id, nombre, curso, precio FROM alumnos"
)

registros = cursor.fetchall()

conexion.close


for registro in registros:
    alumno = Alumno(
        registro[0],
        registro[1],
        registro[2],
        registro[3]
    )

    print("-------------------------------------------")
    alumno.mostrar_informacion()