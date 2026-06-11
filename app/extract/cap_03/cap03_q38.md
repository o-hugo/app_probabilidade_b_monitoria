---
id: "dantas-cap03-q38"
titulo: "Propriedade Fundamental dos Martingais"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "condicional"]
referencia: "Dantas, Cap. 3, Q. 38"
---

## Enunciado

Considere sequências $\{X_n, n \geq 1\}$ e $\{Y_n, n \geq 1\}$, com $Y_n = f(X_1, \ldots, X_n)$. Dizemos que $\{Y_n\}$ é um **martingal** com respeito a $\{X_n\}$ se:

**(a)** $E(|Y_n|) < \infty$, e

**(b)** $E[Y_{n+1} \mid X_1, X_2, \ldots, X_n] = Y_n$, $\forall n \geq 1$.

Mostre que $E[Y_n] = E[Y_{n-1}] = \cdots = E[Y_1]$, $\forall n \geq 1$.

## Solução

É suficiente mostrar que $E[Y_{n+1}] = E[Y_n]$ para todo $n \geq 1$.

Pela propriedade de martingal, $E[Y_{n+1} \mid X_1, \ldots, X_n] = Y_n$.

Tomando a esperança de ambos os lados e aplicando a lei das esperanças iteradas:

$$E[Y_{n+1}] = E\!\left[E[Y_{n+1} \mid X_1, \ldots, X_n]\right] = E[Y_n].$$

Por indução, $E[Y_n] = E[Y_{n-1}] = \cdots = E[Y_1]$ para todo $n \geq 1$. $\blacksquare$
