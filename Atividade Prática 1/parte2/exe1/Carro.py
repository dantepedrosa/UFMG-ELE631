class Carro(Veiculo):
    def __init__(self, marca, modelo, ano_fabricacao, numero_portas)
        super().__init__(marca, modelo, ano_fabricacao)
        
        if (numero_portas != 2) or (numero_portas != 4):
            raise ValueError("numero_portas deve ser 2 ou 4!")
        
        self.numero_portas = numero_portas
        
    def exibirInfo():
        super().exibirInfo()
        print(f"Veículo: {self.marca} {self.modelo} — Ano: {self.ano_fabricacao} - Número de Portas: {self.numero_portas}")
    