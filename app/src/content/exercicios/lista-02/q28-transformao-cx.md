---
id: "lista02-q28-transformao-cx"
titulo: "Transformação cX"
topicos: ["funcao-de-variavel-aleatoria", "modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Se $X \sim Exp(\lambda)$ e $c > 0$, determine a distribuição de $Y = cX$.

## Solução

$F_Y(y) = P(Y \le y) = P(cX \le y) = P(X \le y/c)$.<br>A FDA de X é $F_X(x) = 1 - e^{-\lambda x}$.<br>$F_Y(y) = F_X(y/c) = 1 - e^{-\lambda(y/c)} = 1 - e^{-(\lambda/c)y}$.<br>Esta é a FDA de uma Exponencial com parâmetro $\lambda' = \lambda/c$. Portanto, $Y \sim Exp(\lambda/c)$.
