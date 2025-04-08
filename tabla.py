class Tabla:
    def _init_(self, numero):
        self.numero = numero

    def imprimir_tabla(self):
        print(f"Tabla del {self.numero}:")
        for i in range(1, 11):
            print(f"{self.numero} x {i} = {self.numero * i}")

    def imprimir_tabla_invertida(self):
        print(f"Tabla del {self.numero} (invertida):")
        for i in range(10, 0, -1):
            print(f"{self.numero} x {i} = {self.numero * i}")


# Uso de la clase
tabla_5 = Tabla(5)
tabla_5.imprimir_tabla()
print()  # Línea en blanco
tabla_5.imprimir_tabla_invertida()