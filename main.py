from ManejadorHelados import ListaHelados
from ManejadorSabores import ListaSabores
def opcion0():
    print("Adiós")

def opcion1():
    tipo=int(input('Ingrese el tamaño del helado en gramos(100, 150, 250, 500, 1000): '))
    Vendidos.Registrar(tipo,Sabores)

def opcion2():
    Sabores.MasPedidos()

def opcion3():
    num=int(input('Ingresar numero de sabor: '))
    Sabores.Gramos(num)

def opcion4():
    tipo = int(input('Ingrese el tamaño del helado en gramos(100, 150, 250, 500, 1000): '))
    Vendidos.SaboresxCantidad(tipo)

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':

    Vendidos = ListaHelados()
    Sabores = ListaSabores()
    Sabores.CargaSabores()

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0 Salir")
        print("1. Vender Helado")
        print("2. 5 sabores mas pedidos")
        print("3. Conocer la cantidad de gramos vendidos de un sabor")
        print("4. Conocer el sabor más vendido de un tipo de helado")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
