import tkinter as tk
from persona import Persona
from tkinter import ttk
from tkinter import messagebox
class Ventana:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Falta de persona")
        self.frame1 = ttk.Frame(self.window, padding=20)
        self.frame2 = ttk.Frame(self.window, padding=10)
        self.label_doc = ttk.Label(self.frame1, text="Documento:")
        self.doc = tk.Entry(self.frame1)
        self.label_nom = ttk.Label(self.frame1, text="Nombre:")
        self.nom = tk.Entry(self.frame1)       
        self.label_ape = ttk.Label(self.frame1, text="Apellido:")
        self.ape = tk.Entry(self.frame1)
        self.label_edad = ttk.Label(self.frame1, text="Edad:  ")
        self.edad = tk.Entry(self.frame1)
        self.btn_aceptar = ttk.Button(self.frame2, text="Aceptar", command=self.boton_aceptar)
        self.btn_cancelar = ttk.Button(self.frame2, text="Cancelar", command=self.boton_cancelar)
        self.frame1.pack()
        self.frame2.pack()
        self.label_doc.grid(row=0, column=0)
        self.doc.grid(row=0, column=1)
        self.label_nom.grid(row=1, column=0)
        self.nom.grid(row=1, column=1)
        self.label_ape.grid(row=2, column=0)
        self.ape.grid(row=2, column=1)
        self.label_edad.grid(row=3, column=0)
        self.edad.grid(row=3, column=1)
        self.btn_aceptar.pack(side="left")
        self.btn_cancelar.pack(side="right")
        
    def boton_aceptar(self):
        doc = self.doc.get()
        nom = self.nom.get()
        ape = self.ape.get()
        edad = self.edad.get()
        persona = Persona(doc, nom, ape, edad)
        messagebox.showinfo(title="Persona", message=persona)

        

    def boton_cancelar(self):
        self.window.destroy()
    
    def mostrar(self):
        self.window.mainloop()