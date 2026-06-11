---
id: "dantas-cap05-q27"
titulo: "Transformação Y = -log X com X ~ U(0,1)"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "Y ~ Exp(1)"
tags: ["metodo-fda", "probabilidade"]
referencia: "Dantas, Cap. 5, Q. 27"
---

## Enunciado

Se $X \sim U(0,1)$, qual a distribuição de $Y = -\log X$?

## Solução

$Y = -\log X > 0$ pois $0 < X < 1$. Usando o método da FDA:

$$F_Y(y) = P(Y \le y) = P(-\log X \le y) = P(X \ge e^{-y}) = 1 - e^{-y}, \quad y > 0.$$

Portanto $f_Y(y) = e^{-y}$, $y > 0$, que é a densidade **exponencial** com parâmetro $\lambda = 1$.

$$\boxed{Y \sim \text{Exp}(1).}$$

Este resultado é a base do **método da transformação inversa** para simular variáveis exponenciais a partir de uniformes.
