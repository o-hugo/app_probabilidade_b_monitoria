---
id: "dantas-cap06-q23"
titulo: "Verificação de Independência — Três Densidades"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: []
referencia: "Dantas, Cap. 6, Q. 23"
---

## Enunciado

Verifique, em cada caso, se $X$ e $Y$ são independentes:

(a) $f(x,y)=2xe^{-y}$ para $0\le x\le 1$, $y\ge 0$.

(b) $f(x,y)=24xy$ para $x\ge 0$, $y\ge 0$, $x+y\le 1$.

(c) $f(x,y)=\frac{15}{4}x^2$ para $0\le y\le 1-x^2$.

## Solução

**(a)** $f(x,y)=2x\cdot e^{-y}=g(x)h(y)$, suporte retangular $[0,1]\times[0,\infty)$. **Independentes.** $f_X(x)=2x$, $f_Y(y)=e^{-y}$.

**(b)** Suporte $\{x\ge0,y\ge0,x+y\le1\}$ não é retangular — depende de ambas as variáveis. Marginal de $X$: $f_X(x)=\int_0^{1-x}24xy\,dy=12x(1-x)^2$. Marginal de $Y$: $f_Y(y)=12y(1-y)^2$. Produto: $f_X(x)f_Y(y)\ne f(x,y)$ (verificado pelo suporte). **Não independentes.**

**(c)** Suporte $0\le y\le 1-x^2$ depende de $x$. Marginal de $X$: $f_X(x)=\frac{15}{4}x^2(1-x^2)$, $-1\le x\le 1$. O suporte da condicional depende de $x$. **Não independentes.**
