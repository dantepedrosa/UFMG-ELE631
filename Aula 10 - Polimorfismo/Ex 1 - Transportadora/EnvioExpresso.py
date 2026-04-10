from Envio import Envio

class EnvioExpresso(Envio):

    def __init__(self, distancia, peso):

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

        self.distancia = distancia
        self.peso = peso

    def calcular_frete(self):
        return (self.distancia * 1.5) + (self.peso * 2.0)