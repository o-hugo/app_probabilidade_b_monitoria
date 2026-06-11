---
id: "dantas-cap03-q14"
titulo: "Propriedades algébricas da covariância"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "Demonstradas as quatro propriedades da covariância"
tags: ["variancia", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 14"
---

# Exercício 14

Verifique as seguintes propriedades da covariância:

**(a)** $\text{Cov}(X, Y) = \text{Cov}(Y, X)$

**(b)** $\text{Cov}(X, X) = \text{Var}(X)$

**(c)** $\text{Cov}(aX, Y) = a\,\text{Cov}(X, Y)$

**(d)** $\text{Cov}(aX, bY) = ab\,\text{Cov}(X, Y)$

---

## Solução

Usa-se a definição: $\text{Cov}(X,Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]$.

### Parte (a): Simetria

$$\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = E[YX] - E[Y]E[X] = \text{Cov}(Y,X). \quad \square$$

A simetria segue da comutatividade do produto de números reais.

---

### Parte (b): Covariância de X consigo mesmo = Variância

$$\text{Cov}(X,X) = E[XX] - E[X]E[X] = E[X^2] - (E[X])^2 = \text{Var}(X). \quad \square$$

---

### Parte (c): Homogeneidade no primeiro argumento

Seja $\mu_X = E[X]$ e $\mu_Y = E[Y]$. Então $E[aX] = a\mu_X$.

$$\text{Cov}(aX, Y) = E[(aX - a\mu_X)(Y - \mu_Y)] = E[a(X - \mu_X)(Y - \mu_Y)]$$

$$= a\,E[(X - \mu_X)(Y - \mu_Y)] = a\,\text{Cov}(X, Y). \quad \square$$

---

### Parte (d): Homogeneidade em ambos os argumentos

Aplicando (c) duas vezes (ou usando simetria):

$$\text{Cov}(aX, bY) = a\,\text{Cov}(X, bY) = a\,\text{Cov}(bY, X) = ab\,\text{Cov}(Y,X) = ab\,\text{Cov}(X,Y). \quad \square$$

Alternativamente, diretamente:

$$\text{Cov}(aX, bY) = E[aX \cdot bY] - E[aX]E[bY] = ab\,E[XY] - ab\,E[X]E[Y] = ab\,\text{Cov}(X,Y). \quad \square$$
