from Capitulo import Capitulo

class Libro:
    __idLibro= 0
    __titulo=''
    __autor=''
    __editorial=''
    __isbn=0
    __cantidadCapitulos=0
    __capitulos=None

    def __init__(self,id,titulo,autor,editorial,isbn,cant):
        self.__idLibro=id
        self.__titulo=titulo
        self.__autor=autor
        self.__editorial=editorial
        self.__isbn=isbn
        self.__cantidadCapitulos=cant
        self.__capitulos=[]

    def addCapitulo(self,unCap,pag):
        Cap=Capitulo(unCap,pag)
        self.__capitulos.append(Cap)

    def getId(self):
        return self.__idLibro
    def getTitulo(self):
        return self.__titulo
    def getAutor(self):
        return self.__autor
    def getCantCaps(self):
        return self.__cantidadCapitulos

    def getTotalPag(self):
        total=0
        for i in range(self.__cantidadCapitulos):
            total+=self.__capitulos[i].getPag()
        return total

    def BuscarCaps(self,j,palabra):
        cadena = self.__capitulos[j].getTitulo()
        b = cadena.find(palabra)
        return b

    def mostrarLibro(self):
        print('Titulo: {}'.format(self.__titulo))
        print('Capitulos:')
        for i, cap in enumerate(self.__capitulos):
            print('{}'.format(cap.getTitulo()))
        print('Total de paginas: {}'.format(self.getTotalPag()))