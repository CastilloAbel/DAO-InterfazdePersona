from tkinter import *
from tkinter.ttk import Treeview
class ListadoPersonas:
    
    def __init__(self, padron):
        self.ventana = Tk()
        
        grilla = Treeview(self.ventana, columns=("A", "B", "C", "D"), height=200)
        grilla.column("#0", width=0)
        grilla.column("A", width=50)
        grilla.column("B", width=150)
        grilla.column("C", width=150)
        grilla.column("D", width=50)
        grilla.heading("A", text="Documento")
        grilla.heading("B", text="Nombre")
        grilla.heading("C", text="Apellido")
        grilla.heading("D", text="Edad")
        grilla.pack(fill=BOTH)
        for p in padron.personas:
            grilla.insert("", END, values=(p.doc, p.nom, p.ape, p.edad))
            
    def mostrar(self):
        self.ventana.mainloop()