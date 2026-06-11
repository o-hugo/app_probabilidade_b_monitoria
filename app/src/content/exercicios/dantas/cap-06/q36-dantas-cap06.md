---
id: "dantas-cap06-q36"
titulo: "Densidade Marginal via Condicional Uniforme"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 36"
---

## Enunciado

$X\sim U(0,1)$ e dado $X=x$, $Y|X=x\sim U(x,1)$. Determine a densidade marginal de $Y$.

## Solução

$$f_{Y|X}(y|x)=\frac{1}{1-x},\quad x<y<1.$$

A densidade conjunta: $f(x,y)=f_X(x)\cdot f_{Y|X}(y|x)=\frac{1}{1-x}$, para $0<x<y<1$.

Marginal de $Y$: integrar sobre $x\in(0,y)$:

$$f_Y(y)=\int_0^y\frac{1}{1-x}dx=\Big[-\ln(1-x)\Big]_0^y=-\ln(1-y), \quad 0<y<1.$$

**Verificação:** $\int_0^1(-\ln(1-y))dy=[-{(1-y)\ln(1-y)+(1-y)}]_0^1=0-(-1)=1$. $\checkmark$
