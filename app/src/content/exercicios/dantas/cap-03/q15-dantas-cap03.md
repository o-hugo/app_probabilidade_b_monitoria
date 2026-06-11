---
id: "dantas-cap03-q15"
titulo: "Bilinearidade da covariância"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Cov(sum alpha_i X_i, sum beta_j Y_j) = sum_i sum_j alpha_i beta_j Cov(X_i, Y_j)"
tags: ["variancia", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 15"
---

# Exercício 15

Sejam $X_1, \ldots, X_n$ e $Y_1, \ldots, Y_m$ variáveis aleatórias (com variâncias finitas). Mostre:

**(a)** $\text{Cov}\!\left(\displaystyle\sum_{i=1}^n X_i,\; Y_j\right) = \displaystyle\sum_{i=1}^n \text{Cov}(X_i, Y_j)$

**(b)** $\text{Cov}\!\left(X_i,\; \displaystyle\sum_{j=1}^m Y_j\right) = \displaystyle\sum_{j=1}^m \text{Cov}(X_i, Y_j)$

**(c)** $\text{Cov}\!\left(\displaystyle\sum_{i=1}^n \alpha_i X_i,\; \displaystyle\sum_{j=1}^m \beta_j Y_j\right) = \displaystyle\sum_{i=1}^n\sum_{j=1}^m \alpha_i \beta_j\, \text{Cov}(X_i, Y_j)$

---

## Solução

Usa-se a linearidade da esperança: $E\!\left[\sum_i Z_i\right] = \sum_i E[Z_i]$.

### Parte (a)

Seja $S = \sum_{i=1}^n X_i$. Então $E[S] = \sum_{i=1}^n E[X_i]$.

$$\text{Cov}(S, Y_j) = E[S Y_j] - E[S]E[Y_j]$$

$$= E\!\left[\sum_{i=1}^n X_i \cdot Y_j\right] - \left(\sum_{i=1}^n E[X_i]\right) E[Y_j]$$

$$= \sum_{i=1}^n E[X_i Y_j] - \sum_{i=1}^n E[X_i]E[Y_j]$$

$$= \sum_{i=1}^n \left(E[X_i Y_j] - E[X_i]E[Y_j]\right) = \sum_{i=1}^n \text{Cov}(X_i, Y_j). \quad \square$$

---

### Parte (b)

Por simetria da covariância (Ex. 14a) e aplicando (a):

$$\text{Cov}\!\left(X_i, \sum_{j=1}^m Y_j\right) = \text{Cov}\!\left(\sum_{j=1}^m Y_j, X_i\right) = \sum_{j=1}^m \text{Cov}(Y_j, X_i) = \sum_{j=1}^m \text{Cov}(X_i, Y_j). \quad \square$$

---

### Parte (c)

Aplicando homogeneidade (Ex. 14c–d) e as partes (a) e (b):

$$\text{Cov}\!\left(\sum_{i=1}^n \alpha_i X_i,\; \sum_{j=1}^m \beta_j Y_j\right) = \sum_{i=1}^n \alpha_i\, \text{Cov}\!\left(X_i,\; \sum_{j=1}^m \beta_j Y_j\right)$$

$$= \sum_{i=1}^n \alpha_i \sum_{j=1}^m \beta_j\, \text{Cov}(X_i, Y_j) = \sum_{i=1}^n\sum_{j=1}^m \alpha_i \beta_j\, \text{Cov}(X_i, Y_j). \quad \square$$

> **Interpretação matricial:** Se $\boldsymbol{\alpha} = (\alpha_1,\ldots,\alpha_n)^\top$ e $\boldsymbol{\beta} = (\beta_1,\ldots,\beta_m)^\top$, então $\text{Cov}(\boldsymbol{\alpha}^\top \mathbf{X}, \boldsymbol{\beta}^\top \mathbf{Y}) = \boldsymbol{\alpha}^\top \Sigma_{XY} \boldsymbol{\beta}$, onde $\Sigma_{XY}$ é a matriz de covariâncias cruzadas.
