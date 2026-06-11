---
id: "dantas-cap07-q11"
titulo: "Limite em Probabilidade de (X₁²+⋯+Xₙ²)/n — Poisson"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 7, Q. 11"
---

## Enunciado

$X_1,X_2,\ldots$ i.i.d. $\text{Poisson}(\lambda)$. Calcule o limite em probabilidade de $Y_n=\dfrac{X_1^2+\cdots+X_n^2}{n}$.

## Solução

Pela **Lei Fraca dos Grandes Números**: se $X_i$ i.i.d. com $E(X_i^2)<\infty$, então

$$\frac{X_1^2+\cdots+X_n^2}{n}\xrightarrow{P}E(X_1^2).$$

Para $X\sim\text{Poisson}(\lambda)$: $E(X^2)=\text{Var}(X)+[E(X)]^2=\lambda+\lambda^2$.

$$Y_n\xrightarrow{P}\lambda+\lambda^2=\lambda(1+\lambda).$$
