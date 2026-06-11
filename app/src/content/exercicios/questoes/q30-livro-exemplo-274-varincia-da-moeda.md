---
id: "questoes-q30-livro-exemplo-274-varincia-da-moeda"
titulo: "Exemplo 2.7.4 (Variância da Moeda)"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["variancia"]
referencia: "Dantas, Ex. 2.7.4"
---

## Enunciado

Calcular a variância da variável aleatória X do exemplo 2.4.1 (número de caras em 2 lançamentos de moeda).

## Solução

## Passo 1: Relembrar a Distribuição de Probabilidade de X

Do Exemplo 2.4.1, temos:

$P(X=0) = 1/4$

$P(X=1) = 1/2$

$P(X=2) = 1/4$



## Passo 2: Calcular a Esperança de X, $E(X)$

$$E(X) = \sum x_i P(X=x_i) = (0 \cdot \frac{1}{4}) + (1 \cdot \frac{1}{2}) + (2 \cdot \frac{1}{4})$$

$$E(X) = 0 + \frac{1}{2} + \frac{2}{4} = 1$$

Resumo: Calculamos a média da distribuição, que é o primeiro passo para encontrar a variância.



## Passo 3: Calcular a Variância, $Var(X)$

Usamos a definição de variância: $Var(X) = E((X-E(X))^2) = \sum (x_i - E(X))^2 P(X=x_i)$.

$$Var(X) = (0-1)^2 \cdot \frac{1}{4} + (1-1)^2 \cdot \frac{1}{2} + (2-1)^2 \cdot \frac{1}{4}$$

$$Var(X) = (-1)^2 \cdot \frac{1}{4} + (0)^2 \cdot \frac{1}{2} + (1)^2 \cdot \frac{1}{4}$$

$$Var(X) = 1 \cdot \frac{1}{4} + 0 + 1 \cdot \frac{1}{4} = \frac{1}{4} + \frac{1}{4} = \frac{1}{2} = 0.5$$

Resumo: Aplicamos a fórmula da variância, calculando a média ponderada dos desvios quadrados da média.
