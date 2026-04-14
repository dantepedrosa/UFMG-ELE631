# Atividade Prática 1 – Parte 1 (APPOO)
**Prof. Luiza Bernardes Real**  
**Período:** 2026/1  

**Alunos:** _____________________________________________  

---

## 1 (Aula 05)

Faça o diagrama UML e implemente em Python.  
Coloque aqui os prints dos seus códigos e dos resultados dos testes.  
Implemente as classes e `main` em arquivos `.py` separados.

- Crie uma classe `Bolo`
- Crie uma instância da classe `Bolo`

Crie dois tipos de bolo com os seguintes atributos:
- Nome  
- Recheio  
- Massa  
- Se tem cobertura (o primeiro tem e o segundo não)

Crie um terceiro bolo, igual ao primeiro, mas sem cobertura:

- Advindo da instância principal (crie a partir da classe com os atributos requeridos)  
  - Printe na tela a cobertura de todos os bolos  

- Advindo do primeiro bolo (um objeto já criado), mas mude a cobertura para: sem cobertura  
  - Printe na tela a cobertura de todos os bolos  

**Explique os resultados.**

---

## 2 (Aula 05)

Faça o diagrama UML e implemente em Python.  
Coloque os prints dos seus códigos e dos resultados.  
Considere cada classe em um arquivo `.py`.  
Faça testes recursivos de possíveis erros de valor inseridos pelo usuário.

- Crie a classe `FazBolo`
- Crie um construtor com:
  - massa  
  - recheio  
  - cobertura  

Crie um método chamado `assar`, com os seguintes parâmetros:
- temperatura (fogo médio, baixo ou alto)
- tempo de preparo

Print esperado:

> "Você está querendo assar o bolo de massa com recheio de recheio e cobertura de cobertura no fogo temperatura por X minutos"

Onde `X` e `temperatura` são inseridos pelo usuário.

Crie mensagens considerando:

- **Fogo alto**:  
  - Assa em 10 minutos  
  - Antes: cru  
  - Depois: queima  

- **Fogo médio**:  
  - Assa em 30 minutos  
  - Antes: cru  
  - Depois: queima  

- **Fogo baixo**:  
  - Assa em 45 minutos  
  - Antes: cru  
  - Depois: queima  

**Observações:**
- Considere restrições para números negativos ou valores absurdos  
- Crie testes e explique os resultados  

---

## 3 (Aula 05)

Faça o diagrama UML e implemente em Python.  
Coloque os prints dos seus códigos e dos resultados dos testes.  
Crie testes e mensagens de erro para solicitações inválidas.  
Considere cada classe em um arquivo `.py`.

### Contexto
Sistema para administração de uma locadora de veículos.

### Classe `CarroAlugado`

**Atributos:**
- modelo  
- quantidade_dias  
- quilometros_rodados  

**Método:**
- `fornecaValorAluguel()`

Regras:
- R$120,00 por dia  
- R$0,80 por km rodado  

---

### Classe `Locadora`

**Atributo:**
- nome_locadora  

**Método:**
- `determineValorAluguel(carro: CarroAlugado)`

---

### Instruções adicionais

Na função `main()`:
- Crie um carro alugado e uma locadora com dados fictícios  
- Solicite à locadora o valor do aluguel  

Print esperado:

> "O carro [modelo], alugado por [dias] dias na locadora [nome], teve o valor total de [valor] reais, considerando [dias] dias e [km] km rodados."

---

### Tratamento de erros

Crie validações para:
- Dias negativos  
- Quilômetros negativos  
- Valores não numéricos  
- Tentativa de cálculo com dados inválidos  

---

## 4 (Aula 05)

Inspirado no exercício anterior:

- Crie suas próprias classes (mínimo 2 classes + 1 `main`)
- Deve haver:
  - Entrada de dados do usuário  
  - Mensagens de saída  
  - Verificação de erros  
  - Propósito real  

**Entrega:**
- Código  
- Diagrama UML  
- Prints dos resultados  