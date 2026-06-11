---
id: "lista02-q06-durao-exponencial-de-ligao"
titulo: "Duração Exponencial de Ligação"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["confiabilidade", "falta-de-memoria"]
---

## Enunciado

Duração da ligação é $X \sim Exp(\lambda=1/10)$. Calcule a probabilidade de esperar: a) > 10 min; b) entre 10 e 20 min.

## Solução

Para $X \sim Exp(\lambda)$, a função de sobrevivência é $P(X > t) = e^{-\lambda t}$.

## a) Mais que 10 minutos

$ P(X > 10) = e^{-(1/10) \times 10} = e^{-1} \approx 0.3679 $

## b) Entre 10 e 20 minutos

$ P(10 < X < 20) = P(X>10) - P(X>20) = e^{-10/10} - e^{-20/10} = e^{-1} - e^{-2} \approx 0.3679 - 0.1353 = 0.2326 $
