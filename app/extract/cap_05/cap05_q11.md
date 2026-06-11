---
id: "dantas-cap05-q11"
titulo: "Confiabilidade — Aproximação Normal para Binomial"
topicos: ["04-distribuicao-normal"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "tlc", "confiabilidade"]
referencia: "Dantas, Cap. 5, Q. 11"
---

## Enunciado

Amostra de 1000 itens com confiabilidade (prob de funcionar) 0,95. Calcule $P(\text{pelo menos 30 defeituosos})$. Enuncie as suposições.

## Passo 1: Modelo

$X$ = número de defeituosos $\sim \text{Bin}(1000, 0{,}05)$. Suposições: itens independentes, mesma prob de defeito.

$\mu = 1000 \times 0{,}05 = 50$, $\sigma = \sqrt{1000 \times 0{,}05 \times 0{,}95} = \sqrt{47{,}5} \approx 6{,}89$.

**Resumo:** $\mu=50$, $\sigma \approx 6{,}89$.

## Passo 2: Aproximação normal

$$P(X \ge 30) \approx P\!\left(Z \ge \frac{29{,}5 - 50}{6{,}89}\right) = P(Z \ge -2{,}97) = \Phi(2{,}97) \approx 0{,}9985.$$

**Resumo:** Há 99,85% de probabilidade de que pelo menos 30 itens sejam defeituosos.
