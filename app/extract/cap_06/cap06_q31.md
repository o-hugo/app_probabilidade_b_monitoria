---
id: "dantas-cap06-q31"
titulo: "Mínimo de Exponenciais Independentes"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "probabilidade", "falta-de-memoria"]
referencia: "Dantas, Cap. 6, Q. 31"
---

## Enunciado

$X_1,\ldots,X_n$ independentes com $X_i\sim\text{Exp}(\lambda_i)$.

(a) Determine a distribuição de $X_{(1)}=\min_i X_i$.
(b) Mostre que $P(X_k=\min_i X_i)=\dfrac{\lambda_k}{\lambda_1+\cdots+\lambda_n}$.

## Solução

**(a) Distribuição de $X_{(1)}$:**

$$P(X_{(1)}>t)=P(X_1>t,\ldots,X_n>t)=\prod_{i=1}^n e^{-\lambda_i t}=e^{-(\sum\lambda_i)t}.$$

Portanto $X_{(1)}\sim\text{Exp}(\lambda_1+\cdots+\lambda_n)$.

**(b) Probabilidade do argmínimo:**

$X_k$ e $M_k=\min_{i\ne k}X_i$ são independentes (funções de conjuntos disjuntos de variáveis independentes). $M_k\sim\text{Exp}(\sum_{i\ne k}\lambda_i)$.

$$P(X_k\le M_k)=P(X_k\le M_k)=\int_0^\infty\lambda_k e^{-\lambda_k t}\cdot e^{-(\sum_{i\ne k}\lambda_i)t}dt=\lambda_k\int_0^\infty e^{-(\sum_i\lambda_i)t}dt=\frac{\lambda_k}{\sum_i\lambda_i}. \quad\blacksquare$$
