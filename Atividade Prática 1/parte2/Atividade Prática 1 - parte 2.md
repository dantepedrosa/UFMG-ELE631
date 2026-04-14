# Atividade Prática 1 – Parte 2 (APPOO)
**Prof. Luiza Bernardes Real**  
**Período:** 2026/1  

**Alunos:** _____________________________________________  

---

## 1

Faça o diagrama UML e implemente em Python.  
Coloque os prints do código e dos resultados dos testes.  
Crie testes e mensagens de erro para solicitações inválidas.

Você está modelando um sistema de cadastro de veículos. Implemente as classes conforme descrito abaixo:

### Superclasse `Veiculo`

**Atributos:**
- marca  
- modelo  
- ano_fabricacao  

**Validações no `__init__`:**
- marca e modelo não podem ser vazios  
- ano_fabricacao deve ser um inteiro entre 1886 e 2025  

**Método:**
- `exibirInfo()` → imprime:
  
  > "Veículo: [marca] [modelo] — Ano: [ano_fabricacao]"

---

### Subclasse `Carro` (herda de `Veiculo`)

**Atributo adicional:**
- numero_portas (deve ser 2 ou 4 — lançar `ValueError` caso contrário)

**Comportamento:**
- Sobrescrever `exibirInfo()`  
- Utilizar `super()` para reaproveitar a implementação da superclasse  

---

### Subclasse `Moto` (herda de `Veiculo`)

**Atributo adicional:**
- cilindradas (deve ser > 0 — lançar `ValueError` caso contrário)

**Comportamento:**
- Sobrescrever `exibirInfo()` usando `super()`  

---

### Subclasse `Caminhao` (herda de `Veiculo`)

**Atributo adicional:**
- capacidade_carga_toneladas (deve ser > 0 — lançar `ValueError` caso contrário)

**Comportamento:**
- Sobrescrever `exibirInfo()` usando `super()`  

---

### Instruções adicionais

- Na função `main()`, crie pelo menos um objeto de cada subclasse com dados fictícios  
- Chame `exibirInfo()` para cada objeto  
- Observe o comportamento polimórfico  

**Crie testes cobrindo:**
- Ano inválido (ex: 1800 ou 3000)  
- Marca vazia  
- Número de portas inválido (ex: 3)  
- Cilindradas negativas  

---

## 2

Explique com suas palavras:

- Qual a diferença entre **herança simples** e **herança múltipla**  
- Dê um exemplo de cada uma  

---

## 3

Faça o diagrama UML e implemente em Python.  
Coloque os prints do código e dos resultados dos testes.  
Crie testes e mensagens de erro para solicitações inválidas.

Você está desenvolvendo um sistema para uma empresa com diferentes tipos de funcionários e um departamento financeiro.

---

### Superclasse `Funcionario`

**Atributos:**
- nome  
- matricula  

**Validações no `__init__`:**
- nome não pode ser vazio  
- matrícula deve ser uma string não vazia  

**Método:**
- `calcularPagamento()`  
  - Implementação genérica (será sobrescrita nas subclasses)

---

### Subclasse `Assalariado` (herda de `Funcionario`)

**Atributo adicional:**
- salario_fixo (deve ser > 0)

**Comportamento:**
- `calcularPagamento()` retorna `salario_fixo`

---

### Subclasse `Horista` (herda de `Funcionario`)

**Atributos adicionais:**
- valor_hora (deve ser > 0)  
- horas_trabalhadas (deve ser >= 0)  

**Comportamento:**
- `calcularPagamento()` retorna: valor_hora × horas_trabalhadas

---

### Subclasse `Comissionado` (herda de `Funcionario`)

**Atributos adicionais:**
- salario_base (deve ser > 0)  
- total_vendas (deve ser >= 0)  
- percentual_comissao (deve ser > 0 e <= 100)  

**Comportamento:**
- `calcularPagamento()` retorna: salario_base + (total_vendas × percentual_comissao / 100)

---

### Classe `Financeiro` (NÃO herda de `Funcionario`)

**Atributo:**
- nome_departamento  

**Método:**
- `processarPagamento(funcionario)`

**Regras:**
- Deve validar se o parâmetro é uma instância de `Funcionario`  
- Deve chamar `calcularPagamento()` do objeto recebido  

**Saída esperada:**

> "Departamento [nome_departamento] processou o pagamento de [nome]"  
> "Matrícula: [matricula] | Valor: R$ [valor]"

---

### Instruções adicionais

- Na `main()`, crie:
- Pelo menos um objeto de cada tipo de funcionário  
- Um objeto `Financeiro`  

- Faça o `Financeiro` processar o pagamento de cada funcionário  
- Isso representa troca de mensagens entre objetos  

---

### Testes obrigatórios

Crie validações para:
- Salário negativo  
- Horas negativas  
- Comissão acima de 100%  
- Parâmetro inválido em `processarPagamento` (ex: string)  