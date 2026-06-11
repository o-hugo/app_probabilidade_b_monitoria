---
id: "dantas-cap06-q06"
titulo: "Densidade Conjunta — Região Parabólica"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "probabilidade"]
referencia: "Dantas, Cap. 6, Q. 6"
---

## Enunciado

A função densidade de probabilidade conjunta de $X$ e $Y$ é: $f(x,y)=cx^2y$ para $x^2\le y\le 1$, e zero caso contrário.

(a) Esboce o gráfico da região $f(x,y)>0$.
(b) Determine o valor da constante $c$.
(c) Determine $P(X\ge Y)$.

## Solução

**(a) Região:** $x^2\le y\le 1$ — entre a parábola $y=x^2$ e a reta $y=1$; $x\in[-1,1]$.

**(b) Constante $c$:**

$$\int_{-1}^{1}\int_{x^2}^{1}cx^2y\,dy\,dx = c\int_{-1}^{1}x^2\cdot\frac{1-x^4}{2}dx = \frac{c}{2}\cdot 2\int_0^1(x^2-x^6)dx = c\!\left(\frac{1}{3}-\frac{1}{7}\right)=\frac{4c}{21}=1.$$

$$c = \frac{21}{4}.$$

**(c) $P(X\ge Y)$:** Na região $x\ge y$ e $x^2\le y\le 1$ com $x\in[-1,1]$: precisamos $y\le x$ e $y\ge x^2$, então $x^2\le y\le x$, válido para $x\in[0,1]$ (onde $x\ge x^2$).

$$P(X\ge Y)=\frac{21}{4}\int_0^1\int_{x^2}^{x}x^2y\,dy\,dx = \frac{21}{4}\int_0^1 x^2\cdot\frac{x^2-x^4}{2}dx = \frac{21}{8}\int_0^1(x^4-x^6)dx=\frac{21}{8}\!\left(\frac{1}{5}-\frac{1}{7}\right)=\frac{21}{8}\cdot\frac{2}{35}=\frac{3}{20}.$$
