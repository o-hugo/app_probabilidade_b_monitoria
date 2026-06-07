---
id: "questoes-q26-livro-exemplo-242-fda-em-degraus"
titulo: "Exemplo 2.4.2 (FDA em Degraus)"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Ex. 2.4.2"
---

## Enunciado

A função de distribuição de uma variável aleatória X é dada por: $F(x)=0$ para $x<0$, $F(x)=1/2$ para $0\le x<1$, $F(x)=5/8$ para $1\le x<2$ e $F(x)=1$ para $x\ge2$. Determinar a distribuição de probabilidade de X.

## Solução

## Passo 1: Identificar os Pontos de Descontinuidade (Saltos)

A função de distribuição (FDA) de uma variável discreta é uma função em degraus. Os "saltos" ocorrem nos pontos onde a variável X assume valores com probabilidade positiva. Observando a definição de $F(x)$, vemos que os saltos ocorrem em $x=0$, $x=1$ e $x=2$.

Resumo: Os valores que X pode assumir são os pontos onde a FDA "pula" para um valor maior.



## Passo 2: Calcular a Probabilidade em Cada Ponto de Salto

A probabilidade em um ponto $x_i$ é igual ao tamanho do salto nesse ponto. A fórmula é $P(X=x_i) = F(x_i) - F(x_i^-)$, onde $F(x_i^-)$ é o limite de $F(x)$ quando $x$ se aproxima de $x_i$ pela esquerda.

**Para $x=0$:**

$P(X=0) = F(0) - \lim_{x \to 0^-}F(x) = \frac{1}{2} - 0 = \frac{1}{2}$

**Para $x=1$:**

$P(X=1) = F(1) - \lim_{x \to 1^-}F(x) = \frac{5}{8} - \frac{1}{2} = \frac{5-4}{8} = \frac{1}{8}$

**Para $x=2$:**

$P(X=2) = F(2) - \lim_{x \to 2^-}F(x) = 1 - \frac{5}{8} = \frac{3}{8}$

Resumo: Calculamos o tamanho de cada salto na FDA para encontrar a probabilidade associada a cada valor de X.



## Passo 3: Apresentar a Distribuição de Probabilidade

A distribuição de probabilidade de X é:

$P(X=0) = 1/2$

$P(X=1) = 1/8$

$P(X=2) = 3/8$

A soma das probabilidades é $1/2 + 1/8 + 3/8 = 4/8 + 1/8 + 3/8 = 8/8 = 1$.
