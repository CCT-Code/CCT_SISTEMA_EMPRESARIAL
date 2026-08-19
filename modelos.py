class Alumno:
    def __init__(self, id, nombre, curso, precio):
        self.id = id
        self.nombre = nombre
        self.curso = curso
        self.precio = precio
        self.total_pagado = 0

    def mostrar_informacion(self):
        print("ID: ", self.id)
        print("Nombre: ", self.nombre)
        print("Curso: ", self.curso)
        print("Precio: ", self.precio)
        print("Total pagado: ", self.total_pagado)
        print("Saldo pendiente: ", self.calcular_saldo())
        print("Estado de pago: ", self.obtener_estado_pago())

    def registrar_pago(self, cantidad):
        if cantidad <= 0 :
            print("Error: el pago debe ser mayor que 0.")
            return

        saldo_actual = self.calcular_saldo()

        if cantidad > saldo_actual:
            print("Error: el pago no puede ser mayor que el saldo pendiente.")
            return

        self.total_pagado = self.total_pagado + cantidad

        print("Pago registrado correctamente.")

    def calcular_saldo(self):
        saldo = self.precio - self.total_pagado
        return saldo

    def obtener_estado_pago(self):
        if self.total_pagado == 0:
            return "Pendiente"

        elif self.total_pagado < self.precio:
            return "Pago parcial"

        else:
            return "Pagado"
