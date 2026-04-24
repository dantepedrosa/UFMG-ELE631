from Emprestimo import Emprestimo

class EmprestimoLivro(Emprestimo):
    
    def __init__(self, nome_usuario : str, titulo : str):

        # Validação e definição de usuário
        if not isinstance(nome_usuario, str):
            raise TypeError("O nome do usuário deve ser uma string.")
        self.titulo = nome_usuario

        # Validação e definição de título
        if not isinstance(titulo, str):
            raise TypeError("O título do livro deve ser uma string.")
        self.titulo = titulo

    def registrar(self):
        # Verificar duplicidade de usuario
        pass

    def __eq__(self, other):
            # Verificação de tipo
            if not isinstance(other, Emprestimo):
                return NotImplemented
            
            return self.titulo == other.titulo and self.nome == other.nome