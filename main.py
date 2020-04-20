from manejadorEmails import Lista

if __name__ == '__main__':

    listaCorreos = Lista()
#inciso1
    print('Ingrese nombre y correo electronico')
    nombre = input('Nombre:')
    cuenta = input('Cuenta:')
    contrasenia = input('Contraseña:')
    listaCorreos.agregar(cuenta,contrasenia)
    print('Estimado '+nombre+' te enviaremos tus mensajes a la direccion {}'.format(listaCorreos.getEmail(0)))
#inciso2
    print('Ingrese su contraseña actual:')
    actual = input()
    mail = listaCorreos.getEmail(0)
    b = listaCorreos.modifContra(mail,actual)
    if (b == 0):
        print('Se realizo el cambio de contraseña')
    else:
        print('Contraseña incorrecta')
#inciso3
    print('Ingrese el correo electronico:')
    cuenta = input()
    listaCorreos.agregar(cuenta,0)
#inc#iso4
    import csv
    listaArchivo = Lista()
    correo = ''
    archivo = open('correos.csv')
    reader = csv.reader(archivo,delimiter=',')
    for fila in reader:
        correo = fila
        listaCorreos.agregar(correo[0],0)
        listaArchivo.agregar(correo[0],0)
    archivo.close()
    print('Lista de correos:')
    listaCorreos.mostrarDatos()
    print('Ingrese el dominio a buscar:')
    dom = input()
    contador = listaArchivo.contadorDominio(dom)
    print('El dominio aparece: {} veces'.format(contador))
