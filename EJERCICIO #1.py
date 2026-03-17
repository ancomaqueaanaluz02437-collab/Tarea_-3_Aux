#Ejercicio 4 Videojuegos
class Videojuego:
    def __init__(self, nombre=None, plataforma=None, jugadores=None):
        if nombre is None and plataforma is None and jugadores is None:
            self.nombre = "Desconocido"
            self.plataforma = "Desconocida"
            self.jugadores = 1
        elif jugadores is None:
            self.nombre = nombre
            self.plataforma = plataforma
            self.jugadores = 1
        else:
            self.nombre = nombre
            self.plataforma = plataforma
            self.jugadores = jugadores
    def agregarJugadores(self, cantidad=None):
        if cantidad is None:
            self.jugadores += 1
        else:
            self.jugadores += cantidad
    def mostrarDatos(self):
        print("Nombre:", self.nombre)
        print("Plataforma:", self.plataforma)
        print("Jugadores:", self.jugadores)
v1 = Videojuego("Minecraft", "PC", 2)
v2 = Videojuego("Free Fire", "Android", 3)
v1.agregarJugadores()     
v2.agregarJugadores()    
v1.mostrarDatos()
v2.mostrarDatos()
