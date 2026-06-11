---
id: "dantas-cap05-q06"
titulo: "Tempo de Espera na Cabine Telefônica — Exponencial"
topicos: ["03-modelos-continuos"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "(a) e^{-1} ≈ 0,368  (b) e^{-1} - e^{-2} ≈ 0,233"
tags: ["probabilidade", "falta-de-memoria"]
referencia: "Dantas, Cap. 5, Q. 6"
---

## Enunciado

A duração de uma ligação telefônica é $X \sim \text{Exp}(\lambda = 1/10)$ (minutos). Uma pessoa está na sua frente. Determine a probabilidade de esperar: (a) mais de 10 minutos; (b) entre 10 e 20 minutos.

## Solução

Para $X \sim \text{Exp}(1/10)$: $P(X > t) = e^{-t/10}$.

**(a)** $P(X > 10) = e^{-10/10} = e^{-1} \approx 0{,}368$.

**(b)** $P(10 < X < 20) = e^{-1} - e^{-2} \approx 0{,}368 - 0{,}135 = 0{,}233$.
