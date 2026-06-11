---
id: "dantas-cap06-q37"
titulo: "Exponencial-Uniforme: Distribuição de Y/X² e Momentos"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca", "variancia"]
referencia: "Dantas, Cap. 6, Q. 37"
---

## Enunciado

$X\sim\text{Exp}(1/2)$ e $Y|X=x\sim U(0,x^2)$.

(a) Qual é a distribuição de $Y/X^2$?
(b) Determine $E(X)$, $E(Y)$ e $\text{Cov}(X,Y)$.

## Passo 1: Item (a) — Distribuição de $Y/X^2$

Dado $X=x$: $Y/x^2|X=x\sim U(0,1)$ (pois $Y\sim U(0,x^2)$).

Como isso vale para todo $x$, $Y/X^2\sim U(0,1)$ (mistura de uniformes unitárias = uniforme unitária).

## Passo 2: Item (b) — Momentos

$X\sim\text{Exp}(1/2)$: $E(X)=2$, $E(X^2)=\text{Var}(X)+[E(X)]^2=4+4=8$, $E(X^3)=3!/(\frac{1}{2})^3\cdot\ldots=48$.

$E(Y|X)=X^2/2$, portanto:
$$E(Y)=E[X^2/2]=\frac{1}{2}E(X^2)=4.$$

$E(XY)=E[X\cdot E(Y|X)]=E[X\cdot X^2/2]=\frac{1}{2}E(X^3)$.

$E(X^3)=\frac{3!}{(1/2)^3}=48$ (para $\text{Exp}(\lambda)$: $E(X^n)=n!/\lambda^n$, com $\lambda=1/2$).

$$E(XY)=\frac{48}{2}=24.$$

$$\text{Cov}(X,Y)=E(XY)-E(X)E(Y)=24-2\cdot 4=16.$$
