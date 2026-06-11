---
id: "dantas-cap05-q28"
titulo: "Transformação Linear Y = cX com X Exponencial"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "Y ~ Exp(λ/c)"
tags: ["metodo-fda"]
referencia: "Dantas, Cap. 5, Q. 28"
---

## Enunciado

$X \sim \text{Exp}(\lambda)$, $c > 0$ constante. Determine a distribuição de $Y = cX$.

## Solução

$$F_Y(y) = P(Y \le y) = P(cX \le y) = P\!\left(X \le \frac{y}{c}\right) = 1 - e^{-\lambda y/c}, \quad y > 0.$$

Portanto $f_Y(y) = \frac{\lambda}{c}e^{-(\lambda/c)y}$, $y > 0$.

$$\boxed{Y \sim \text{Exp}(\lambda/c).}$$

A família exponencial é fechada sob multiplicação por constante positiva (com reparametrização da taxa).
