---
id: "lista02-q33-transformada-integral-de-probabilidade"
titulo: "Transformada Integral de Probabilidade"
topicos: ["funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Seja X uma v.a. contínua com FDA F. Mostre que $Y=F(X)$ é $U(0, 1)$.

## Solução

A FDA de Y, $F_Y(y)$, para $y \in (0,1)$ é: $F_Y(y) = P(Y \le y) = P(F(X) \le y)$.<br>Como F é uma função não-decrescente, podemos aplicar sua inversa, $F^{-1}$, em ambos os lados da inequação:<br>$P(F(X) \le y) = P(F^{-1}(F(X)) \le F^{-1}(y)) = P(X \le F^{-1}(y))$.<br>Por definição da FDA de X, $P(X \le x) = F(x)$. Portanto, $P(X \le F^{-1}(y)) = F(F^{-1}(y)) = y$.<br>Assim, $F_Y(y) = y$ para $y \in (0,1)$, que é a FDA de uma $U(0,1)$.
