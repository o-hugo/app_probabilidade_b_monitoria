---
id: "dantas-cap06-q21"
titulo: "Independência — Exercícios 1 a 6"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: []
referencia: "Dantas, Cap. 6, Q. 21"
---

## Enunciado

Considere novamente os exercícios de 1 a 6. Verifique em quais casos $X$ e $Y$ são independentes.

## Solução

$X$ e $Y$ são independentes sse $f(x,y)=f_X(x)f_Y(y)$ para todo $(x,y)$.

**Q1:** $f(x,y)=\frac{3}{2}y^2$. Marginal de $X$: $f_X(x)=\int_0^1\frac{3}{2}y^2dy=\frac{1}{2}$ para $x\in[0,2]$. Marginal de $Y$: $f_Y(y)=\int_0^2\frac{3}{2}y^2dx=3y^2$. Produto: $f_X(x)f_Y(y)=\frac{3}{2}y^2=f(x,y)$. **Independentes.**

**Q2:** $f(x,y)=\frac{6}{7}(x^2+xy/2)$. Não fatora em $g(x)h(y)$. **Não independentes.**

**Q3:** Suporte de $f$: $|y|<x$, que depende de $x$. Não é produto de suportes marginais. **Não independentes.**

**Q4:** $f(x,y)=\frac{1}{y}e^{-y-x/y}$. Marginal de $Y$: $e^{-y}$; $f(x,y)/f_Y(y)=\frac{1}{y}e^{-x/y}$ que depende de $y$. **Não independentes.**

**Q5:** Suporte $0\le y\le x$ depende de $x$. **Não independentes.**

**Q6:** Suporte $x^2\le y\le 1$ depende de $x$. **Não independentes.**

**Resumo:** Apenas o exercício 1 tem $X$ e $Y$ independentes.
