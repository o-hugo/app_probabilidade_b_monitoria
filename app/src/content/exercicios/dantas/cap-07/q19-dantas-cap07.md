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

Diretamente pela densidade, com $x=\mu+\sigma z$ e $dx=\sigma\,dz$:

$$E(X^2)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}(\mu^2+2\mu\sigma z+\sigma^2z^2)\,e^{-z^2/2}\,dz=\frac{1}{\sqrt{2\pi}}\left[\mu^2\sqrt{2\pi}+2\mu\sigma\cdot 0+\sigma^2\sqrt{2\pi}\right]=\mu^2+\sigma^2,$$

usando $\int_{-\infty}^{\infty}e^{-z^2/2}dz=\sqrt{2\pi}$, $\int_{-\infty}^{\infty}z\,e^{-z^2/2}dz=0$ (integrando ímpar) e $\int_{-\infty}^{\infty}z^2e^{-z^2/2}dz=\sqrt{2\pi}$ (por partes).

$$Y_n\xrightarrow{P}\sigma^2+\mu^2.$$
