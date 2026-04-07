from Entrega import Entrega
from Caminhao import Caminhao
from Moto import Moto

if __name__ == '__main__':

    # Testa entrega Caminhão
    entrega1 = Caminhao(codigo=1, distancia=100, taxa_adicional=50)
    custo = entrega1.calcular_custo()
    assert custo == 150 , f"O custo calculado foi {custo}, mas era esperado 150"

    # Testa entrega Moto
    entrega2 = Moto(codigo=2, distancia=120)
    custo = entrega2.calcular_custo()
    assert custo == 120 , f"O custo calculado foi {custo}, mas era esperado 120"

    # Testa criação de entrega genérica
    try:
        entrega3 = Entrega(codigo=3, distancia=80)
    except Exception as e:
        print(f"Erro intencional detectado: {e}")