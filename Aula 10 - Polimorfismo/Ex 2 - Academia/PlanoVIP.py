from Plano import Plano

class PlanoVIP(Plano):

    def __init__(self, taxa_fixa, quantidade_aulas_extras, taxa_personal):

        # Validação de taxa_fixa
        if not isinstance(taxa_fixa, (int, float)):
            raise TypeError("A taxa_fixa deve ser um valor numérico.")
        if taxa_fixa <= 0:
            raise ValueError("A taxa_fixa deve ser maior que zero.")

        # Validação de quantidade_aulas_extras
        if not isinstance(quantidade_aulas_extras, int):
            raise TypeError("A quantidade de aulas extras deve ser um valor inteiro.")
        if quantidade_aulas_extras < 0:
            raise ValueError("A quantidade de aulas extras não pode ser negativa.")

        # Validação de taxa_personal
        if not isinstance(taxa_personal, (int, float)):
            raise TypeError("A taxa personal deve ser um valor numérico.")
        if taxa_personal <= 0:
            raise ValueError("A taxa personal deve ser maior que zero.")

        self.taxa_fixa = taxa_fixa
        self.quantidade_aulas_extras = quantidade_aulas_extras
        self.taxa_personal = taxa_personal

    def calcular_mensalidade(self):
        return self.taxa_fixa + (self.quantidade_aulas_extras * 15.0) + self.taxa_personal