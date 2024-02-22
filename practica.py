class Pelicula:
    def __init__(self, titulo="vacio", estreno="vacio", genero="vacio"):
        self.titulo = titulo
        self.artistas = []
        self.estreno = estreno
        self.genero = genero
    
    def verArtistas(self):
        listadoAux = [] # solo para imprimir
        for artista in self.artistas:
            listadoAux.append(artista.nombre)
        return listadoAux
    
class Artísta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []
    
    def verPeliculas(self):
        listadoAux = [] # solo para imprimir
        for pelicula in self.peliculas:
            listadoAux.append(pelicula.titulo)
        return listadoAux
            

class App:
    def __init__(self):
        self.listadoPeliculas = []
        self.listadoArtistas = []
    
    def busqueda(self, titulo="ninguno", nombre="ninguno"):
        if titulo != "ninguno":
            for pelicula in self.listadoPeliculas:
                if pelicula.titulo == titulo:
                # si existe entonces me devuelve un true
                    return True
            return False
        else:
            for artista in self.listadoArtistas:
                if artista.nombre == nombre:
                    return True
            return False
    
    def retorno(self, titulo="ninguno", nombre="ninguno"):
        if titulo != "ninguno":
            for pelicula in self.listadoPeliculas:
                if pelicula.titulo == titulo:
                # si existe entonces me devuelve un true
                    return pelicula
            return None
        else:
            for artista in self.listadoArtistas:
                if artista.nombre == nombre:
                    return artista
            return None
    
    def carga(self,archivoRuta):
        try:
            # en caso de generarse un error el with open se encarga de cerrar el archivo
            with open(archivoRuta, "r") as archivo:
                lineas = archivo.readlines()
                for linea in lineas:
                    partes = linea.strip().split(";")
                    if len(partes) == 4:
                        titulo = partes[0]
                        existePelicula = self.busqueda(titulo, "ninguno")
                        if existePelicula is False:    
                            actores = partes[1].strip().split(",")
                            estreno = partes[2]
                            genero = partes[3]
                            pelicula = Pelicula(titulo, estreno, genero)
                            for actor in actores:
                                artista = Artísta(actor)
                                existeArtista = self.busqueda("ninguno", actor)
                                pelicula.artistas.append(artista)
                                if existeArtista is True:
                                    continue
                                self.listadoArtistas.append(artista)
                            self.listadoPeliculas.append(pelicula)
                        else:
                            print(f"La película:")
                            print(pelicula.titulo, pelicula.estreno, pelicula.genero)
                            print("con los artístas: ", pelicula.verArtistas())
                            while True:
                                respuesta = input("desea sobreescribir los datos de la pelicula? (s/n)")
                                if respuesta.lower() == "s" or respuesta.lower() == "n":
                                    break
                                print("Ingrese únicamente s o n")
                            if respuesta.lower() == "s":
                                self.listadoPeliculas.remove(self.retorno(titulo, "ninguno"))
                                actores = partes[1].strip().split(",")
                                estreno = partes[2]
                                genero = partes[3]
                                pelicula = Pelicula(titulo, estreno, genero)
                                for actor in actores:
                                    artista = Artísta(actor)
                                    existeArtista = self.busqueda("ninguno", actor)
                                    pelicula.artistas.append(artista)
                                    if existeArtista is True:
                                        continue
                                    self.listadoArtistas.append(artista)
                                self.listadoPeliculas.append(pelicula)
                            else:
                                continue
            # si no se genera ningún error se imprime el mensaje de carga exitosa y se cierra el archivo automáticamente
            print("Carga realizada con éxito")
        except Exception as e:
            print(f"Error: {e}")
            print()
    
    def gestionArtistas(self):
        listadoAuxDiccionarios = []
        while True:
            print("-"*30, "mostrar artístas según la pelicula", "-"*30)
            for i in range(len(self.listadoPeliculas)):
                print(f" {i+1}. {self.listadoPeliculas[i].titulo}")
                diccionarioAux = {"pelicula": self.listadoPeliculas[i], "indice": i+1}
                listadoAuxDiccionarios.append(diccionarioAux)
            print(" 0. Salir ")
            print("-"*67)
            print()
            option = ""
            while True:
                option = int(input("Ingrese el número de la pelicula para ver sus artístas: "))
                if option <= len(self.listadoPeliculas) and option >= 0:
                    break
                print()
                print("Ingrese el número correspondiente a la opción que desea seleccionar")
            if option == 0:
                break
            peliculaAux = None
            for elemento in range(len(listadoAuxDiccionarios)):
                if option == listadoAuxDiccionarios[elemento]["indice"]:
                    peliculaAux = listadoAuxDiccionarios[elemento]["pelicula"]
                    break
            print("la pelicula: ", peliculaAux.titulo, "cuenta con los artístas: ", peliculaAux.verArtistas())
            break
            
    def gestion(self):
        while True:
            print("-"*30, "Gestión de películas", "-"*30)
            print(" 1. Mostrar listado de películas por nombre ")
            print(" 2. Mostrar listado de peliculas por artístas")
            print(" 3. Salir ")
            print("-"*67)
            print()
            option = ""
            while True:
                option = int(input("Ingrese el número de la opción a la que desea ingresar: "))
                if option == 1 or option == 2 or option == 3:
                    break
                print()
                print("Ingrese el número correspondiente a la opción que desea seleccionar")
            if option == 1:
                for pelicula in self.listadoPeliculas:
                    print("la pelicula:", pelicula.titulo, "estrenada en el año:", pelicula.estreno, "pertenece al género:", pelicula.genero, "y cuenta con los artístas: ", pelicula.verArtistas())
                print()
            elif option == 2:
                self.gestionArtistas()
                print()
            elif option == 3:
                break
            else:
                print("Ingrese el número correspondiente a la opción que desea seleccionar")
                print()

    def filtrar(self):
        pass
    
    def grafica(self):
        pass
    
    def menu(self):
        while True:
            print("-"*30, "Menú", "-"*30)
            print(" 1. Cargar archivo de entrada ")
            print(" 2. Gestionar películas ")
            print(" 3. Filtrar información ")
            print(" 4. Gráfico ")
            print(" 5. Salir ")
            print("-"*67)
            print()
            option = ""
            while True:
                option = int(input("Ingrese el número de la opción a la que desea ingresar: "))
                if option > 0 and option < 6:
                    break
                print()
                print("Ingrese el número correspondiente a la opción que desea seleccionar")
            if option == 1:
                RutaArchivo = input("Ingrese el nombre del archivo que desea cargar: ")
                self.carga(RutaArchivo)
                print()
            elif option == 2:
                self.gestion()
            elif option == 3:
                self.filtrar()
                print()
            elif option == 4:
                self.grafica()
                print()
            elif option == 5:
                print("Gracias por utilizar el programa <3")
                break
            else:
                print("Ingrese el número correspondiente a la opción que desea seleccionar")
                print()
        
    def bienvenida(self):
        print("-"*57)
        print("|\tLenguajes formales y de programación\t\t|")
        print("|\tPrimer Semestre 2024\tSección: B+\t\t|")
        print("|\tDesarrollado por: Angel Enrique Alvarado Ruiz\t|")
        print("|\tbajo el Carné: 202209714\t\t\t|")
        print("-"*57)
        
if __name__ == '__main__':
    app = App()
    app.bienvenida()
    input("Presione Enter para continuar...")
    # borrar la siguiente línea al momento de entregar
    app.carga("pruebas.lfp")
    app.menu()
        