from Emails import Email

class Lista:

    __emails = []
    def __init__(self):
        self.__emails=[]

    def crear(self,cuenta,contrasenia):
        a, b = cuenta.split('@')
        b, c = b.split('.')
        correo = Email(a,b,c,contrasenia)
        return correo

    def agregar(self,unEmail,contrasenia):
        c=self.crear(unEmail,contrasenia)
        self.__emails.append(c)

    def mostrarDatos(self):
        a = Email('','','','')
        for a in self.__emails:
            print(a)

    def getEmail(self,indice):
        return self.__emails[indice]

    def modifContra(self,mail,actual):
        b = mail.modifContraseña(actual)
        return b
    def retornaDominio(self,mail):
        a = mail.getDominio()
        return a
    def contadorDominio(self,dom):
        contador = 0
        for i in range(len(self.__emails)):
            mail = self.getEmail(i)
            print(mail)
            dominio = self.retornaDominio(mail)
            if dom == dominio:
                contador += 1
        return contador