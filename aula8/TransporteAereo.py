from Transporte import Transporte

class TransporteAereo(Transporte):

    def __init__(self, peso, custo_por_kg, taxa_fixa):
        
        if not isinstance(peso, (int, float)) or peso <= 0:
            raise ValueError("peso must be a positive integer")
        self.peso = peso

        if not isinstance(custo_por_kg, (int, float)) or custo_por_kg <= 0:
            raise ValueError("custo_por_kg must be a positive integer")
        self.custo_por_kg = custo_por_kg

        if not isinstance(taxa_fixa, (int, float)):
            raise ValueError("taxa_fixa must be a positive integer")
        self.taxa_fixa = taxa_fixa
    
    def calcular_custo(self):
        return (self.peso * self.custo_por_kg) + self.taxa_fixa