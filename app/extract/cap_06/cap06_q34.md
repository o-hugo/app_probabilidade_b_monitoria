---
id: "dantas-cap06-q34"
titulo: "Densidades Condicionais — Exercícios 1 a 6"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca"]
referencia: "Dantas, Cap. 6, Q. 34"
---

## Enunciado

Considere os exercícios 1 a 6. Determine: (a) $f(y|x)$ e $f(x|y)$; (b) $E(X|Y=y)$ e $E(Y|X=x)$.

## Solução

**Q1:** $f(x,y)=\frac{3}{2}y^2$, $f_X(x)=\frac{1}{2}$, $f_Y(y)=3y^2$ (por Q21, independentes).
- $f(y|x)=3y^2$; $f(x|y)=\frac{1}{2}$.
- $E(Y|X=x)=\int_0^1 3y^3dy=3/4$; $E(X|Y=y)=1$.

**Q2:** $f_X(x)=\frac{6}{7}(2x^2+x)$; $f_Y(y)=\frac{6}{7}\int_0^1(x^2+xy/2)dx=\frac{6}{7}(\frac{1}{3}+y/4)$.
- $f(y|x)=\frac{x^2+xy/2}{2x^2+x}$; $f(x|y)=\frac{x^2+xy/2}{1/3+y/4}$.
- $E(Y|X=x)=\int_0^2 y\cdot f(y|x)dy$.

**Q3:** $f_X(x)=x^3/4$; $f(y|x)=\frac{x(x-y)/8}{x^3/4}=\frac{x-y}{2x^2}$ para $y\in(-x,x)$.
- $E(Y|X=x)=\int_{-x}^{x}y\cdot\frac{x-y}{2x^2}dy=\frac{1}{2x^2}\!\left[x\frac{y^2}{2}-\frac{y^3}{3}\right]_{-x}^x=\frac{-x}{3}$.

**Q4–Q6:** Análogo — $f(y|x)=f(x,y)/f_X(x)$ usando as marginais calculadas nos exercícios anteriores.
