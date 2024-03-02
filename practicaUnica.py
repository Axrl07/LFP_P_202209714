# imports
from graphviz import Digraph

# clases para peliculas y artistas
class Pelicula:
    def __init__(self, titulo, estreno, genero):
        self.titulo = titulo
        self.artistas = []
        self.estreno = estreno
        self.genero = genero
    
    def verArtistas(self) -> list:
        listadoAux = []
        for artista in self.artistas:
            listadoAux.append(artista.nombre)
        return listadoAux
   
class Artista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []
    
    def verPeliculas(self) -> list:
        listadoAux = []
        for pelicula in self.peliculas:
            listadoAux.append(pelicula.titulo)
        return listadoAux

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
        try:
            for pelicula in self.listadoPeliculas:
                if pelicula.estreno not in self.listadoEstrenos:
                    self.listadoEstrenos.append(pelicula.estreno)
            for pelicula in self.listadoPeliculas:
                aux = pelicula.genero
                for genero in aux:
                    aux2 = genero.lower().strip()
                    if aux2 not in self.listadoGeneros:
                        self.listadoGeneros.append(aux2)
            print("-"*30,"configuración de listados","-"*30)
            print("La configuración de los listados fue exitosa")
            print("-"*90)
        except Exception as e:
            print(f"Error: {e}")
            print("intentelo nuevamente, verifique que el archivo contenga el formato correcto")
    
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
    
    def sobreescritura(self, titulo="ninguno", nombre="ninguno") -> object:
        if titulo != "ninguno":
            for pelicula in self.listadoPeliculas:
                if pelicula.titulo == titulo:
                # si existe entonces me devuelve su objeto
                    return pelicula
            return None
        else:
            for artista in self.listadoArtistas:
                artistaAux = artista.nombre
                if artistaAux == nombre:
                    return artista
            return None
        
        
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
                            peliculaAux = self.sobreescritura(titulo, "ninguno")
                            actores = partes[1].strip().split(",")
                            actores2 = [x.strip() for x in actores]
                            estreno = partes[2].strip()
                            genero = partes[3].strip().split(",")
                            
                            print("-"*20,f"Coincidencia Encontrada", "-"*20)
                            print("El registro ingresado es:")
                            print(f"Titulo de la película: {titulo}")
                            print(f"estrenada en el año: {estreno} y del género: {genero}.")
                            print(f"con los artístas: {actores2}")
                            print("-"*60)
                            print("El registro en sistema es:")
                            print(f"Titulo de la película: {peliculaAux.titulo}")
                            print(f"estrenada en el año: {peliculaAux.estreno} y del género: {peliculaAux.genero}.")
                            print(f"con los artístas: {peliculaAux.verArtistas()}")
                            print("-"*60)
                            while True:
                                respuesta = input("desea sobreescribir los datos de la pelicula? (s/n)")
                                if respuesta.lower() == "s" or respuesta.lower() == "n":
                                    break
                                print("Ingrese únicamente s o n")
                            if respuesta.lower() == "s":
                                self.listadoPeliculas.remove(self.retorno(titulo, "ninguno"))
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
                                continue
            # si no se genera ningún error se imprime el mensaje de carga exitosa y se cierra el archivo automáticamente
            print("-"*30,"carga de archivos de prueba","-"*30)
            print("Carga realizada con éxito")
            self.configurarListados()
        except Exception as e:
            print(f"Error: {e}")
            print("intentelo nuevamente, verifique el nombre y extensión del archivo")
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
        listadoAuxiliar = []
        while True:
            if clave == "nombre":
                print(" * "*7,f"listado de películas"," * "*7)
            else:
                print("-"*20, f"información de películas", "-"*20)
            for i in range(len(self.listadoPeliculas)):
                if clave == "nombre":
                    print(f"{self.listadoPeliculas[i].titulo}")
                    listadoAuxiliar.append(self.listadoPeliculas[i])
                else:
                    print(f" {i+1}. {self.listadoPeliculas[i].titulo}")
                    diccionarioAux = {"pelicula": self.listadoPeliculas[i], "indice": i+1}
                    listadoAuxiliar.append(diccionarioAux)
            if clave == "artistas":
                print(" 0. Salir ")
                print("-"*75)
                print()
            option = ""
            while True:
                try:
                    if clave == "artistas":
                        option = int(input("Ingrese el número de la película, para ver su información: "))
                        print()
                        if option <= (len(self.listadoPeliculas)+1) and option >= 0:
                            break
                    else:
                        break
                except:
                    print()
                    print("Ingrese el número correspondiente a la opción que desea seleccionar")
            if option == 0:
                break
            if clave == "artistas":
                print(" * "*10,f"Información"," * "*10)
                for elemento in range(len(listadoAuxiliar)):
                    peliculaAux = listadoAuxiliar[elemento]["pelicula"]
                    indicePelicula = listadoAuxiliar[elemento]["indice"]
                    if option == indicePelicula:
                        print("la pelicula: ", peliculaAux.titulo)
                        print(f"fue estrenada en el año: {peliculaAux.estreno}")
                        if len(peliculaAux.genero) > 1:
                            print("cuenta con los géneros: ", peliculaAux.genero)
                        lista = ""
                        for x in peliculaAux.verArtistas():
                            if x == peliculaAux.verArtistas()[-1]:
                                lista += x
                                print(f"y los artístas que participan en ella son: {lista}")
                                break
                            lista += x + ", "
                        break
                print(" * "*25)
            else:
                print(" * "*20)
                print(f"el total de peliculas en sistema es de: {len(listadoAuxiliar)}")
                print(" * "*20)
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
                    print()
                    if option >= 1 and option <= 3:
                        break
                except:
                    print("Ingrese el número correspondiente a la opción que desea seleccionar")
                    print()
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
                print(" * "*5,f"peliculas en las que participa {filtro}"," * "*5)
                for x in peliculasAux:
                    print(x)
                print(" * "*25)
                break
            elif tipo == "estreno":
                for i in range(len(listadoAuxDiccionarios)+1):
                    indiceAux = listadoAuxDiccionarios[i]["indice"]
                    estrenoAux = listadoAuxDiccionarios[i]["estreno"]
                    if option == indiceAux:
                        peliculasAux = self.filtro(estrenoAux, "estreno")
                        filtro = estrenoAux
                        break
                print(" * "*5,f"peliculas estrenadas en el año {filtro}"," * "*5)
                for x in peliculasAux:
                    print(x.titulo)
                print(" * "*23)
                break
            else:
                for i in range(len(listadoAuxDiccionarios)+1):
                    indiceAux = listadoAuxDiccionarios[i]["indice"]
                    generoAux = listadoAuxDiccionarios[i]["genero"]
                    if option == indiceAux:
                        peliculasAux = self.filtro(generoAux, "genero")
                        filtro = generoAux
                        break
                print(" * "*5,f"peliculas del genero {filtro}", " * "*5)
                for x in peliculasAux:
                    print(x.titulo)
                print(" * "*23)
                break
                
    def filtrado(self):
        while True:
            print("-"*15," Filtrado de películas ","-"*15)
            print("1. filtrar por artista")
            print("2. filtrar por estreno")
            print("3. filtrar por genero")
            print("4. Salir")
            print()
            option = None
            while True:
                try:
                    option = int(input("ingrese el numero de la opcion que desea: ")) 
                    print()
                    if option >=1 and option <=4:
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
            elif option == 3:
                self.gestionFiltros("genero")
                print()
            elif option == 4:
                break
            else:
                print("Ingrese el número correspondiente a la opción que desea seleccionar")
                print()
    
    # apartado de graphviz
    def crear_grafo(self):
        # creando grafo y nodos
        grafo = Digraph()
        nodos = {}
        
        # Agregar nodos de peliculas
        for pelicula in self.listadoPeliculas:
            #grafo.node(identificador de nodo,etiquetas , atributos)
            grafo.node(pelicula.titulo, f"Titulo: {pelicula.titulo}", shape="box", style="filled", color="lightgreen")
            # verificando la lista de artistas
            for artista in pelicula.artistas:
                if artista.nombre not in nodos:
                    # si no existe el artista en el diccionario, se crea
                    nodos[artista.nombre] = artista.verPeliculas()
                else:
                    continue
        
        #conectando los nodos de artistas con las peliculas
        for artista, peliculas in nodos.items():
            grafo.node(artista, shape="box", style="filled", color="skyblue")
            for pelicula in peliculas:
                grafo.edge(pelicula, artista, color="black")
        
        # configurando el grafo
        grafo.attr(rankdir="LR", splines="ortho")
        grafo.render("digrama de relaciones Pelicula-Artista", format="jpg", view=True)
        print(" * "*10)
        print("Grafico creado correctamente")
        print(" * "*10)
        
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
    print()
    # comentar para la presentación
    app.carga("pruebas.lfp")
    app.carga("pruebaAux.lfp")
    app.carga("pruebas2.lfp")
    #
    print()
    app.menu()
        