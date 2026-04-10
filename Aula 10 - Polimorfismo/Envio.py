from abc import ABC, abstractmethod

class Envio(ABC):

    @abstractmethod
    def calcular_frete(self):
        pass