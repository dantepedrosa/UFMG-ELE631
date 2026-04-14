class Bolo:
    def __init__(self, nome, recheio, massa, temCobertura):
        self.nome = nome
        self.recheio = recheio
        self.massa = massa
        self.temCobertura = temCobertura


    def __str__(self):
        return f"Nome: {self.nome}, Recheio: {self.recheio}, Massa: {self.recheio}, Tem cobertura: {self.temCobertura}"
