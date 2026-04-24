from Emprestimo import Emprestimo

class BancoDeDados:
    def __init__(self):
        self.__emprestimos = []

    def exportarDados(self):
        pass

    def importarDados(self, path: str):
        pass

    def verificaDuplicidade(self, emprestimo : Emprestimo):
        # Validação de tipo
        if not isinstance(emprestimo, Emprestimo):
            raise TypeError("emprestimo deve ser do tipo Emprestimo.")
        
        return any(emprestimo == e for e in self.__emprestimos)


    def registrar_Emprestimo(self, emprestimo : Emprestimo):
        if not isinstance(emprestimo, Emprestimo):
            raise TypeError("emprestimo deve ser do tipo Emprestimo.")
        
