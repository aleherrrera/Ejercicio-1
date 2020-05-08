from Helado import Helado

class ListaHelados:
    __helados=[]

    def __init__(self):
        self.__helados=[]

    def Registrar(self,tipo,Sabores):
        i=0
        while i==0:
            cantSabores=int(input('Cuantos sabores desea(max=4)?: '))
            if cantSabores<=4:
                unHelado=Helado(tipo,cantSabores,Sabores)
                self.__helados.append(unHelado)
                i=1
            else:
                print('Cantidad de sabores incorrectos')
    def SaboresxCantidad(self,gramos):
        for i, helado in enumerate(self.__helados):
            if gramos==helado.getGramos():
                print(helado.getSabores())





