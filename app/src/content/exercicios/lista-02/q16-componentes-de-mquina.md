---
id: "lista02-q16-componentes-de-mquina"
titulo: "Componentes de Máquina"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["confiabilidade"]
---

## Enunciado

Máquina funciona se ≥3 de 5 componentes funcionam. Vida de cada comp. $X \sim Exp(1/5)$. a) P(máquina funciona > 5h). b) No. médio de comp. funcionando em 10h.

## Solução

**Passo 1:** Probabilidade de um componente individual funcionar.<br>A prob. $p$ de um componente funcionar por mais de $t$ horas é $P(X > t) = e^{-t/5}$.

## a) P(máquina funciona > 5h)

A prob. de um comp. funcionar > 5h é $p_5 = P(X > 5) = e^{-5/5} = e^{-1} \approx 0.3679$.<br>Seja $Y$ o número de componentes funcionando. $Y \sim B(5, p_5)$. A máquina funciona se $Y \ge 3$.<br>$ P(Y \ge 3) = P(Y=3) + P(Y=4) + P(Y=5) $<br>$ = \binom{5}{3}(e^{-1})^3(1-e^{-1})^2 + \binom{5}{4}(e^{-1})^4(1-e^{-1})^1 + \binom{5}{5}(e^{-1})^5 \approx 0.263 $

## b) Número médio de componentes funcionando em 10h

A prob. de um comp. funcionar > 10h é $p_{10} = P(X>10) = e^{-10/5} = e^{-2} \approx 0.1353$.<br>O número médio é a esperança de $Z \sim B(5, p_{10})$: $E[Z] = np_{10} = 5 \times e^{-2} \approx 0.6767$.
