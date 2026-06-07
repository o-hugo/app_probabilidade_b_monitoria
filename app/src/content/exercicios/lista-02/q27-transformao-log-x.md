---
id: "lista02-q27-transformao-log-x"
titulo: "Transformação log X"
topicos: ["funcao-de-variavel-aleatoria", "modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["metodo-fda"]
---

## Enunciado

Se $X \sim U(0, 1)$, qual a distribuição de $Y = -\ln X$?

## Solução

Usamos o método da FDA: $F_Y(y) = P(Y \le y)$. O intervalo de Y é $(0, \infty)$.<br>$P(-\ln X \le y) = P(\ln X \ge -y) = P(X \ge e^{-y})$.<br>Como $X \sim U(0,1)$, $P(X \ge x) = 1-x$ para $x \in (0,1)$.<br>$F_Y(y) = 1 - e^{-y}$. Esta é a FDA de uma Exponencial com $\lambda=1$.<br>A FDP é $f_Y(y) = F_Y'(y) = e^{-y}$. Portanto, $Y \sim Exp(1)$.
