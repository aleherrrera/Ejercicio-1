class Email:

    __cuenta=''
    __dominio=''
    __tipo=''
    __contrasenia=''

    def __init__(self,cuenta,dominio,tipo,contrasenia=0):
        self.__cuenta=cuenta
        self.__dominio=dominio
        self.__tipo=tipo
        self.__contrasenia=contrasenia

    def retornaEmail(self):
        print('{}@{}.{}'.format(self.__cuenta,self.__dominio,self.__tipo))

    def getDominio(self):
        return self.__dominio

    def modifContraseña(self,actual):
        b = -1
        if (actual == self. __contrasenia):
            b = 0
            nueva = input('Nueva:')
            self.__contrasenia=nueva
        return b

    def __str__(self):
        return ''+self.__cuenta+'@'+self.__dominio+'.'+self.__tipo

    def crearCuenta(self,a,b,c,contrasenia):
        self.__cuenta=a
        self.__dominio=b
        self.__tipo=c
        self.__contrasenia=contrasenia

    def getContraseña(self):
        return self.__contrasenia