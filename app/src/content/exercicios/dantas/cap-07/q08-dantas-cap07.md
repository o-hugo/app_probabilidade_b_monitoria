---
id: "dantas-cap07-q08"
titulo: "Produção Semanal — Markov e Tchebyschev"
topicos: ["07-desigualdades-concentracao"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 7, Q. 8"
---

## Enunciado

$X$ = itens produzidos por semana, $E(X)=50$, $P(X\ge 0)=1$.

(a) O que se pode afirmar sobre $P(X>100)$?
(b) Se $\text{Var}(X)=50$, o que se pode afirmar sobre $P(X>100)$? Compare.

## Solução

**(a) Desigualdade de Markov:**

$$P(X>100)\le P(X\ge 100)\le\frac{E(X)}{100}=\frac{50}{100}=\frac{1}{2}.$$

A produção excede 100 unidades com probabilidade de no máximo 50%.

**(b) Desigualdade de Tchebyschev** com $\mu=50$, $\sigma^2=50$, $\sigma=\sqrt{50}$:

$$P(X>100)\le P(|X-50|\ge 50)\le\frac{50}{50^2}=\frac{1}{50}.$$

A probabilidade cai para no máximo 2%. **A informação sobre a variância fornece uma limitante muito mais precisa.**
