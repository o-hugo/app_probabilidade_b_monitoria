---
id: "dantas-cap07-q39"
titulo: "TLC e Aproximação de Stirling"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 39"
---

## Enunciado

$X_i$ i.i.d. $\text{Poisson}(1)$, $S_n=\sum_{i=1}^n X_i$.

(a) Calcule $P(S_n=n)$ exatamente.
(b) Via TLC, mostre que $P(S_n=n)\approx\dfrac{1}{\sqrt{2\pi n}}$.
(c) Conclua a aproximação de Stirling: $n!\approx n^{n+1/2}e^{-n}\sqrt{2\pi}$.

## Passo 1: Item (a)

$S_n\sim\text{Poisson}(n)$:

$$P(S_n=n)=\frac{e^{-n}n^n}{n!}.$$

## Passo 2: Item (b) — Aproximação via TLC

$E(S_n)=n$, $\text{Var}(S_n)=n$. Pelo TLC, para inteiros próximos à média:

$$P(S_n=n)=P\!\left(n\le S_n\le n\right)\approx P\!\left(-\frac{1/2}{\sqrt{n}}\le Z\le\frac{1/2}{\sqrt{n}}\right)\approx\phi(0)\cdot\frac{1}{\sqrt{n}}=\frac{1}{\sqrt{2\pi}}\cdot\frac{1}{\sqrt{n}}=\frac{1}{\sqrt{2\pi n}}.$$

Usando a dica: $\int_{-1/\sqrt{n}}^0 e^{-x^2/2}dx\approx 1/\sqrt{n}$.

## Passo 3: Item (c) — Stirling

Igualando (a) e (b):

$$\frac{e^{-n}n^n}{n!}\approx\frac{1}{\sqrt{2\pi n}} \implies n!\approx n^n e^{-n}\sqrt{2\pi n}=n^{n+1/2}e^{-n}\sqrt{2\pi}. \quad\blacksquare$$
