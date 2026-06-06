---
id: "questoes-q29-livro-exemplo-273-dado"
titulo: "Exemplo 2.7.3 (Dado)"
topicos: ["funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Seja X o número observado no lançamento de um dado e seja $Y=(X-E(X))^{2}$. Determine a distribuição de probabilidade e a esperança de Y.

## Solução

## Passo 1: Determinar a Distribuição e a Esperança de X

Para um dado justo, a distribuição de X é $P(X=x) = 1/6$ para $x \in \{1, 2, 3, 4, 5, 6\}$.

A esperança de X é:

$$E(X) = \sum x P(X=x) = (1+2+3+4+5+6) \cdot \frac{1}{6} = \frac{21}{6} = 3.5$$

Resumo: Calculamos a esperança do resultado do dado, que é o ponto de equilíbrio da distribuição.



## Passo 2: Calcular os Valores de Y para cada Valor de X

Agora, calculamos $Y = (X-3.5)^2$ para cada resultado possível de X.

Se $X=1, Y = (1 - 3.5)^2 = (-2.5)^2 = 6.25$

Se $X=2, Y = (2 - 3.5)^2 = (-1.5)^2 = 2.25$

Se $X=3, Y = (3 - 3.5)^2 = (-0.5)^2 = 0.25$

Se $X=4, Y = (4 - 3.5)^2 = (0.5)^2 = 0.25$

Se $X=5, Y = (5 - 3.5)^2 = (1.5)^2 = 2.25$

Se $X=6, Y = (6 - 3.5)^2 = (2.5)^2 = 6.25$

Resumo: Aplicamos a transformação a cada valor de X para encontrar os possíveis valores de Y.



## Passo 3: Determinar a Distribuição de Probabilidade de Y

Agrupamos os valores de Y e somamos suas probabilidades:

$P(Y=0.25) = P(X=3) + P(X=4) = 1/6 + 1/6 = 2/6 = 1/3$

$P(Y=2.25) = P(X=2) + P(X=5) = 1/6 + 1/6 = 2/6 = 1/3$

$P(Y=6.25) = P(X=1) + P(X=6) = 1/6 + 1/6 = 2/6 = 1/3$

Resumo: Construímos a distribuição de Y combinando os resultados de X que levam ao mesmo valor de Y.



## Passo 4: Calcular a Esperança de Y

A esperança de Y é $E(Y) = \sum y P(Y=y)$.

$$E(Y) = (0.25) \cdot (\frac{1}{3}) + (2.25) \cdot (\frac{1}{3}) + (6.25) \cdot (\frac{1}{3})$$

$$E(Y) = \frac{0.25 + 2.25 + 6.25}{3} = \frac{8.75}{3} \approx 2.9167$$

Note que $E(Y) = E((X-E(X))^2)$ é, por definição, a Variância de X, $Var(X)$.

Resumo: Usamos a distribuição de Y para calcular sua esperança, que também é a variância da variável original X.
