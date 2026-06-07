---
id: "lista02-q11-confiabilidade-de-itens"
titulo: "Confiabilidade de Itens"
topicos: ["distribuicao-normal"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["tlc", "padronizacao-z"]
---

## Enunciado

A confiabilidade de um item é 0.95. Em 1000 itens, calcule a probabilidade de se obter pelo menos 30 itens defeituosos.

## Solução

Seja $X$ o número de defeituosos. A prob. de defeito é $p = 1 - 0.95 = 0.05$. Logo, $X \sim B(1000, 0.05)$. Queremos $P(X \ge 30)$.

**Aproximação Normal:** $\mu = np = 50$, $\sigma = \sqrt{npq} = \sqrt{47.5} \approx 6.89$.<br>**Correção de Continuidade:** $P(X \ge 30) \approx P(X_{norm} > 29.5)$.<br>$P(Z > \frac{29.5 - 50}{6.89}) = P(Z > -2.97) = 1 - \Phi(-2.97) = \Phi(2.97) \approx 0.9985$.
