---
id: "dantas-cap06-q04"
titulo: "Esperança e Covariância — Densidade Conjunta com Exponencial"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "variancia"]
referencia: "Dantas, Cap. 6, Q. 4"
---

## Enunciado

A função densidade conjunta de $X$ e $Y$ é dada por:
$$f(x,y) = \frac{1}{y}e^{-(y+x/y)}, \quad x>0,\ y>0.$$
Determine $E(X)$, $E(Y)$ e $\text{Cov}(X,Y)$.

## Passo 1: Marginais

Marginal de $Y$: $f_Y(y)=\int_0^\infty \frac{1}{y}e^{-y-x/y}dx = \frac{1}{y}e^{-y}\cdot y = e^{-y}$, logo $Y\sim\text{Exp}(1)$.

Condicional $X|Y=y$: $f_{X|Y}(x|y)=\frac{1}{y}e^{-x/y}$, ou seja $X|Y=y\sim\text{Exp}(1/y)$.

## Passo 2: Momentos via esperança iterada

$$E(X)=E[E(X|Y)]=E[Y]=1.$$

$$E(X^2)=E[E(X^2|Y)]=E[2Y^2]=2E(Y^2)=2\cdot 2=4.$$

$$E(Y)=1,\quad E(Y^2)=\text{Var}(Y)+[E(Y)]^2=1+1=2.$$

## Passo 3: Covariância

$$E(XY)=E[E(XY|Y)]=E[Y\cdot E(X|Y)]=E[Y\cdot Y]=E(Y^2)=2.$$

$$\text{Cov}(X,Y)=E(XY)-E(X)E(Y)=2-1\cdot 1=1.$$

**Resumo:** $E(X)=1$, $E(Y)=1$, $\text{Cov}(X,Y)=1$.
