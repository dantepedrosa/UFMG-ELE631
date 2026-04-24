from Emprestimo import Emprestimo
from BancoDeDados import BancoDeDados as BD

class EmprestimoLivro(Emprestimo):


    def registrar(self):

        self.prazoDevolucao = 7
        BD.registrar_Emprestimo(self)

    def to_dict(self):
        return {
            "nome_usuario": self.nome_usuario,
            "titulo": self.titulo,
            "prazoDevolucao": self.prazoDevolucao
        }


