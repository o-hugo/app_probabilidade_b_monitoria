---
id: "dantas-cap07-q19"
titulo: "Limite em Probabilidade de (X₁²+⋯+Xₙ²)/n — Normal"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "esperanca"]
referencia: "Dantas, Cap. 7, Q. 19"
---

## Enunciado

$X_1,X_2,\ldots$ i.i.d. $N(\mu,\sigma^2)$. Qual o limite em probabilidade de $Y_n=\dfrac{X_1^2+\cdots+X_n^2}{n}$?

## Solução

Pela **Lei Fraca dos Grandes Números**:

$$Y_n=\frac{1}{n}\sum_{i=1}^n X_i^2\xrightarrow{P}E(X_1^2).$$

Para $X\sim N(\mu,\sigma^2)$: $E(X^2)=\text{Var}(X)+[E(X)]^2=\sigma^2+\mu^2$.

$$Y_n\xrightarrow{P}\sigma^2+\mu^2.$$
