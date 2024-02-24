# imports
from graphviz import Digraph

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
        self.listadoGeneros = []
        self.listadoEstrenos = []
    
    # apartado de carga de archivos 
    def configurarListados(self):
        for pelicula in self.listadoPeliculas:
            if pelicula.estreno not in self.listadoEstrenos:
                self.listadoEstrenos.append(pelicula.estreno)
        for pelicula in self.listadoPeliculas:
            aux = pelicula.genero
            for genero in aux:
                aux2 = genero.lower().strip()
                if aux2 not in self.listadoGeneros:
                    self.listadoGeneros.append(aux2)
        print("Configuración de base de datos realizada con éxito")
    
    def busqueda(self, titulo="ninguno", nombre="ninguno") -> bool:
        if titulo != "ninguno":
            for pelicula in self.listadoPeliculas:
                if pelicula.titulo == titulo:
                # si existe entonces me devuelve un true
                    return True
            return False
        else:
            for artista in self.listadoArtistas:
                artistaAux = artista.nombre
                if artistaAux == nombre:
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
                        titulo = partes[0].strip()
                        existePelicula = self.busqueda(titulo, "ninguno")
                        if existePelicula is False:    
                            actores = partes[1].strip().split(",")
                            actores2 = [x.strip() for x in actores]
                            estreno = partes[2].strip()
                            genero = partes[3].strip().split(",")
                            pelicula = Pelicula(titulo, estreno, genero)
                            for actor in actores2:
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
        print("-"*30, "Listado de generos", "-"*30)
        for genero in self.listadoGeneros:
            print(f" los generos disponibles son: ", genero)
        print("-"*30)
        print()
        print("-"*30, "Listado de estrenos", "-"*30)
        for estreno in self.listadoEstrenos:
            print(f" los años de estreno disponibles son: ", estreno)
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
        if tipo == "estreno":
            # for que busca las peliculas que coincidan con el año de estreno
            for pelicula in self.listadoPeliculas:
                if pelicula.estreno == llave:
                    listaAux.append(pelicula)
            return listaAux
        else:
            # for que busca las peliculas que coincidan con el género
            for pelicula in self.listadoPeliculas:
                aux = pelicula.genero
                for genero in aux:
                    aux2 = genero.lower().strip()
                    if aux2 == llave and aux2 not in listaAux:
                        listaAux.append(pelicula)
            return listaAux
    
    # el filtro falta verificar que se aniden las peliculas
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
                for i in range(len(self.listadoEstrenos)):
                    estreno = self.listadoEstrenos[i]
                    print(f" {i+1}. peliculas estrenadas en {estreno}")
                    diccionarioAux = {"estreno": estreno, "indice": i+1}
                    listadoAuxDiccionarios.append(diccionarioAux)
            else:
                for i in range(len(self.listadoGeneros)):
                    genero = self.listadoGeneros[i]
                    print(f" {i+1}. peliculas del genero {genero}")
                    diccionarioAux = {"genero": genero, "indice": i+1}
                    listadoAuxDiccionarios.append(diccionarioAux)
            print(" 0. Salir ")
            print("-"*30)
            print()
            option = None
            while True:
                try:
                    option = int(input("Ingrese el número del artísta por el que desea filtrar: "))
                    print()
                    if option <= (len(listadoAuxDiccionarios)+1) and option >= 0:
                        break
                except:
                    print()
                    print("Ingrese el número correspondiente a la opción que desea seleccionar")
            if option == 0:
                    break
            peliculasAux = []
            filtro = None
            if tipo == "artista":
                for i in range(len(listadoAuxDiccionarios)+1):
                    indiceAux = listadoAuxDiccionarios[i]["indice"]
                    artistaAux = listadoAuxDiccionarios[i]["artista"]
                    if option == indiceAux:
                        peliculasAux = artistaAux.verPeliculas()
                        filtro = artistaAux.nombre
                        break
                print(f"las peliculas en las que participa el artista {filtro} son: ", peliculasAux)
                break
            elif tipo == "estreno":
                for i in range(len(listadoAuxDiccionarios)+1):
                    indiceAux = listadoAuxDiccionarios[i]["indice"]
                    estrenoAux = listadoAuxDiccionarios[i]["estreno"]
                    if option == indiceAux:
                        peliculasAux = self.filtro(estrenoAux, "estreno")
                        filtro = estrenoAux
                        break
                print(f"las peliculas estrenadas en el año {filtro} son: ")
                for x in peliculasAux:
                    print(x.titulo)
                break
            else:
                for i in range(len(listadoAuxDiccionarios)+1):
                    indiceAux = listadoAuxDiccionarios[i]["indice"]
                    generoAux = listadoAuxDiccionarios[i]["genero"]
                    if option == indiceAux:
                        peliculasAux = self.filtro(generoAux, "genero")
                        filtro = generoAux
                        break
                print(f"las peliculas del genero {filtro} son: ")
                for x in peliculasAux:
                    print(x.titulo)
                break
                
    def filtrado(self):
        print("-"*15," Filtrado de películas ","-"*15)
        print("1. filtrar por actor")
        print("2. filtrar por estreno")
        print("3. filtrar por genero")
        print()
        option = None
        while True:
            try:
                option = int(input("ingrese el numero de la opcion que desea: ")) 
                print()
                if option >=1 and option <=3:
                    break
            except:
                print("error al ingresar la opcion intentelo nuevamente.")
                print("-"*30)
                print()
        if option == 1:
            self.gestionFiltros("artista")
            print()
        elif option == 2:
            self.gestionFiltros("estreno")
            print()
        else:
            self.gestionFiltros("genero")
            print()
    
    # apartado de graphviz
    def crear_grafo(self):
        grafo = Digraph()
        
        # para almacenar todos los nodos que se han creado
        nodos = {}
        
        # Agregar nodos de peliculas
        for pelicula in self.listadoPeliculas:
            #grafo.node(identificador de nodo,etiquetas , atributos)
            grafo.node(pelicula.titulo, f"Titulo: {pelicula.titulo}\nEstreno: {pelicula.estreno}\nGenero: {pelicula.genero}", shape="box", style="filled", color="lightgreen")
            # verificando la lista de artistas
            for artista in pelicula.artistas:
                if artista.nombre not in nodos:
                    # si no existe el artista en el diccionario, se crea
                    nodos[artista.nombre] = []
                nodos[artista.nombre].append(pelicula.titulo)
        
        #conectando los nodos de artistas con las peliculas
        for artista, peliculas in nodos.items():
            grafo.node(artista, shape="box", style="filled", color="skyblue")
            for pelicula in peliculas:
                # relacionando los nodos
                # grafo.edge(nodoPrincipal, nodoSecundario, atributos)
                # el formato anterior es para que la flecha vaya de la pelicula al artista/s
                grafo.edge(pelicula, artista, color="black")
                
        #ajustando
        grafo.attr(rankdir="LR", splines="ortho")
        
        #guardando
        grafo.render("digrama de relaciones Pelicula-Artista", format="jpg", view=True)
    
    # menu principal y de bienvenida
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
                try:
                    option = int(input("Ingrese el número de la opción a la que desea ingresar: "))
                    print()
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
                print()
            elif option == 3:
                self.filtrado()
                print()
            elif option == 4:
                self.crear_grafo()
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
    input("Presione Enter para continuar...")
    app.carga("pruebas.lfp")
    app.carga("pruebas2.lfp")
    app.configurarListados()
    app.menu()
        