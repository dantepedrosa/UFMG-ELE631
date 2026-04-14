class Veiculo:
    def __init__(self, marca, modelo, ano_fabricacao):
        
        if (marca == "" ) or (modelo == "") :
            raise ValueError("A marca e modelo não podem estar vazios!")
        
        self.marca = marca
        self.modelo = modelo
        
        if not isinstance(ano_fabricacao, int):
            raise TypeError("O ano_fabricacao deve ser um inteiro entre 1886 e 2025.")
        
        if (ano_fabricacao < 1986) or (ano_fabricacao > 2025):
            raise ValueError("O ano_fabricacao deve ser um inteiro entre 1886 e 2025.")
            
        self.ano_fabricacao = ano_fabricacao
            
    def exibirInfo(self):
        print(f"Veículo: {self.marca} {self.modelo} — Ano: {self.ano_fabricacao}")