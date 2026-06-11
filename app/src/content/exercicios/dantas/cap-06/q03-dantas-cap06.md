---
id: "dantas-cap06-q03"
titulo: "Densidade Conjunta — Região Triangular e Marginais"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 3"
---

## Enunciado

As variáveis aleatórias $X$ e $Y$ têm distribuição conjunta dada por $f(x,y) = \frac{1}{8}x(x-y)$, $0 < x < 2$, $-x < y < x$, e zero caso contrário.

(a) Esboce o gráfico da região do plano em que $f(x,y) > 0$.
(b) Verifique que $\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x,y)\,dx\,dy = 1$.
(c) Encontre as densidades marginais de $X$ e de $Y$.

## Solução

**(a) Região:** Para cada $x\in(0,2)$, $y\in(-x,x)$ — triângulo com vértices $(0,0)$, $(2,-2)$, $(2,2)$.

**(b) Verificação:**

$$\int_0^2\int_{-x}^{x}\frac{1}{8}x(x-y)\,dy\,dx = \frac{1}{8}\int_0^2 x\!\left[xy-\frac{y^2}{2}\right]_{-x}^{x}dx = \frac{1}{8}\int_0^2 x\cdot x^2\,dx = \frac{1}{8}\cdot\frac{16}{4}=1.\checkmark$$

(O termo $\int_{-x}^x (x-y)\,dy = 2x^2$ pois $\int_{-x}^x x\,dy=2x^2$ e $\int_{-x}^x y\,dy=0$.)

**(c) Densidades marginais:**

$$f_X(x) = \int_{-x}^{x}\frac{1}{8}x(x-y)\,dy = \frac{x}{8}\cdot 2x^2 = \frac{x^3}{4}, \quad 0<x<2.$$

Para $f_Y(y)$, a variável $x$ satisfaz $x>|y|$ e $x<2$, i.e., $x\in(|y|,2)$:

$$f_Y(y) = \int_{|y|}^{2}\frac{1}{8}x(x-y)\,dx = \frac{1}{8}\int_{|y|}^2\!(x^2-xy)\,dx, \quad -2<y<2.$$

$$= \frac{1}{8}\!\left[\frac{x^3}{3}-\frac{x^2 y}{2}\right]_{|y|}^2 = \frac{1}{8}\!\left(\frac{8}{3}-2y - \frac{|y|^3}{3}+\frac{y|y|}{2}\right).$$
