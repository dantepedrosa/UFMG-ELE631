from abc import ABC, abstractmethod

class Plano(ABC):
    
    @abstractmethod
    def calcular_mensalidade(self):
        pass