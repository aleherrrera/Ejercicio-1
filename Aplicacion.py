from tkinter import *
from tkinter import ttk,font,messagebox

class Aplicacion():
    __ventana=None
    __centimetros=None
    __kilogramos=None

    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.resizable(0,0)


        fuente=font.Font(size=8,weight='bold')
        fuente1=font.Font(size=10)


        #variables
        self.__centimetros = StringVar()
        self.__kilogramos = StringVar()
        self.__mensaje1 = StringVar()
        self.__mensaje2 = StringVar()
        self.__mensaje3 = StringVar()

        #ventatna principal
        self.marco=ttk.Frame(self.__ventana,borderwidth=2,padding=(10,10,10,10))


        #primera linea
        self.marco1=ttk.Frame(self.marco,borderwidth=1,relief='raised',padding=(0,0))
        self.alturaLbl=ttk.Label(self.marco,text='Altura:',font=fuente,padding=(5,5))
        self.ctext1=ttk.Entry(self.marco,textvariable=self.__centimetros,width=20)
        self.cmLbl=ttk.Label(self.marco1,text='cm',padding=(0,0))

        #segunda linea
        self.marco2=ttk.Frame(self.marco,borderwidth=1,relief='raised',padding=(0,0))
        self.pesoLbl=ttk.Label(self.marco,text='Peso:',font=fuente,padding=(5,5))
        self.ctext2=ttk.Entry(self.marco,textvariable=self.__kilogramos,width=20)
        self.kgLbl=ttk.Label(self.marco2,text='kg',padding=(2,0))

        #tercer linea
        self.boton1 = Button(self.marco, text='Calcular', command=self.calcular, bg='lightgreen', fg='white')
        self.boton2 = Button(self.marco, text='Limpiar', command=self.limpiar, bg='lightgreen', fg='white')

        #cuarta linea
        self.marco3=ttk.Frame(self.marco,borderwidth=1,padding=(0,0))
        self.etiq1=ttk.Label(self.marco3,textvariable=self.__mensaje1,foreground='green')
        self.etiq2=ttk.Label(self.marco3,textvariable=self.__mensaje2,font=fuente,foreground='green')
        self.etiq3=ttk.Label(self.marco3,textvariable=self.__mensaje3,font=fuente1,foreground='green')

        #separadores
        self.separ1= ttk.Separator(self.marco,orient=HORIZONTAL)
        self.separ2= ttk.Separator(self.marco,orient=HORIZONTAL)
        self.separ3=ttk.Separator(self.marco,orient=HORIZONTAL)
        self.separ4=ttk.Separator(self.marco,orient=VERTICAL)

        #UBICACION EN LA GRILLA
        self.marco.columnconfigure(0, weight=1)
        self.marco.rowconfigure(0, weight=1)
        self.marco.grid(column=0,row=0,sticky=(N,E,W,S))

        #FILA1
        self.separ1.grid(column=0,row=1,columnspan=7)

        #FILA2
        self.marco1.grid(column = 6, row = 2, sticky = W)
        self.alturaLbl.grid(column=0,row=2)
        self.ctext1.grid(column=1,row=2,columnspan=5,sticky=(W,E))
        self.cmLbl.grid(column = 0, row = 0, sticky = W)

        #FILA3
        self.separ2.grid(column=0,row=3,columnspan=7)

        #FILA4
        self.marco2.grid(column = 6, row = 4, sticky = W)
        self.pesoLbl.grid(column=0, row=4)
        self.ctext2.grid(column=1, row=4, columnspan=5,sticky=(W,E))
        self.kgLbl.grid(column=0, row=0,sticky=W)

        #FILA5
        self.separ3.grid(column=0,row=5,columnspan=7)

        #FILA6
        self.boton1.grid(column=1,row=5,columnspan=2,sticky=W)
        self.separ4.grid(column=3,row=5)
        self.boton2.grid(column=4,row=5,columnspan=2)

        #FILA7
        self.marco3.columnconfigure(0,weight=1)
        self.marco3.rowconfigure(0, weight=1)
        self.marco3.grid(column = 2, row = 6,columnspan=2,rowspan=2, sticky = W)
        self.etiq1.grid(column=0,row=0,columnspan=2)
        self.etiq2.grid(column=2,row=0)
        self.etiq3.grid(column=1,row=1)

        self.ctext1.focus_set()
        self.__ventana.mainloop()

    def calcular(self):
        try:
            altura=float(float(self.__centimetros.get())/100)
            peso=float(self.__kilogramos.get())
            imc=peso/(altura*altura)
            cadena='%.2f Kg/m2'%(imc)
            self.__mensaje1.set('Tu Indice de Masa Corporal (IMC) es ')
            self.__mensaje2.set(cadena)
            self.composicion(imc)
        except ValueError:
            messagebox.showerror('Error',message='Ingresar valores numéricos')
            self.__kilogramos.set('')
            self.__centimetros.set('')
            self.ctext1.focus_set()
            self.ctext2.focus_set()

    def composicion(self,imc):
        if imc < 18.5:
            self.__mensaje3.set('Peso inferior al normal')
        else:
            if imc >= 18.5 and imc < 24.9:
                self.__mensaje3.set('Normal')
            else:
                if imc >= 25 and imc < 29.9:
                    self.__mensaje3.set('Peso superior al normal')
                else:
                    if imc >= 30:
                        self.__mensaje3.set('Obesidad')

    def limpiar(self):
        self.__kilogramos.set('')
        self.__centimetros.set('')
        self.__mensaje1.set('')
        self.__mensaje2.set('')
        self.__mensaje3.set('')
        self.ctext1.focus_set()
