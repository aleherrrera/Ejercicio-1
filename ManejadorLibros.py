import csv
from Libro import Libro

class ListaLibros:
    __libros=[]

    def __init__(self):
        self.__libros=[]

    def cargarLibros(self):
        archivo = open('libros.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera=True
        for fila in reader:
            if bandera:
                id = int(fila[0])
                titulo = str(fila[1])
                autor = str(fila[2])
                editorial = str(fila[3])
                isbn = int(fila[4])
                cantCap = int(fila[5])
                unLibro=Libro(id,titulo,autor,editorial,isbn,cantCap)
                bandera = not bandera
                i=0
            else:
                if i < cantCap:
                    titCap = str(fila[0])
                    cantPag = int(fila[1])
                    i+=1
                    unLibro.addCapitulo(titCap,cantPag)
                if i == cantCap:
                    bandera= True
                    self.__libros.append(unLibro)

    def Busca(self,id):
        i=0
        c=len(self.__libros)
        while i<c and id != self.__libros[i].getId():
            i+=1
        if i < c:
            return i

    def InfoLibro(self):
        id=int(input('Ingrese Id del libro: '))
        i=self.Busca(id)
        if i !=None:
            self.__libros[i].mostrarLibro()
        else:
            print('Id ingresada no corresponde a un libro')

    def BuscarPalabra(self):
        palabra=str(input('Ingrese palabra: '))
        c=len(self.__libros)
        bandera=True
        for i in range(c):
            cadena = self.__libros[i].getTitulo()
            b=cadena.find(palabra)
            if b>=0:
                bandera=not bandera
                print('Titulo: {}\nAutor: {}'.format(self.__libros[i].getTitulo(),self.__libros[i].getAutor()))
            else:
                j=0
                cant=self.__libros[i].getCantCaps()
                while j < cant and b == -1:
                    b = self.__libros[i].BuscarCaps(j,palabra)
                    j+=1
                if b >= 0:
                    bandera = not bandera
                    print('Titulo: {}\nAutor: {}'.format(self.__libros[i].getTitulo, self.__libros[i].getAutor()))
        if bandera==True:
            print('No se encontro la palabra ingresada')