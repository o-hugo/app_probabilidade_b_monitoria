---
id: "dantas-cap06-q35"
titulo: "Esperança Condicional e Covariância"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca", "variancia"]
referencia: "Dantas, Cap. 6, Q. 35"
---

## Enunciado

Densidade conjunta: $f(x,y)=\frac{e^{-y}}{y}$, $0<x<y$, $y\ge 0$.

(a) Calcule $E(X|Y=y)$. (b) Determine $\text{Cov}(X,Y)$.

## Passo 1: Marginal de $Y$ e condicional de $X|Y$

$$f_Y(y)=\int_0^y\frac{e^{-y}}{y}dx=e^{-y},\quad Y\sim\text{Exp}(1).$$

$$f_{X|Y}(x|y)=\frac{f(x,y)}{f_Y(y)}=\frac{1}{y},\quad 0<x<y \implies X|Y=y\sim U(0,y).$$

## Passo 2: Item (a)

$$E(X|Y=y)=\frac{y}{2}.$$

## Passo 3: Item (b) — Covariância

$E(X)=E[E(X|Y)]=E[Y/2]=\frac{1}{2}$ (pois $E(Y)=1$).

$E(Y)=1$ (Exp(1)).

$E(XY)=E[Y\cdot E(X|Y)]=E[Y\cdot Y/2]=\frac{1}{2}E(Y^2)=\frac{1}{2}\cdot 2=1$.

$$\text{Cov}(X,Y)=E(XY)-E(X)E(Y)=1-\frac{1}{2}\cdot 1=\frac{1}{2}.$$
