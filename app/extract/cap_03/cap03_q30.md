---
id: "dantas-cap03-q30"
titulo: "Independência implica E[X|Y]=E[X]; E[X|Y]=E[X] implica não-correlação"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca", "variancia"]
referencia: "Dantas, Cap. 3, Q. 30"
---

## Enunciado

**(a)** Mostre que se $X$ e $Y$ são independentes, então $E[X \mid Y = y] = E[X]$ para todo $y$.

**(b)** Verifique que se $E[X \mid Y = y] = E[X]$ para todo $y$, então $X$ e $Y$ são **não-correlacionadas** (i.e., $\text{Cov}(X,Y) = 0$).

## Passo 1: Prova de (a) — independência implica $E[X|Y=y] = E[X]$

**Resumo:** Pela definição de independência, $f_{X|Y}(x|y) = f_X(x)$, de onde a esperança condicional coincide com a incondicional.

**Caso discreto:** Se $X$ e $Y$ são independentes, então $P(X=x, Y=y) = P(X=x)P(Y=y)$. Logo:

$$P(X = x \mid Y = y) = \frac{P(X=x, Y=y)}{P(Y=y)} = \frac{P(X=x)P(Y=y)}{P(Y=y)} = P(X=x).$$

Portanto:

$$E[X \mid Y = y] = \sum_x x \cdot P(X=x \mid Y=y) = \sum_x x \cdot P(X=x) = E[X]. \quad \blacksquare$$

**Caso contínuo:** Analogamente, $f_{X|Y}(x \mid y) = f_{X,Y}(x,y)/f_Y(y) = f_X(x)f_Y(y)/f_Y(y) = f_X(x)$, e o resultado segue.

## Passo 2: Prova de (b) — $E[X|Y=y]=E[X]$ implica $\text{Cov}(X,Y)=0$

**Resumo:** Calcula-se $E[XY]$ via esperanças iteradas e mostra-se que $E[XY] = E[X]E[Y]$.

Usando a lei da esperança total:

$$E[XY] = E[E(XY \mid Y)].$$

Pela propriedade $E[g(Y) \cdot X \mid Y] = g(Y) \cdot E[X \mid Y]$ (com $g(Y) = Y$):

$$E[XY \mid Y = y] = y \cdot E[X \mid Y = y] = y \cdot E[X].$$

Portanto $E[XY \mid Y] = Y \cdot E[X]$, e:

$$E[XY] = E[Y \cdot E[X]] = E[X] \cdot E[Y].$$

Assim:

$$\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = E[X]E[Y] - E[X]E[Y] = 0. \quad \blacksquare$$

**Observação:** A recíproca não vale: não-correlação não implica independência em geral.
