---
id: "dantas-cap07-q36"
titulo: "Limite de Poisson Parcial via TLC"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["tlc"]
referencia: "Dantas, Cap. 7, Q. 36"
---

## Enunciado

Mostre que $\displaystyle\lim_{n\to\infty}e^{-n}\sum_{k=0}^n\frac{n^k}{k!}=\frac{1}{2}$.

## Solução

Seja $X_1,X_2,\ldots$ i.i.d. $\text{Poisson}(1)$ e $S_n=X_1+\cdots+X_n\sim\text{Poisson}(n)$.

$$P(S_n\le n)=\sum_{k=0}^n\frac{e^{-n}n^k}{k!}=e^{-n}\sum_{k=0}^n\frac{n^k}{k!}.$$

$E(S_n)=n$, $\text{Var}(S_n)=n$. Pelo TLC:

$$P(S_n\le n)=P\!\left(\frac{S_n-n}{\sqrt{n}}\le 0\right)\to\Phi(0)=\frac{1}{2}.$$

Portanto $\displaystyle\lim_{n\to\infty}e^{-n}\sum_{k=0}^n\frac{n^k}{k!}=\frac{1}{2}$. $\blacksquare$
