class Artista:
    def _init_(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, mi género musical es {self.genero}.")

    def actuar(self):
        print(f"{self.nombre} está realizando su presentación.")

    def despedirse(self):
        print(f"Gracias por acompañarme. ¡Hasta pronto!")


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super()._init_(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su éxito {self.cancion_mas_popular} con gran energía.")


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super()._init_(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")



class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super()._init_(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")



def iniciar_festival(lista_artistas):
    print("\n================================")
    print("       ¡INICIA EL FESTIVAL!")
    print("================================")

    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("--------------------------------")



lista_artistas = []

print("BIENVENIDO AL FESTIVAL MUSICAL")

cantidad = int(input("¿Cuántos artistas se presentarán? "))

for i in range(cantidad):
    print(f"\nARTISTA {i + 1}")

    tipo = input("Tipo de artista (Cantante, DJ o Banda): ").lower()

    nombre = input("Nombre: ")
    genero = input("Género musical: ")
    popularidad = int(input("Popularidad (1 al 100): "))

    if tipo == "cantante":
        cancion = input("Canción más popular: ")
        artista = Cantante(nombre, genero, popularidad, cancion)

    elif tipo == "dj":
        estilo = input("Estilo musical: ")
        artista = DJ(nombre, genero, popularidad, estilo)

    elif tipo == "banda":
        integrantes = int(input("Número de integrantes: "))
        artista = Banda(nombre, genero, popularidad, integrantes)

    else:
        print("Tipo de artista no válido.")
        continue

    lista_artistas.append(artista)

iniciar_festival(lista_artistas)

print("\n¡GRACIAS POR ASISTIR AL FESTIVAL MUSICAL!")