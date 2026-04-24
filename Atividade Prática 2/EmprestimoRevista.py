from Emprestimo import Emprestimo
from BancoDeDados import BancoDeDados as BD

class EmprestimoRevista(Emprestimo):
    
    def __init__(self, nome_usuario : str, titulo : str, edicao):
        super().__init__(nome_usuario, titulo)

        # Validação e definição de edição
        if not isinstance(edicao, (int, str)):
            raise TypeError("A edição do livro deve ser um inteiro ou uma string.")
        self.edicao = edicao

    def registrar(self):
        self.prazoDevolucao = 2
        BD.registrar_Emprestimo(self)

    def to_dict(self):
        return {
            "nome_usuario": self.nome_usuario,
            "titulo": self.titulo,
            "edicao": self.edicao,
            "prazoDevolucao": self.prazoDevolucao
        }
    