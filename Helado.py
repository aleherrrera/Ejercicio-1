from ManejadorSabores import ListaSabores

class Helado:
    __gramos=0
    __sabores=[]

    def __init__(self,gramos,cantSabor,Sabores):
        self.__gramos=gramos
        grSabor=gramos/cantSabor
        print(Sabores)
        for i in range(cantSabor):
            numSabor=int(input('Ingrese numero de sabor:'))
            self.__sabores.append(numSabor)
            Sabores.ContadorSumador(numSabor,grSabor)

    def getGramos(self):
        return self.__gramos
    def getSabores(self):
        cadena=''
        for i,sabor in enumerate(self.__sabores):
            cadena+=str(sabor)+'\n'
        return cadena
