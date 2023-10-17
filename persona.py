class Persona:
    def __init__(self, doc, nom, ape, edad):
        self.doc = doc
        self.nom = nom
        self.ape = ape 
        self.edad = edad
        
    def __str__(self):
        return f"Documento: {self.doc}, Nombre: {self.nom}, Apellido: {self.ape}, Edad: {self.edad}"
    