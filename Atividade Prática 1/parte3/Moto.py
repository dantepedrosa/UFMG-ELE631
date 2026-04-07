from Entrega import Entrega

class Moto(Entrega):

    def __init__(self, codigo, distancia):
        super().__init__(codigo, distancia)

    def calcular_custo(self):
        return self.distancia
        