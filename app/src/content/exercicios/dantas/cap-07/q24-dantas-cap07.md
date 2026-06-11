---
id: "dantas-cap07-q24"
titulo: "TLC — Poisson com Média 100"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 24"
---

## Enunciado

$X\sim\text{Poisson}(100)$. Determine $P(80\le X\le 120)$.

## Solução

$E(X)=100$, $\text{Var}(X)=100$, $\sigma=10$.

Pelo TLC (aproximação normal para Poisson com $\lambda$ grande):

$$P(80\le X\le 120)=P\!\left(\frac{80-100}{10}\le Z\le\frac{120-100}{10}\right)=P(-2\le Z\le 2).$$

$$P(-2\le Z\le 2)=2\Phi(2)-1\approx 2(0{,}9772)-1=0{,}9544.$$

A probabilidade é aproximadamente **95,44%**.
