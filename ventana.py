from persona import Persona
from tkinter import *
from tkinter import messagebox
class Ventana:
    def __init__(self):
        self.window = Tk()
        self.window.title("Alta de persona")
        
        frame1 = Frame()
        frame1.pack(pady=20, padx=10)
        frame2 = Frame()
        frame2.pack(pady=5, padx=5)
        
        self.doc = StringVar()
        self.nom = StringVar()
        self.ape = StringVar()
        self.edad = StringVar()
        
        Label(frame1, text="Documento:").grid(row=0, column=0)
        Entry(frame1, textvariable=self.doc).grid(row=0, column=1)
        Label(frame1, text="Nombre:").grid(row=1, column=0)
        Entry(frame1, textvariable=self.nom).grid(row=1, column=1) 
        Label(frame1, text="Apellido:").grid(row=2, column=0)
        Entry(frame1, textvariable=self.ape).grid(row=2, column=1)
        Label(frame1, text="Edad:").grid(row=3, column=0)
        Entry(frame1, textvariable=self.edad).grid(row=3, column=1)
        
        Button(frame2, text="Aceptar", command=self.aceptar).pack(side="left", padx=10)
        Button(frame2, text="Cancelar", command=self.window.destroy).pack(side="right", padx=10)
        
    def aceptar(self):

        persona = Persona(int(self.doc.get()), self.nom.get(), self.ape.get(), int(self.edad.get()))
        messagebox.showinfo(title="Persona", message=persona)
        self.doc.set("")
        self.nom.set("")
        self.ape.set("")
        self.edad.set("")
    
    def mostrar(self):
        self.window.mainloop()