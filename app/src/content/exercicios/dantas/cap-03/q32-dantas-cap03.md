---
id: "dantas-cap03-q32"
titulo: "Propriedades da esperança condicional: E(XY|Y), E[g(X,Y)|Y], E(XY)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 32"
---

## Enunciado

Mostre as seguintes propriedades da esperança condicional:

**(a)** $E(XY \mid Y = y) = y \cdot E(X \mid Y = y)$

**(b)** $E[g(X, Y) \mid Y = y] = E[g(X, y) \mid Y = y]$

**(c)** $E(XY) = E\!\left[Y \cdot E(X \mid Y)\right]$

## Passo 1: Prova de (a)

**Resumo:** No cálculo da esperança condicional dado $Y=y$, o fator $y$ é constante e sai da soma.

**Caso discreto:**

$$E(XY \mid Y = y) = \sum_x xy \cdot P(X = x \mid Y = y) = y \sum_x x \cdot P(X = x \mid Y = y) = y \cdot E(X \mid Y = y). \quad \blacksquare$$

**Caso contínuo:** analogamente, $y$ é fixo na integração sobre $x$:

$$E(XY \mid Y = y) = \int_{-\infty}^{+\infty} xy \, f_{X|Y}(x \mid y)\, dx = y \int_{-\infty}^{+\infty} x \, f_{X|Y}(x \mid y)\, dx = y \cdot E(X \mid Y = y). \quad \blacksquare$$

## Passo 2: Prova de (b)

**Resumo:** Dado $Y=y$, o valor de $Y$ é fixado em $y$ na função $g$, tornando $g(X,Y)=g(X,y)$ a.s.

Dado o evento $\{Y = y\}$, a v.a. $Y$ vale $y$ com certeza. Portanto, na esperança condicional:

$$E[g(X, Y) \mid Y = y] = \sum_x g(x, y) \cdot P(X = x \mid Y = y) = E[g(X, y) \mid Y = y]. \quad \blacksquare$$

O item (a) é um caso particular de (b) com $g(x, y) = xy$.

## Passo 3: Prova de (c)

**Resumo:** Aplica a lei da esperança total a $E(XY)$ e usa o item (a).

Pela lei da esperança total:

$$E(XY) = E[E(XY \mid Y)].$$

Pelo item (a), $E(XY \mid Y = y) = y \cdot E(X \mid Y = y)$, ou em notação de v.a.:

$$E(XY \mid Y) = Y \cdot E(X \mid Y).$$

Portanto:

$$E(XY) = E[Y \cdot E(X \mid Y)]. \quad \blacksquare$$
