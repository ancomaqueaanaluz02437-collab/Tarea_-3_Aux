#Ejercicio 5 Aula
class Aula:
    def __init__(self, nombreAula, piso, estudiantes, notas):
        self.nombreAula = nombreAula
        self.piso = piso
        self.estudiantes = estudiantes
        self.notas = notas
    def mostrarDatos(self, estado=None):
        if estado is None:
            print("Nombre del aula:", self.nombreAula)
            print("Piso:", self.piso)
            print("Estudiantes y notas:")
            for i in range(len(self.estudiantes)):
                print(self.estudiantes[i], "-", self.notas[i])
        else:
            print("Estado de estudiantes:")
            for i in range(len(self.estudiantes)):
                if self.notas[i] >= 51:
                    print(self.estudiantes[i], ": APROBADO")
                else:
                    print(self.estudiantes[i], ": REPROBADO")
estudiantes = ["Andrea", "Luz"]
notas = [76, 90]
aula1 = Aula("Aula 103", 2, estudiantes, notas)
aula1.mostrarDatos()
print()
aula1.mostrarDatos(True)
