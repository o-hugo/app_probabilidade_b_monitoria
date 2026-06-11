---
id: "questoes-q14-slide-questo-14"
titulo: "Questão 14"
topicos: ["funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "slide"
solucao_verificada: false
tags: ["metodo-fda"]
---

## Enunciado

Suponha que $P(X\le0,29)=0,75,$ onde X é uma variável aleatória contínua com alguma distribuição definida sobre (0,1). Se $Y=1-X$, determine k de modo que $P(Y\le k)=0,25$.

## Solução

## Passo 1: Expressar a Probabilidade de Y em Termos de X

Nosso objetivo é encontrar $k$ tal que $P(Y \le k) = 0.25$. Substituímos $Y=1-X$ na inequação:

$$P(1-X \le k)$$

Agora, isolamos X:

$$P(-X \le k-1)$$

Multiplicando a inequação por -1, invertemos o sinal:

$$P(X \ge 1-k)$$

Resumo: Manipulamos a probabilidade desejada para Y em uma probabilidade equivalente para X.



## Passo 2: Usar a Propriedade do Complemento

A probabilidade de $X$ ser maior ou igual a um valor é 1 menos a probabilidade de ser menor que esse valor.

$$P(X \ge 1-k) = 1 - P(X < 1-k)$$

Como X é uma variável contínua, $P(X < a) = P(X \le a)$. Portanto:

$$1 - P(X \le 1-k)$$

Resumo: Convertemos a probabilidade de 'maior ou igual que' para 'menor ou igual que' usando o evento complementar.



## Passo 3: Montar e Resolver a Equação Final

Juntando tudo, temos:

$$P(Y \le k) = 1 - P(X \le 1-k) = 0.25$$

Isolando a probabilidade de X:

$$P(X \le 1-k) = 1 - 0.25 = 0.75$$

O enunciado nos deu a informação de que $P(X \le 0.29) = 0.75$. Comparando as duas equações, os argumentos das probabilidades devem ser iguais:

$$1-k = 0.29$$

$$k = 1 - 0.29 = 0.71$$

Resumo: Igualamos a expressão que encontramos com a informação dada no problema para resolver para k.
