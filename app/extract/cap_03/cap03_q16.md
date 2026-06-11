---
id: "dantas-cap03-q16"
titulo: "Variância de soma e generalização para n variáveis"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "Var(sum X_i) = sum Var(X_i) + sum_{i≠j} Cov(X_i, X_j)"
tags: ["variancia", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 16"
---

# Exercício 16

**(a)** Mostre que $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X,Y)$.

**(b)** Generalize para $\text{Var}\!\left(\displaystyle\sum_{i=1}^n X_i\right) = \displaystyle\sum_{i=1}^n \text{Var}(X_i) + \displaystyle\sum_{i \neq j} \text{Cov}(X_i, X_j)$.

---

## Solução

### Parte (a)

Usando bilinearidade (Ex. 15c) e as propriedades do Ex. 14:

$$\text{Var}(X+Y) = \text{Cov}(X+Y, X+Y).$$

Expandindo pela bilinearidade:

$$= \text{Cov}(X,X) + \text{Cov}(X,Y) + \text{Cov}(Y,X) + \text{Cov}(Y,Y)$$

$$= \text{Var}(X) + \text{Cov}(X,Y) + \text{Cov}(X,Y) + \text{Var}(Y)$$

$$= \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X,Y). \quad \square$$

---

### Parte (b)

Seja $S = \sum_{i=1}^n X_i$. Pela bilinearidade da covariância (Ex. 15c com $\alpha_i = \beta_i = 1$):

$$\text{Var}(S) = \text{Cov}(S, S) = \text{Cov}\!\left(\sum_{i=1}^n X_i,\; \sum_{j=1}^n X_j\right) = \sum_{i=1}^n \sum_{j=1}^n \text{Cov}(X_i, X_j).$$

Separando os termos diagonais ($i = j$) dos cruzados ($i \neq j$):

$$= \sum_{i=1}^n \text{Cov}(X_i, X_i) + \sum_{i \neq j} \text{Cov}(X_i, X_j) = \sum_{i=1}^n \text{Var}(X_i) + \sum_{i \neq j} \text{Cov}(X_i, X_j). \quad \square$$

> **Corolário:** Se $X_1, \ldots, X_n$ são dois a dois não-correlacionados (em particular, se são independentes), então $\text{Cov}(X_i, X_j) = 0$ para $i \neq j$, e:
> $$\text{Var}\!\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i).$$
