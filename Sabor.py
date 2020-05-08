
class Sabor:
    __numero=0
    __nombre=''
    __descripcion=''
    __contador=0
    __gramos=0.0

    def __init__(self,numero,nombre,descripcion,contador=0,gramos=0.0):
        self.__nombre=nombre
        self.__numero=numero
        self.__descripcion=descripcion
        self.__contador=contador
        self.__gramos=gramos

    def getNombre(self):
        return self.__nombre
    def getNumero(self):
        return self.__numero
    def getDescripcion(self):
        return self.__descripcion
    def getContador(self):
        return self.__contador
    def getGramos(self):
        return self.__gramos

    def setContador(self):
        self.__contador+=1
    def setGramos(self,gramos):
        self.__gramos+=gramos

    def __str__(self):
        cadena= '{:8} {:18} {}'.format(self.getNumero(),self.getNombre(),self.getDescripcion(),)
        return cadena