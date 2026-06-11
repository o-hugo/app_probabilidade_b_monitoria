---
id: "dantas-cap07-q16"
titulo: "Lei dos Grandes Números — Exponencial Deslocada"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "esperanca"]
referencia: "Dantas, Cap. 7, Q. 16"
---

## Enunciado

$X_i$ i.i.d. com $f(x)=e^{-(x-\theta)}$, $x\ge\theta$. Mostre que $\bar{X}_n\xrightarrow{P}1+\theta$.

## Solução

$E(X_1)=\int_\theta^\infty x\,e^{-(x-\theta)}dx$. Substituindo $u=x-\theta$:

$$E(X_1)=\int_0^\infty (u+\theta)e^{-u}du=\theta+\int_0^\infty ue^{-u}du=\theta+1=1+\theta.$$

Pela **Lei Fraca dos Grandes Números** (desde que $E(X_1)<\infty$, o que é satisfeito):

$$\bar{X}_n=\frac{X_1+\cdots+X_n}{n}\xrightarrow{P}E(X_1)=1+\theta. \quad\blacksquare$$
