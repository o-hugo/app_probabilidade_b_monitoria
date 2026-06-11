---
id: "dantas-cap07-q37"
titulo: "Limite Geral de Poisson Parcial com Parâmetro nλ"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["tlc"]
referencia: "Dantas, Cap. 7, Q. 37"
---

## Enunciado

Calcule $\displaystyle\lim_{n\to\infty}e^{-n\lambda}\sum_{k=0}^n\frac{(n\lambda)^k}{k!}$, $0<\lambda\ne 1$.

## Solução

Seja $S_n\sim\text{Poisson}(n\lambda)$.

$$e^{-n\lambda}\sum_{k=0}^n\frac{(n\lambda)^k}{k!}=P(S_n\le n).$$

$E(S_n)=n\lambda$, $\text{Var}(S_n)=n\lambda$, $\sigma_{S_n}=\sqrt{n\lambda}$.

$$P(S_n\le n)=P\!\left(\frac{S_n-n\lambda}{\sqrt{n\lambda}}\le\frac{n-n\lambda}{\sqrt{n\lambda}}\right)=P\!\left(Z_n\le\frac{n(1-\lambda)}{\sqrt{n\lambda}}\right)=P\!\left(Z_n\le(1-\lambda)\sqrt{\frac{n}{\lambda}}\right).$$

- Se $\lambda<1$: $(1-\lambda)\sqrt{n/\lambda}\to+\infty$, portanto o limite é $\Phi(+\infty)=\mathbf{1}$.
- Se $\lambda>1$: $(1-\lambda)\sqrt{n/\lambda}\to-\infty$, portanto o limite é $\Phi(-\infty)=\mathbf{0}$.

$$\lim_{n\to\infty}e^{-n\lambda}\sum_{k=0}^n\frac{(n\lambda)^k}{k!}=\begin{cases}1,&0<\lambda<1,\\0,&\lambda>1.\end{cases}$$
