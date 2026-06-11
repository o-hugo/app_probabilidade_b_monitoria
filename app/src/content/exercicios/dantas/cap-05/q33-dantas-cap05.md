---
id: "dantas-cap05-q33"
titulo: "Transformação Integral de Probabilidade: Y = F(X) ~ U(0,1)"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["metodo-fda", "fdp-valida"]
referencia: "Dantas, Cap. 5, Q. 33"
---

## Enunciado

$X$ contínua com FDA $F$ qualquer. Defina $Y = F(X)$. Mostre que $Y \sim U(0,1)$.

## Solução

Como $F$ é contínua e estritamente crescente no suporte de $X$, para $0 < y < 1$:

$$F_Y(y) = P(Y \le y) = P(F(X) \le y) = P(X \le F^{-1}(y)) = F(F^{-1}(y)) = y.$$

Logo $F_Y(y) = y$ para $y \in (0,1)$, que é a FDA de $U(0,1)$. $\blacksquare$

**Aplicação:** Para simular $X \sim F$, gere $U \sim U(0,1)$ e retorne $X = F^{-1}(U)$ (método da transformação inversa).
