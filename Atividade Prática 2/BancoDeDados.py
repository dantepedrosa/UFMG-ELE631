from Emprestimo import Emprestimo

class BancoDeDados:
    def __init__(self):
        self.__emprestimos = []

    def existeEmprestimo(self, emprestimo : Emprestimo):
        # Validação de tipo
        if not isinstance(emprestimo, Emprestimo):
            raise TypeError("emprestimo deve ser do tipo Emprestimo.")

        return any(emprestimo == e for e in self.__emprestimos)


    def registrar_Emprestimo(self, emprestimo : Emprestimo):
        # Validação de tipo
        if not isinstance(emprestimo, Emprestimo):
            raise TypeError("emprestimo deve ser do tipo Emprestimo.")

        if self.existeEmprestimo(emprestimo):
            print(f"Empréstimo para {emprestimo.nome_usuario} e {emprestimo.titulo} já existe.")
            return False
        
        self.__emprestimos.append(emprestimo)

        print(f"Empréstimo para {emprestimo.nome_usuario} e {emprestimo.titulo} registrado com sucesso.")
        return True

