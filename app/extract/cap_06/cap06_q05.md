---
id: "dantas-cap06-q05"
titulo: "Covariância — Densidade Triangular"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "variancia"]
referencia: "Dantas, Cap. 6, Q. 5"
---

## Enunciado

Calcule a covariância entre $X$ e $Y$ se a função densidade conjunta é dada por:
$$f(x,y) = \frac{2e^{-2x}}{x}, \quad x\ge 0,\ 0\le y\le x.$$

## Passo 1: Marginais

$$f_X(x)=\int_0^x\frac{2e^{-2x}}{x}dy=2e^{-2x}, \quad x>0 \implies X\sim\text{Exp}(2).$$

$$f_Y(y)=\int_y^\infty\frac{2e^{-2x}}{x}dx, \quad y\ge 0.$$

## Passo 2: Momentos

$E(X)=1/2$, $E(X^2)=1/2$, logo $\text{Var}(X)=1/4$.

$E(Y)=E[E(Y|X)]=E[X/2]=1/4$.

$E(XY)=E[X\cdot E(Y|X)]=E[X\cdot X/2]=\frac{1}{2}E(X^2)=\frac{1}{2}\cdot\frac{1}{2}=\frac{1}{4}$.

## Passo 3: Covariância

$$\text{Cov}(X,Y)=E(XY)-E(X)E(Y)=\frac{1}{4}-\frac{1}{2}\cdot\frac{1}{4}=\frac{1}{4}-\frac{1}{8}=\frac{1}{8}.$$

(Dado $X=x$, $Y|X=x\sim U(0,x)$, logo $E(Y|X)=X/2$.)
