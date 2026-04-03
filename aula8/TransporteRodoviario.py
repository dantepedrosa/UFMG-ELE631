from Transporte import Transporte

class TransporteRodoviario(Transporte):
    
    def __init__(self, distancia, custo_por_km):
        
        if not isinstance(distancia, (int, float)):
            raise TypeError('distancia deve ser int ou float')
        if distancia <= 0:
            raise ValueError('distancia deve ser maior que zero')
        self.distancia = distancia

        if not isinstance(custo_por_km, (int, float)):
            raise TypeError('custo_por_km deve ser int ou float')
        if custo_por_km <= 0:
            raise ValueError('custo_por_km deve ser maior que zero')
        self.custo_por_km = custo_por_km
    
    def calcular_custo(self):
        return self.distancia * self.custo_por_km