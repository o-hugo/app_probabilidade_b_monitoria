---
id: "dantas-cap06-q28"
titulo: "Desigualdade de Cauchy-Schwarz e Fréchet"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca"]
referencia: "Dantas, Cap. 6, Q. 28"
---

## Enunciado

(a) Mostre a desigualdade de Cauchy-Schwarz: $(E[XY])^2\le E[X^2]E[Y^2]$.

(b) Se $X$ e $Y$ são variáveis aleatórias quaisquer, mostre: $F_{X,Y}(x,y)\le\sqrt{F_X(x)\cdot F_Y(y)}$.

## Solução

**(a) Cauchy-Schwarz:**

Para qualquer $t\in\mathbb{R}$: $E[(tX+Y)^2]\ge 0$.

$$E[t^2X^2+2tXY+Y^2]=t^2E[X^2]+2tE[XY]+E[Y^2]\ge 0.$$

Este polinômio em $t$ é não-negativo, logo seu discriminante é $\le 0$:

$$4(E[XY])^2-4E[X^2]E[Y^2]\le 0 \implies (E[XY])^2\le E[X^2]E[Y^2]. \quad\blacksquare$$

**(b) Desigualdade de Fréchet:**

Defina $A=\{X\le x\}$ e $B=\{Y\le y\}$. Sejam $I_A$ e $I_B$ as indicadoras.

$$F_{X,Y}(x,y)=P(A\cap B)=E[I_A I_B].$$

Por Cauchy-Schwarz:

$$(E[I_A I_B])^2\le E[I_A^2]E[I_B^2]=E[I_A]E[I_B]=P(A)P(B)=F_X(x)F_Y(y).$$

Portanto $F_{X,Y}(x,y)\le\sqrt{F_X(x)F_Y(y)}$. $\blacksquare$
