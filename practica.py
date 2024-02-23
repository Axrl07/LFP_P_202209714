# clases para peliculas y artistas
class Pelicula:
    def __init__(self, titulo="vacio", estreno="vacio", genero="vacio"):
        self.titulo = titulo
        self.artistas = []
        self.estreno = estreno
        self.genero = genero
    
    # me devuelve una lista solamente con los nombres de los artistas que participan en la pelicula
    def verArtistas(self) -> list:
        listadoAux = [] # solo para imprimir
        for artista in self.artistas:
            listadoAux.append(artista.nombre)
        return listadoAux
    
    def sobreEscribirArtista(self, nombre, objeto) -> None:
        for i in range(len(self.artistas)):
            if self.artistas[i].nombre == nombre:
                self.artistas[i] = objeto
                break
   
class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []
    
    # me devuelve una lista solamente con los nombres de las peliculas en las que participa el artista
    def verPeliculas(self) -> list:
        listadoAux = [] # solo para imprimir
        for pelicula in self.peliculas:
            listadoAux.append(pelicula.titulo)
        return listadoAux
    
    def sobreEscribirPelicula(self, titulo, objeto) -> None:
        for i in range(len(self.peliculas)):
            if self.peliculas[i].titulo == titulo:
                self.peliculas[i] = objeto
                break

# clase principal
class App:
    # constructor de la clase
    def __init__(self):
        self.listadoPeliculas = []
        self.listadoArtistas = []
    
    # apartado de carga de archivos
    def busqueda(self, titulo="ninguno", nombre="ninguno") -> bool:
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
    
    def retorno(self, titulo="ninguno", nombre="ninguno") -> object:
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
                                existeArtista = self.busqueda("ninguno", actor)
                                if existeArtista is not True:
                                    artista = Artista(actor)
                                    artista.peliculas.append(pelicula)
                                    pelicula.artistas.append(artista)
                                    self.listadoArtistas.append(artista)
                                else:
                                    artista = self.retorno("ninguno", actor)
                                    artista.peliculas.append(pelicula)
                                    pelicula.artistas.append(artista)
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
                                    existeArtista = self.busqueda("ninguno", actor)
                                    if existeArtista is not True:
                                        artista = Artista(actor)
                                        artista.peliculas.append(pelicula)
                                        pelicula.artistas.append(artista)
                                        self.listadoArtistas.append(artista)
                                    else:
                                        artista = self.retorno("ninguno", actor)
                                        artista.peliculas.append(pelicula)
                                        pelicula.artistas.append(artista)
                                self.listadoPeliculas.append(pelicula)
                            else:
                                continue
            # si no se genera ningún error se imprime el mensaje de carga exitosa y se cierra el archivo automáticamente
                      
            print("Carga realizada con éxito")
        except Exception as e:
            print(f"Error: {e}")
            print()
    
    # apartado de gestión de peliculas y artistas
    
    def verContenidos(self) -> None:
        print("-"*30, "Listado de películas", "-"*30)
        for pelicula in self.listadoPeliculas:
            print(f" {pelicula.titulo} estrenada en el año {pelicula.estreno} del género {pelicula.genero}")
            print(" con los artístas: ", pelicula.verArtistas())
        print("-"*30)
        print()
        print("-"*30, "Listado de artistas", "-"*30)
        for artista in self.listadoArtistas:
            listado = artista.verPeliculas()
            print(f" {artista.nombre}", "participa en las peliculas: ", listado)
        print("-"*30)
        print()
        
    def gestionInformacion(self,clave) -> None:
        listadoAuxDiccionarios = []
        while True:
            print("-"*30, f"mostrar peliculas según {clave}", "-"*30)
            for i in range(len(self.listadoPeliculas)):
                if clave == "nombre":
                    print(f" {i+1}. {self.listadoPeliculas[i].titulo}")
                    diccionarioAux = {"pelicula": self.listadoPeliculas[i], "indice": i+1}
                    listadoAuxDiccionarios.append(diccionarioAux)
                else:
                    print(f" {i+1}. {self.listadoArtistas[i].nombre}")
                    diccionarioAux = {"artista": self.listadoArtistas[i], "indice": i+1}
                    listadoAuxDiccionarios.append(diccionarioAux)
            print(" 0. Salir ")
            print("-"*30)
            print()
            option = ""
            while True:
                try:
                    if clave == "nombre":
                        option = int(input("Ingrese el número de la pelicula para ver los artistas que participan: "))
                        if option <= (len(self.listadoPeliculas)+1) and option >= 0:
                            break
                    else:
                        option = int(input("Ingrese el número del artísta, para ver las peliculas en las que participa: "))
                        if option <= (len(self.listadoArtistas)+1) and option >= 0:
                            break
                except:
                    print()
                    print("Ingrese el número correspondiente a la opción que desea seleccionar")
            if option == 0:
                break
            for elemento in range(len(listadoAuxDiccionarios)):
                if clave == "nombre":
                    peliculaAux = listadoAuxDiccionarios[elemento]["pelicula"]
                    indicePelicula = listadoAuxDiccionarios[elemento]["indice"]
                    if option == indicePelicula:
                        print("la pelicula: ", peliculaAux.titulo, "cuenta con los artístas: ", peliculaAux.verArtistas())
                        break
                else:
                    artistaAux = listadoAuxDiccionarios[elemento]["artista"]
                    indiceArtista = listadoAuxDiccionarios[elemento]["indice"]
                    if option == indiceArtista:
                        print("el artísta: ", artistaAux.nombre, "participa en las peliculas: ", artistaAux.verPeliculas())
                        break
            break
            
    def gestion(self):
        while True:
            print("-"*15, " Gestión de películas ", "-"*15)
            print(" 1. Mostrar listado de películas por nombre ")
            print(" 2. Mostrar listado de peliculas por artístas")
            print(" 3. Salir ")
            print("-"*67)
            print()
            option = ""
            while True:
                try:
                    option = int(input("Ingrese el número de la opción a la que desea ingresar: "))
                    if option == 1 or option == 2 or option == 3:
                        break
                except:
                    print()
                    print("Ingrese el número correspondiente a la opción que desea seleccionar")
            if option == 1:
                self.gestionInformacion("nombre")
                print()
            elif option == 2:
                self.gestionInformacion("artistas")
                print()
            elif option == 3:
                break
            else:
                print("Ingrese el número correspondiente a la opción que desea seleccionar")
                print()

    # apartado de filtros
    def filtro(self, llave, tipo) -> list:
        listaAux = []
        if tipo == "artista":
            # for que busca las peliculas que coincidan con el nombre del artísta
            for pelicula in self.listadoPeliculas:
                nombresArtistas = pelicula.verArtistas()
                for nombre in nombresArtistas:
                    if nombre == llave:
                        listaAux.append(pelicula)
            return listaAux
        elif tipo == "estreno":
            # for que busca las peliculas que coincidan con el año de estreno
            for pelicula in self.listadoPeliculas:
                if pelicula.estreno == llave:
                    listaAux.append(pelicula)
            return listaAux
        else:
            # for que busca las peliculas que coincidan con el género
            for pelicula in self.listadoPeliculas:
                if pelicula.genero == llave:
                    listaAux.append(pelicula)
            return listaAux
    
    def gestionFiltros(self, tipo) -> None:
        while True:
            listadoAuxDiccionarios = []
            print("-"*15, f" Filtrado por {tipo} ", "-"*15)
            if tipo == "artista":
                for i in range(len(self.listadoArtistas)):
                    artistaAux = self.listadoArtistas[i]
                    print(f" {i+1}. {artistaAux.nombre}")
                    diccionarioAux = {"artista": artistaAux, "indice": i+1}
                    listadoAuxDiccionarios.append(diccionarioAux)
            elif tipo == "estreno":
                listadoAuxEstrenos = []
                for i in range(len(self.listadoPeliculas)):
                    estreno = self.listadoPeliculas[i].estreno
                    if estreno not in listadoAuxEstrenos:
                        print(f" {i+1}. peliculas estranadas en el año {estreno}")
                        diccionarioAux = {"estreno": estreno, "indice": i+1}
                        listadoAuxDiccionarios.append(diccionarioAux)
                        estreno.append(estreno)
            else:
                listadoAuxGeneros = []
                for i in range(len(self.listadoPeliculas)):
                    genero = self.listadoPeliculas[i].genero
                    if genero not in listadoAuxGeneros:
                        print(f" {i+1}. peliculas del genero {genero}")
                        diccionarioAux = {"genero": genero, "indice": i+1}
                        listadoAuxDiccionarios.append(diccionarioAux)
                        genero.append(genero)
            print(" 0. Salir ")
            print("-"*30)
            print()
            option = None
            while True:
                try:
                    option = int(input("Ingrese el número del artísta por el que desea filtrar: "))
                    if option <= (len(self.listadoArtistas)+1) and option >= 0:
                        break
                except:
                    print()
                    print("Ingrese el número correspondiente a la opción que desea seleccionar")
            if option == 0:
                    break
            peliculasAux = []
            for elemento in range(len(listadoAuxDiccionarios)):
                if tipo == "artista":
                    indiceArtista = listadoAuxDiccionarios[elemento]["indice"]
                    artistaAux = listadoAuxDiccionarios[elemento]["artista"]
                    if option == indiceArtista:
                        peliculasAux = self.filtro(artistaAux, "artista")
                elif tipo == "estreno":
                    indiceEstreno = listadoAuxDiccionarios[elemento]["indice"]
                    estrenoAux = listadoAuxDiccionarios[elemento]["estreno"]
                    if option == indiceEstreno:
                        peliculasAux = self.filtro(estrenoAux, "estreno")
                else:
                    indiceGenero = listadoAuxDiccionarios[elemento]["indice"]
                    generoAux = listadoAuxDiccionarios[elemento]["genero"]
                    if option == indiceGenero:
                        peliculasAux = self.filtro(generoAux, "genero")
            if tipo == "artista":
                print(f"las peliculas en las que participa el artista {artistaAux.nombre} son: ", peliculasAux)
                print()
                break
            elif tipo == "estreno":
                print(f"las peliculas estrenadas en el año {estrenoAux} son: ", peliculasAux)
                print()
                break
            else:
                print(f"las peliculas del genero {generoAux} son: ", peliculasAux)
                print()
                break
                
    def filtrado(self):
        print("-"*15," Filtrado de películas ","-"*15)
        print("1. filtrar por actor")
        print("2. filtrar por estreno")
        print("3. filtrar por genero")
        option = None
        while True:
            try:
                option = int(input("ingrese el numero de la opcion que desea")) 
                if option >=1 and option <=3:
                    break
            except:
                print("error al ingresar la opcion intentelo nuevamente.")
                print("-"*30)
                print()
        if option == 1:
            self.gestionFiltros("artista")
        elif option == 2:
            self.gestionFiltros("estreno")
        else:
            self.gestionFiltros("genero")
    
    # apartado de graphviz
    def grafica(self):
        pass
    
    # menu principal y de bienvenida
    def menu(self):
        while True:
            print("-"*30, "Menú", "-"*30)
            print(" 1. Cargar archivo de entrada ")
            print(" 2. Gestionar películas ")
            print(" 3. Filtrar información ")
            print(" 4. Gráfico ")
            print(" 5. Salir ")
            print(" 6. Ver base de datos ")
            print("-"*67)
            print()
            option = ""
            while True:
                try:
                    option = int(input("Ingrese el número de la opción a la que desea ingresar: "))
                    if option > 0 and option <= 6:
                        break
                except:
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
            elif option == 6:
                self.verContenidos()
                print()
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

# ejecución del programa
if __name__ == '__main__':
    app = App()
    app.bienvenida()
    #input("Presione Enter para continuar...")
    # borrar la siguiente línea al momento de entregar
    app.carga("pruebas.lfp")
    app.carga("pruebas2.lfp")
    app.menu()
        