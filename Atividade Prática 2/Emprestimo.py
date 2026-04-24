from abc import ABC, abstractmethod

class Emprestimo(ABC):

    def __init__(self, nome_usuario : str, titulo : str):
        # Validação e definição de usuário
        if not isinstance(nome_usuario, str):
            raise TypeError("O nome do usuário deve ser uma string.")
        self.titulo = nome_usuario

        # Validação e definição de título
        if not isinstance(titulo, str):
            raise TypeError("O título da revista deve ser uma string.")
        self.titulo = titulo

        self.prazoDevolucao = None    

    @abstractmethod
    def registrar(self):
        pass

    def __eq__(self, other):
        # Verificação de tipo
        if not isinstance(other, Emprestimo):
            return NotImplemented
        
        email = email.strip().lower()

        return (
                self.titulo.strip().lower() == other.titulo.strip().lower() and 
                self.nome.strip().lower() == other.nome_usuario.strip().lower()
                )
