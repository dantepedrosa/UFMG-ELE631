import unittest
from Transporte import Transporte
from TransporteAereo import TransporteAereo
from TransporteRodoviario import TransporteRodoviario

class TestTransportMethods(unittest.TestCase):

    def test_CalculaTransporteRodoviario(self):
        transporte = TransporteRodoviario(distancia=100, custo_por_km=0.5)
        custo = transporte.calcular_custo()
        self.assertEqual(custo, 50)

    def test_CalculaTransporteAereo(self):
        transporte = TransporteAereo(peso=10, custo_por_kg=5, taxa_fixa=20)
        custo = transporte.calcular_custo()
        self.assertEqual(custo, 70)

    def test_InstanciaClasseAbstrata(self):
        with self.assertRaises(TypeError):
            transporte = Transporte()
    
    def test_InstanciaClasseSemImplementacao(self):
        class TransporteIncompleto(Transporte):
            pass
        
        with self.assertRaises(TypeError):
            transporte = TransporteIncompleto()

if __name__ == '__main__':
    unittest.main()