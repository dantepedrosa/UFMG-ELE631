from Entrega import Entrega

class Caminhao(Entrega):

    def __init__(self, codigo, distancia, taxa_adicional):
        super().__init__(codigo, distancia)

        # Validação de dados de distancia
        if not (isinstance(taxa_adicional, float) or isinstance(taxa_adicional, int)):
            raise TypeError("A taxa_adicional deve ser um número.")
        if  taxa_adicional < 0:
            raise ValueError("A taxa_adicional não pode ser negativa.")
        
        self.taxa_adicional = taxa_adicional

    def calcular_custo(self):
        return self.distancia + self.taxa_adicional
        