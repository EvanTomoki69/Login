from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
from turtle import width
import _mysql_connector

#ventana de ingreso
w=Tk()
w.geometry('550x675+0+0')
w.title('Tu Cuenta MBX')
w.resizable(0,0)

j=0
r=0
for i in range(100):
    c=str(202020+r)
    Frame(w,width=25, height=675,bg='#ff0000'+c).place(x=j,y=0) #define ancho, alto y color con código HTML ff0000
    j=j+10
    r=r+1

#altura del cuadro interior
Frame(w,width=500, height=620,bg='white').place(x=25,y=25)

#marca1
l1=Label(w,text='MBX', bg='red')
l=('impact', 50) 
l1.config(font=l)
l1.place(x=225,y=70)

#etiqueta2 email y fuente 
l2=Label(w,text='Email', bg='white')
l=('times', 15) 
l2.config(font=l)
l2.place(x=100,y=200)

#cuadro de texto email
e2=Entry(w,width=35,border=0)
e2.config(font=l)
e2.place(x=100,y=225)

#etiqueta3 contraseña
l3=Label(w,text='Contraseña', bg='white')
l=('times', 15) 
l3.config(font=l)
l3.place(x=100,y=290)

#cuadro de texto para anotar contraseña
e3=Entry(w,width=35,border=0)
e3.config(font=l)
e3.place(x=100,y=315)

Frame(w,width=300,height=2,bg="#141414").place(x=100,y=250)
Frame(w,width=300,height=2,bg="#141414").place(x=100,y=340)

#define el comando de acceso y los atributos del nombre de usuario y contraseña
def cmd():
    if e2.get()=='user@mbx.com' and e3.get()=='admin':
        messagebox.showinfo("Ingreso Exitoso","   Bienvenido   ")
        q=Tk()
        q.mainloop()
    else:
        messagebox.showinfo("Ingreso Fallido","   Porfavor intente de nuevo   ")

#boton de acceso
Button(w,width=40,height=4,fg='black',bg='#ffffff',border=3,command=cmd,text="A C C E S O").place(x=135,y=450)

w.mainloop()