class Capitulo:
    __titulo: ''
    __cantidadPaginas= 0

    def __init__(self,titulo,cantPag):
        self.__titulo=titulo
        self.__cantidadPaginas=cantPag

    def getTitulo(self):
        return self.__titulo
    def getCantPag(self):
        return self.__cantidadPaginas
    def getPag(self):
        return self.__cantidadPaginas