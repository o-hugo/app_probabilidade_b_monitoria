---
id: "dantas-cap07-q05"
titulo: "Markov: P(X ≥ 2μ) ≤ 1/2"
topicos: ["07-desigualdades-concentracao"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "esperanca"]
referencia: "Dantas, Cap. 7, Q. 5"
---

## Enunciado

Seja $X\ge 0$ com $\mu=E(X)$. Mostre que $P(X\ge 2\mu)\le\dfrac{1}{2}$.

## Solução

Pela desigualdade de Markov com $a=2\mu$:

$$P(X\ge 2\mu)\le\frac{E(X)}{2\mu}=\frac{\mu}{2\mu}=\frac{1}{2}. \quad\blacksquare$$

**Interpretação:** Pelo menos metade da massa de probabilidade está abaixo do dobro da média.
