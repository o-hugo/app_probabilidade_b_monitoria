---
id: "dantas-cap06-q02"
titulo: "Densidade Conjunta — Verificação e Marginal de X"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "probabilidade"]
referencia: "Dantas, Cap. 6, Q. 2"
---

## Enunciado

A função densidade de probabilidade de $X$ e $Y$ é dada por:
$$f(x,y) = \frac{6}{7}\!\left(x^2 + \frac{xy}{2}\right), \quad 0 < x < 1,\ 0 < y < 2,$$
e zero caso contrário.

(a) Verifique se esta é de fato uma função densidade conjunta.
(b) Calcule a função densidade marginal de $X$.
(c) Determine $P(X > Y)$.

## Solução

**(a) Verificação:**

$$\int_0^1\int_0^2 \frac{6}{7}\!\left(x^2+\frac{xy}{2}\right)dy\,dx = \frac{6}{7}\int_0^1\!\left[2x^2 + x\right]dx = \frac{6}{7}\!\left[\frac{2}{3}+\frac{1}{2}\right] = \frac{6}{7}\cdot\frac{7}{6}=1.\checkmark$$

**(b) Marginal de $X$:**

$$f_X(x)=\int_0^2 \frac{6}{7}\!\left(x^2+\frac{xy}{2}\right)dy = \frac{6}{7}\!\left[2x^2+x\right], \quad 0<x<1.$$

**(c) $P(X>Y)$:** A região $x>y$ com $0<x<1$, $0<y<2$ restringe-se a $y<x\le 1$ (pois $x<1<2$).

$$P(X>Y)=\int_0^1\int_0^x \frac{6}{7}\!\left(x^2+\frac{xy}{2}\right)dy\,dx = \frac{6}{7}\int_0^1\!\left[x^3+\frac{x^3}{4}\right]dx = \frac{6}{7}\cdot\frac{5}{4}\cdot\frac{1}{4}=\frac{30}{112}=\frac{15}{56}.$$
