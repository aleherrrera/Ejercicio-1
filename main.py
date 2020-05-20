from ManejadorLibros import ListaLibros

def opcion0():
    print("Adiós")

def opcion1():
    Lista.InfoLibro()

def opcion2():
    Lista.BuscarPalabra()

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':

    Lista = ListaLibros()
    Lista.cargarLibros()

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0 Salir")
        print("1. Mostrar libro")
        print("2. Buscar libro por palabra")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú