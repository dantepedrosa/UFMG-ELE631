from Envio import Envio

class EnvioSimples(Envio):

    def __init__(self, distancia):

        # Validação de distância
        if not isinstance(distancia, (int, float)):
            raise TypeError("A distância deve ser um valor numérico.")
        if distancia <= 0:
            raise ValueError("A distância deve ser maior que zero.")

        self.distancia = distancia

    def calcular_frete(self):
        return self.distancia * 1.0