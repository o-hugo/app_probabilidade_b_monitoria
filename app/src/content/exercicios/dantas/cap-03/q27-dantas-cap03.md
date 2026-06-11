---
id: "dantas-cap03-q27"
titulo: "X uniforme em {0,...,10}, Y uniforme em {-x,...,x} dado X=x"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 27"
---

## Enunciado

(Baseado no Exemplo 11 do capítulo.) Seja $X$ uniformemente distribuída em $\{0, 1, 2, \ldots, 10\}$. Dado $X = x$, $Y$ é uniformemente distribuída em $\{-x, -x+1, \ldots, x-1, x\}$ (conjunto com $2x+1$ elementos).

Determine:
- A distribuição condicional de $Y$ dado $X = x$.
- A distribuição condicional de $X$ dado $Y = y$.
- $E(Y \mid X)$ e $E(X \mid Y)$.

## Passo 1: Distribuição condicional $Y \mid X = x$

**Resumo:** Por construção, $Y \mid X = x$ é uniforme em $\{-x, \ldots, x\}$, com $2x+1$ pontos.

$$P(Y = y \mid X = x) = \frac{1}{2x+1}, \quad y \in \{-x, -x+1, \ldots, x\}, \quad x \in \{0,1,\ldots,10\}.$$

Para $x = 0$: $Y = 0$ com probabilidade 1.

## Passo 2: Distribuição conjunta de $(X, Y)$

**Resumo:** $P(X=x, Y=y) = P(Y=y|X=x) \cdot P(X=x) = \frac{1}{2x+1} \cdot \frac{1}{11}$.

$$P(X=x, Y=y) = \frac{1}{11(2x+1)}, \quad x \in \{0,\ldots,10\},\; |y| \leq x.$$

## Passo 3: Marginal de $Y$ e distribuição condicional $X \mid Y = y$

**Resumo:** $P(Y=y) = \frac{1}{11}\sum_{x=|y|}^{10} \frac{1}{2x+1}$; a condicional pondera pelo inverso de $2x+1$.

Para um dado $y$ com $|y| \leq 10$, os valores de $x$ compatíveis são $x \in \{|y|, |y|+1, \ldots, 10\}$, pois precisamos $|y| \leq x$.

$$P(Y = y) = \sum_{x=|y|}^{10} \frac{1}{11(2x+1)} = \frac{1}{11} \sum_{x=|y|}^{10} \frac{1}{2x+1}.$$

A distribuição condicional de $X$ dado $Y = y$ é:

$$P(X = x \mid Y = y) = \frac{P(X=x, Y=y)}{P(Y=y)} = \frac{1/(2x+1)}{\displaystyle\sum_{x'=|y|}^{10} \frac{1}{2x'+1}}, \quad x \geq |y|.$$

## Passo 4: Esperanças condicionais

**Resumo:** $E(Y|X=x) = 0$ por simetria; $E(X|Y=y)$ é média ponderada de $x$ por $1/(2x+1)$.

**$E(Y \mid X = x)$:** a distribuição de $Y \mid X=x$ é simétrica em torno de 0, logo:

$$\boxed{E(Y \mid X = x) = 0 \quad \text{para todo } x.}$$

**$E(X \mid Y = y)$:**

$$E(X \mid Y = y) = \sum_{x=|y|}^{10} x \cdot P(X = x \mid Y = y) = \frac{\displaystyle\sum_{x=|y|}^{10} \frac{x}{2x+1}}{\displaystyle\sum_{x=|y|}^{10} \frac{1}{2x+1}}.$$

Esta expressão depende de $|y|$ e deve ser calculada numericamente para cada valor de $y$.
