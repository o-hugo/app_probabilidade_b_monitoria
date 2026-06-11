---
id: "dantas-cap06-q29"
titulo: "Estatísticas de Ordem — Densidade Conjunta e Amplitude"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "metodo-fda"]
referencia: "Dantas, Cap. 6, Q. 29"
---

## Enunciado

Amostra aleatória $X_1,\ldots,X_n$ de densidade $f$ e FDA $F$. Seja $X_{(1)}\le\cdots\le X_{(n)}$ as estatísticas de ordem.

(a) Determine a densidade conjunta de $X_{(1)}$ e $X_{(n)}$.
(b) Determine a densidade de $A=X_{(n)}-X_{(1)}$ (amplitude).

## Solução

**(a) Densidade conjunta de $X_{(1)}$ e $X_{(n)}$:**

Para $x<y$:

$$f_{X_{(1)},X_{(n)}}(x,y)=n(n-1)[F(y)-F(x)]^{n-2}f(x)f(y).$$

**Derivação:** $P(X_{(1)}>x,X_{(n)}\le y)=[F(y)-F(x)]^n$ (todos os $n$ valores em $(x,y]$). Diferenciando adequadamente (ou usando a fórmula geral das estatísticas de ordem conjuntas):

A probabilidade de ter $X_{(1)}\approx x$ e $X_{(n)}\approx y$ requer: uma observação perto de $x$, uma perto de $y$, e $n-2$ entre eles.

**(b) Densidade da amplitude $A=X_{(n)}-X_{(1)}$:**

Para $a>0$:

$$f_A(a)=\int_{-\infty}^\infty f_{X_{(1)},X_{(n)}}(x,x+a)\,dx=n(n-1)\int_{-\infty}^\infty [F(x+a)-F(x)]^{n-2}f(x)f(x+a)\,dx.$$
