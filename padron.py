from persona import Persona
class Padron():

    def __init__(self):
        self.personas = []
    
    def agregar(self, persona:Persona):
        self.personas.append(persona)