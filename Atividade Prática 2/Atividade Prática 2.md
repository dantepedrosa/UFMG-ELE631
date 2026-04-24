# Atividade Prática 2 – APPOO  
**Prof. Luiza Bernardes Real**  
**2026/1**

**Alunos:** _________________________________________________

---

Uma biblioteca deseja automatizar o controle de empréstimos de materiais para seus usuários. Atualmente, o registro é feito manualmente, o que tem gerado duplicidades, dificuldade de organização e problemas na hora de salvar os dados.

Seu objetivo é projetar e implementar, em Python, um sistema orientado a objetos para cadastro de empréstimos. O sistema deve permitir:

- Registrar diferentes tipos de empréstimo  
- Verificar se um empréstimo já existe antes de cadastrá-lo novamente  
- Extrair o banco de dados e salvá-lo em um arquivo de texto  

---

## Classe Abstrata

Defina uma classe abstrata chamada `Emprestimo`, que represente um empréstimo genérico.

Essa classe deve conter:

- Um método abstrato `registrar()` para registrar o empréstimo no sistema  

---

## Subclasses

### 1. EmprestimoLivro

Representa o empréstimo de um livro.

**Atributos:**

- `nome_usuario`: nome da pessoa que está pegando o livro  
- `titulo`: título do livro  

**Regras ao registrar:**

- O sistema deve definir automaticamente um prazo de devolução de **7 dias**  
- O empréstimo só deve ser adicionado se **não existir outro igual** para o mesmo usuário e o mesmo título  

---

### 2. EmprestimoRevista

Representa o empréstimo de uma revista.  
Deve herdar de `EmprestimoLivro`.

**Atributos adicionais:**

- `edicao`: número ou identificação da edição da revista  

**Regras ao registrar:**

- O prazo de devolução deve ser automaticamente de **2 dias**  
- Deve impedir:
  - duplicidade para o mesmo usuário  
  - mais de um empréstimo da **mesma edição** ao mesmo tempo  

---

## Regras Gerais

O sistema deve verificar se um empréstimo já existe antes de adicioná-lo ao banco de dados.

- Um empréstimo duplicado ocorre quando:
  - o mesmo usuário tenta registrar novamente o mesmo material  

- Caso isso aconteça:
  - exibir uma mensagem informando que o empréstimo já está cadastrado  

---

## Funcionalidades adicionais

Implemente métodos para:

- Listar os empréstimos cadastrados  
- Extrair os dados do banco em formato textual  
- Salvar o banco de dados em um arquivo `.txt`  

---

## Observação

Você pode definir livremente o formato do arquivo, desde que ele seja legível.