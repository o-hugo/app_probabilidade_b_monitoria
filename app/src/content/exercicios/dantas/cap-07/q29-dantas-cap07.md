---
id: "dantas-cap07-q29"
titulo: "Limite via TLC — Integral Incompleta da Gama"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["tlc"]
referencia: "Dantas, Cap. 7, Q. 29"
---

## Enunciado

Calcule $\displaystyle\lim_{n\to\infty}\frac{1}{(n-1)!}\int_0^n t^{n-1}e^{-t}\,dt$.

## Solução

Seja $X_1,\ldots,X_n\sim\text{Exp}(1)$ i.i.d. (Poisson com chegada unitária). $S_n=X_1+\cdots+X_n\sim\text{Gama}(n,1)$.

$$P(S_n\le n)=\int_0^n\frac{t^{n-1}e^{-t}}{(n-1)!}dt=\frac{1}{(n-1)!}\int_0^n t^{n-1}e^{-t}\,dt.$$

$E(S_n)=n$, $\text{Var}(S_n)=n$. Pelo TLC:

$$P(S_n\le n)=P\!\left(\frac{S_n-n}{\sqrt{n}}\le 0\right)\to\Phi(0)=\frac{1}{2}.$$

$$\lim_{n\to\infty}\frac{1}{(n-1)!}\int_0^n t^{n-1}e^{-t}\,dt=\boxed{\frac{1}{2}}.$$
