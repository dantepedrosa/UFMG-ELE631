'''
• Instruções adicionais:
○ Na função main(), crie pelo menos um objeto de cada subclasse com dados fictícios.
○ Chame exibirInfo() para cada objeto e observe como cada subclasse exibe suas
informações de forma especializada.
○ Crie testes que cubram: ano inválido (ex: 1800 ou 3000), marca vazia, número de portas
inválido (ex: 3) e cilindradas negativas.
'''

from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto

def main():
    # Criando objetos de cada subclasse com dados fictícios
    carro1 = Carro("Toyota", "Corolla", 2020, 4)
    moto1 = Moto("Honda", "CB500", 2019, 500)

    # Exibindo informações de cada objeto
    print("Informações do Carro:")
    carro1.exibirInfo()
    print("\nInformações da Moto:")
    moto1.exibirInfo()

    # Testes para casos inválidos
    print("\nTestes para casos inválidos:")
    
    # Ano inválido
    try:
        carro_invalido = Carro("Ford", "Fiesta", 1800, 4)
        carro_invalido.exibirInfo()
    except ValueError as e:
        print(f"Erro: {e}")

    # Marca vazia
    try:
        moto_invalida = Moto("", "CBR600", 2020, 600)
        moto_invalida.exibirInfo()
    except ValueError as e:
        print(f"Erro: {e}")

    # Número de portas inválido
    try:
        carro_invalido2 = Carro("Chevrolet", "Onix", 2021, 3)
        carro_invalido2.exibirInfo()
    except ValueError as e:
        print(f"Erro: {e}")

    # Cilindradas negativas
    try:
        moto_invalida2 = Moto("Yamaha", "MT-07", 2020, -700)
        moto_invalida2.exibirInfo()
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()