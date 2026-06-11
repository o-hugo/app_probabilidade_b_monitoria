---
id: "dantas-cap06-q32"
titulo: "Mediana de Amostra Uniforme tem Distribuição Beta"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 32"
---

## Enunciado

Mostre que a mediana de uma amostra aleatória de tamanho $2n+1$ de $U(0,1)$ tem distribuição $\text{Beta}(n+1,n+1)$.

## Solução

A mediana é a estatística de ordem $X_{(n+1)}$ de uma amostra de tamanho $2n+1$.

A densidade da $k$-ésima estatística de ordem de $U(0,1)$ (tamanho $m$) é:

$$f_{(k)}(x)=\frac{m!}{(k-1)!(m-k)!}x^{k-1}(1-x)^{m-k}, \quad 0<x<1.$$

Para $k=n+1$ e $m=2n+1$:

$$f_{(n+1)}(x)=\frac{(2n+1)!}{n!\,n!}x^n(1-x)^n=\frac{1}{B(n+1,n+1)}x^n(1-x)^n, \quad 0<x<1.$$

pois $B(n+1,n+1)=\frac{(n!)^2}{(2n+1)!}$.

Reconhecemos a densidade $\text{Beta}(n+1,n+1)$. $\blacksquare$
