from Plano import Plano

class PlanoBasico(Plano):

    def __init__(self, taxa_fixa):

        # Validação de taxa_fixa
        if not isinstance(taxa_fixa, (int, float)):
            raise TypeError("A taxa_fixa deve ser um valor numérico.")
        if taxa_fixa <= 0:
            raise ValueError("A taxa_fixa deve ser maior que zero.")

        self.taxa_fixa = taxa_fixa

    def calcular_mensalidade(self):
        return self.taxa_fixa