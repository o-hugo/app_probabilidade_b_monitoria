---
id: "dantas-cap06-q42"
titulo: "Mistura com Priori Gama — Posteriori Condicional"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 42"
---

> ⚠️ **Pendente de revisão (OCR):** O enunciado do livro contém a expressão `f(x) = (1/x!)x^n e^{-x}` que parece corrompida pelo OCR. A interpretação mais provável é $f(x)=\frac{1}{\Gamma(n+1)}x^n e^{-x}=\frac{x^n e^{-x}}{n!}$ (Gama ou Poisson), mas requer verificação contra a imagem original. Ver `review/pendentes_cap06.md`.

## Enunciado (reconstruído)

Suponha que a função densidade de probabilidade da variável aleatória $X$ é dada por $f(x)=\dfrac{x^n e^{-x}}{n!}$, $x>0$ (distribuição Gama$(n+1,1)$), e $f(x)=0$ caso contrário. Dado $X=x$ ($x>0$), as $n$ variáveis $Y_1,\ldots,Y_n$ são independentes com densidade condicional:
$$g(y|x)=\frac{1}{x},\quad 0<y<x.$$

Determine:
(a) A função densidade conjunta de $Y_1,\ldots,Y_n$.
(b) A função densidade condicional de $X$ dado $Y_1=y_1,\ldots,Y_n=y_n$.

## Passo 1: Item (a) — Densidade conjunta de $(Y_1,\ldots,Y_n)$

$$f_{Y_1,\ldots,Y_n}(y_1,\ldots,y_n)=\int_0^\infty f_X(x)\prod_{i=1}^n g(y_i|x)\,dx.$$

Com $g(y_i|x)=1/x$ (uniforme em $(0,x)$) e $f_X(x)=x^n e^{-x}/n!$:

$$=\int_{\max y_i}^\infty\frac{x^n e^{-x}}{n!}\cdot\frac{1}{x^n}\,dx=\frac{1}{n!}\int_{y_{(n)}}^\infty e^{-x}\,dx=\frac{e^{-y_{(n)}}}{n!},$$

onde $y_{(n)}=\max(y_1,\ldots,y_n)$.

## Passo 2: Item (b) — Posteriori de $X$

Por Bayes:

$$f_{X|Y_1,\ldots,Y_n}(x|y_1,\ldots,y_n)\propto f_X(x)\prod_{i=1}^n g(y_i|x)=\frac{x^n e^{-x}}{n!}\cdot\frac{1}{x^n}=\frac{e^{-x}}{n!},$$

para $x\ge y_{(n)}$.

Normalizando: $\int_{y_{(n)}}^\infty e^{-x}/n!\,dx=e^{-y_{(n)}}/n!$, portanto:

$$f_{X|\mathbf{Y}}(x|\mathbf{y})=\frac{e^{-x}}{e^{-y_{(n)}}}=e^{-(x-y_{(n)})}, \quad x\ge y_{(n)}.$$

A posteriori é $\text{Exp}(1)$ deslocada por $y_{(n)}$: $X-y_{(n)}|\mathbf{Y}\sim\text{Exp}(1)$.
