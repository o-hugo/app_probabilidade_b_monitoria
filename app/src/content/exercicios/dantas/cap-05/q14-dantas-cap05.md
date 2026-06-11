---
id: "dantas-cap05-q14"
titulo: "Tempo de Reparo Exponencial e Falta de Memória"
topicos: ["03-modelos-continuos"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "(a) e^{-1} ≈ 0,368  (b) e^{-1} ≈ 0,368"
tags: ["probabilidade", "falta-de-memoria"]
referencia: "Dantas, Cap. 5, Q. 14"
---

## Enunciado

Tempo de reparo $X \sim \text{Exp}(\lambda = 1/2)$ horas. Determine: (a) $P(\text{reparo} > 2\text{h})$; (b) $P(X > 11 \mid X > 9)$.

## Solução

**(a)**
$$P(X > 2) = e^{-2/2} = e^{-1} \approx 0{,}368.$$

**(b)** Pela propriedade de **falta de memória** da exponencial:
$$P(X > 11 \mid X > 9) = P(X > 2) = e^{-1} \approx 0{,}368.$$

A probabilidade condicional é idêntica à de (a) — o tempo já decorrido não influencia o tempo restante.
