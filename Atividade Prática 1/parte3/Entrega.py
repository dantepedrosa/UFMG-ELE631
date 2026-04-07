from abc import ABC, abstractmethod

class Entrega(ABC):

    def __init__(self, codigo, distancia):
        
        # Validação de dados de codigo
        if not isinstance(codigo, int):
            raise TypeError("O codigo deve ser um valor inteiro.")
        if  codigo <= 0:
            raise ValueError("O codigo deve ser maior que zero.")
        
        # Validação de dados de distancia
        if not (isinstance(distancia, float) or isinstance(distancia, int)):
            raise TypeError("A distancia deve ser um número.")
        if  distancia <= 0:
            raise ValueError("A distancia deve ser maior que zero.")
        
        # Definição de variáveis
        self.codigo = codigo      
        self.distancia = distancia

    # Método abstrato a ser implementado
    @abstractmethod
    def calcular_custo(self):
        pass