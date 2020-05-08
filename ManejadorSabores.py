import csv
from Sabor import Sabor

class ListaSabores:
    __sabores=[]

    def __init__(self):
        self.__sabores=[]

    def CargaSabores(self):
        archivo = open('sabores.csv')
        reader=csv.reader(archivo,delimiter=',')
        for fila in reader:
            num=fila[0]
            nom=fila[1]
            desc=fila[2]
            unSabor=Sabor(num,nom,desc)
            self.__sabores.append(unSabor)
        archivo.close()

    def __str__(self):
        cadena='Numero   Nombre          Descripcion\n'
        for i,sabor in enumerate(self.__sabores):
            cadena += str(sabor)+'\n'
        return cadena

    def ContadorSumador(self,numero,gramos):
        indice=numero-1
        self.__sabores[indice].setContador()
        self.__sabores[indice].setGramos(gramos)

    def __gt__(self,otroSabor):
        return self.__sabores.getContador()<otroSabor.getContador()

    def MasPedidos(self):
        new=sorted(self.__sabores, key=lambda x:x.getContador(), reverse=True)
        for i in range(5):
            print(new[i])

    def Gramos(self,numero):
        indice=numero-1
        print('{}gr'.format(self.__sabores[indice].getGramos()))