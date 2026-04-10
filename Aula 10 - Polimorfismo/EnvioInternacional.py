from Envio import Envio

class EnvioInternacional(Envio):

    def __init__(self, distancia, peso, taxa_importacao):

        # Validação de distância
        if not isinstance(distancia, (int, float)):
            raise TypeError("A distância deve ser um valor numérico.")
        if distancia <= 0:
            raise ValueError("A distância deve ser maior que zero.")

        # Validação de peso
        if not isinstance(peso, (int, float)):
            raise TypeError("O peso deve ser um valor numérico.")
        if peso <= 0:
            raise ValueError("O peso deve ser maior que zero.")

        # Validação de taxa de importação
        if not isinstance(taxa_importacao, (int, float)):
            raise TypeError("A taxa de importação deve ser um valor numérico.")
        if taxa_importacao < 0:
            raise ValueError("A taxa de importação não pode ser negativa.")

        self.distancia = distancia
        self.peso = peso
        self.taxa_importacao = taxa_importacao

    def calcular_frete(self):
        return (self.distancia * 2.0) + (self.peso * 3.0) + self.taxa_importacao