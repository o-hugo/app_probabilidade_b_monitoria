---
id: "dantas-cap03-q36"
titulo: "Lei da Variância Total"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["variancia", "condicional", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 36"
---

## Enunciado

Defina $\text{Var}(X \mid Y) = E[(X - E(X \mid Y))^2 \mid Y]$. Mostre que:

$$\text{Var}(X) = E[\text{Var}(X \mid Y)] + \text{Var}[E(X \mid Y)].$$

## Solução

Denote $m(Y) = E(X \mid Y)$. Expandindo a variância condicional:

$$\text{Var}(X \mid Y) = E(X^2 \mid Y) - [E(X \mid Y)]^2 = E(X^2 \mid Y) - m(Y)^2.$$

Tomando a esperança de ambos os lados:

$$E[\text{Var}(X \mid Y)] = E[E(X^2 \mid Y)] - E[m(Y)^2] = E(X^2) - E[m(Y)^2].$$

Por outro lado, pela lei das esperanças iteradas, $E[m(Y)] = E[E(X \mid Y)] = E(X)$, portanto:

$$\text{Var}[E(X \mid Y)] = \text{Var}[m(Y)] = E[m(Y)^2] - (E[m(Y)])^2 = E[m(Y)^2] - (E(X))^2.$$

Somando os dois resultados:

$$E[\text{Var}(X \mid Y)] + \text{Var}[E(X \mid Y)] = E(X^2) - E[m(Y)^2] + E[m(Y)^2] - (E(X))^2$$

$$= E(X^2) - (E(X))^2 = \text{Var}(X). \qquad \blacksquare$$
