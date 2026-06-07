---
id: "lista02-q14-reparo-de-mquina"
titulo: "Reparo de Máquina"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["falta-de-memoria"]
---

## Enunciado

Tempo de reparo $X \sim Exp(\lambda=1/2)$. Determine: a) P(reparo > 2h); b) P(reparo > 11h | reparo > 9h).

## Solução

**Definição:** A distribuição Exponencial possui a propriedade de **falta de memória**, que diz que $P(X > s+t | X > s) = P(X > t)$.

## a) P(reparo > 2 horas)

Usando a função de sobrevivência $P(X > t) = e^{-\lambda t}$:<br>$ P(X > 2) = e^{-(1/2) \times 2} = e^{-1} \approx 0.3679 $

## b) P(reparo > 11h | reparo > 9h)

Pela propriedade de falta de memória:<br>$ P(X > 9+2 | X > 9) = P(X > 2) = e^{-1} \approx 0.3679 $
