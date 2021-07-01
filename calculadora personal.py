from tkinter import *
import tkinter

class calculadora:

    def inicio(self):
        ventana = Tk()
        ventana.title("Calculadora")
        ventana.geometry("300x400")
        ventana.resizable(0,0)

        #pantalla
        numero = IntVar(), True
        pantalla = Entry(ventana, textvariable=numero, font=("Arial", 14))
        pantalla.place(x=15, y=20, width=270 , height=70)

        #funcion de calculos
        def __calculo(operacion):
            if operacion != '':
                try:
                    resultado = str(eval(operacion))
                except ZeroDivisionError:
                    resultado = 'ERROR'
                pantalla.delete(0, tkinter.END)
                pantalla.insert(tkinter.END, resultado)
            else:
                pass

        #botones fila 1
        boton_1 = Button(ventana, text="1", command= lambda: pantalla.insert(tkinter.END, "1"))
        boton_1.place(x=15, y=110, width=50, height=60)

        boton_2 = Button(ventana, text="2", command= lambda: pantalla.insert(tkinter.END, "2"))
        boton_2.place(x=70, y=110, width=50, height=60)

        boton_3 = Button(ventana, text="3", command= lambda: pantalla.insert(tkinter.END, "3"))
        boton_3.place(x=125, y=110, width=50, height=60)

        #botones fila 2
        boton_4 = Button(ventana, text="4", command= lambda: pantalla.insert(tkinter.END, "4"))
        boton_4.place(x=15, y=175, width=50, height=60)

        boton_5 = Button(ventana, text="5", command= lambda: pantalla.insert(tkinter.END, "5"))
        boton_5.place(x=70, y=175, width=50, height=60)

        boton_6 = Button(ventana, text="6", command= lambda: pantalla.insert(tkinter.END, "6"))
        boton_6.place(x=125, y=175, width=50, height=60)

        #botones fila 3
        boton_7 = Button(ventana, text="7", command= lambda: pantalla.insert(tkinter.END, "7"))
        boton_7.place(x=15, y=240, width=50, height=60)

        boton_8 = Button(ventana, text="8", command= lambda: pantalla.insert(tkinter.END, "8"))
        boton_8.place(x=70, y=240, width=50, height=60)

        boton_9 = Button(ventana, text="9", command= lambda: pantalla.insert(tkinter.END, "9"))
        boton_9.place(x=125, y=240, width=50, height=60)

        #botones fila 4
        boton_0 = Button(ventana, text="0", command= lambda: pantalla.insert(tkinter.END, "0"))
        boton_0.place(x=70, y=305, width=50, height=60)

        #botones especiales
        boton_limpiar = Button(ventana, text="Clear", command= lambda: pantalla.delete(0, tkinter.END))
        boton_limpiar.place(x=185, y = 110, width=80, height=60)

        boton_igual = Button(ventana, text="=", command=lambda: __calculo(pantalla.get()))
        boton_igual.place(x=185, y=305, width=50, height=60)

        boton_mas = Button(ventana, text="+", command= lambda: pantalla.insert(tkinter.END, "+"))
        boton_mas.place(x=15, y=305, width=50, height=60)
        
        boton_menos = Button(ventana, text="-", command= lambda: pantalla.insert(tkinter.END, "-"))
        boton_menos.place(x=125, y=305, width=50, height=60)

        boton_mult = Button(ventana, text="*", command= lambda: pantalla.insert(tkinter.END, "*"))
        boton_mult.place(x=185, y=240, width=50, height=60)

        boton_div = Button(ventana, text="/", command= lambda: pantalla.insert(tkinter.END, "/"))
        boton_div.place(x=185, y=175, width=50, height=60)

        ventana.mainloop()

if __name__ == '__main__':
    calculadora().inicio()