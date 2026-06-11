---
id: "dantas-cap06-q01"
titulo: "Densidade Conjunta — Constante e Probabilidades"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "probabilidade"]
referencia: "Dantas, Cap. 6, Q. 1"
---

## Enunciado

Sejam $X$ e $Y$ duas variáveis aleatórias contínuas cuja função densidade de probabilidade conjunta é $f(x,y) = cy^2$ para $0 \le x \le 2$ e $0 \le y \le 1$, e $f(x,y)=0$ caso contrário. Determine:

(a) O valor da constante $c$.
(b) $P(X+Y>2)$.
(c) $P(X \le 1)$.
(d) $P(Y \le 1/2)$.
(e) $P(X = 2Y)$.

## Solução

**(a) Constante $c$:**

$$\int_0^2\int_0^1 cy^2\,dy\,dx = c\cdot 2\cdot\frac{1}{3} = \frac{2c}{3} = 1 \implies c = \frac{3}{2}.$$

**(b) $P(X+Y>2)$:** A região $x+y>2$ com $0\le x\le 2$, $0\le y\le 1$ requer $x>2-y$. Para $y<1$ e $x\le 2$: $x \in (2-y, 2]$.

$$P(X+Y>2) = \int_1^1\ldots + \int_0^1\int_{2-y}^{2}\frac{3}{2}y^2\,dx\,dy = \frac{3}{2}\int_0^1 y^2\cdot y\,dy = \frac{3}{2}\cdot\frac{1}{4} = \frac{3}{8}.$$

**Resumo:** A região $x+y>2$ com $0\le x\le 2$, $0\le y\le 1$ exige $x>2-y$, válido apenas para $y\in(1,1]$; de fato o limite inferior $2-y<0$ quando $y>2$ — revisando: $2-y<2$ sempre, e $2-y\ge 0$ quando $y\le 2$, logo o limite é $x\in(\max(0,2-y),2]$.

Para $y\in[0,1]$: $2-y\in[1,2]$, então $x\in(2-y,2]$, comprimento $y$.

$$P(X+Y>2)=\frac{3}{2}\int_0^1 y^2\cdot y\,dy = \frac{3}{2}\cdot\frac{1}{4}=\frac{3}{8}.$$

**(c) $P(X\le 1)$:**

$$P(X\le 1)=\int_0^1\int_0^1\frac{3}{2}y^2\,dy\,dx = 1\cdot\frac{3}{2}\cdot\frac{1}{3}=\frac{1}{2}.$$

**(d) $P(Y\le 1/2)$:**

$$P(Y\le 1/2)=\int_0^2\int_0^{1/2}\frac{3}{2}y^2\,dy\,dx=2\cdot\frac{3}{2}\cdot\frac{1}{24}=\frac{1}{8}.$$

**(e) $P(X=2Y)=0$** pois é conjunto de medida nula (curva em $\mathbb{R}^2$).
