---
id: "questoes-q11-lista-questo-11"
titulo: "Questão 11"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

Verifique se as expressões a seguir são funções densidade de probabilidade (assuma que elas se anulam fora dos intervalos especificados).

(a) $f(x)=3x$, $0\le x\le1$.

(b) $f(x)=\frac{x^{2}}{2}$, $x\ge0$.

(c) $f(x)=\frac{(x-3)}{2}$, $3\le x\le5$.

(d) $f(x)=2$, $0\le x\le2$.

(e) $f(x)=\begin{cases}\frac{(2+x)}{4},&se&-2\le x<0;\\ \frac{(2-x)}{4},&se&0\le x<2.\end{cases}$

(f) $f(x)=-\pi,$ se $-\pi<x<0$.

## Solução

## Condições para uma fdp

Para ser uma fdp, uma função $f(x)$ deve satisfazer duas condições:
<ol class="list-decimal list-inside">- **Não-negatividade:** $f(x) \ge 0$ para todo $x$.
- **Normalização:** A área total sob a curva deve ser 1, ou seja, $\int_{-\infty}^{\infty} f(x)dx = 1$.
</ol>



(a) $f(x)=3x$, $0\le x\le1$

1. $f(x) \ge 0$ no intervalo. (OK)

2. $\int_0^1 3x \,dx = [\frac{3x^2}{2}]_0^1 = \frac{3}{2} \ne 1$. <span class="text-red-600 font-semibold">NÃO é uma fdp.</span>



(b) $f(x)=\frac{x^{2}}{2}$, $x\ge0$

1. $f(x) \ge 0$ no intervalo. (OK)

2. $\int_0^\infty \frac{x^2}{2} \,dx = [\frac{x^3}{6}]_0^\infty = \infty$. A integral diverge. <span class="text-red-600 font-semibold">NÃO é uma fdp.</span>



(c) $f(x)=\frac{(x-3)}{2}$, $3\le x\le5$

1. Para $x \in [3,5]$, $x-3 \ge 0$, então $f(x) \ge 0$. (OK)

2. $\int_3^5 \frac{x-3}{2} \,dx = \frac{1}{2}[\frac{x^2}{2} - 3x]_3^5 = \frac{1}{2}[(\frac{25}{2}-15) - (\frac{9}{2}-9)] = \frac{1}{2}[-2.5 - (-4.5)] = 1$. (OK)

<span class="text-green-600 font-semibold">É uma fdp válida.</span>



(d) $f(x)=2$, $0\le x\le2$

1. $f(x) = 2 \ge 0$. (OK)

2. $\int_0^2 2 \,dx = [2x]_0^2 = 4 \ne 1$. <span class="text-red-600 font-semibold">NÃO é uma fdp.</span>



(e) $f(x)=\begin{cases}\frac{(2+x)}{4},&-2\le x<0\\ \frac{(2-x)}{4},&0\le x<2\end{cases}$

1. Para $x \in [-2,0)$, $2+x \ge 0$. Para $x \in [0,2)$, $2-x \ge 0$. (OK)

2. $\int_{-2}^0 \frac{2+x}{4} \,dx + \int_0^2 \frac{2-x}{4} \,dx = \frac{1}{4}[2x+\frac{x^2}{2}]_{-2}^0 + \frac{1}{4}[2x-\frac{x^2}{2}]_0^2$

$= \frac{1}{4}[0 - (-4+2)] + \frac{1}{4}[(4-2) - 0] = \frac{1}{4}[2] + \frac{1}{4}[2] = 1$. (OK)

<span class="text-green-600 font-semibold">É uma fdp válida.</span>



(f) $f(x)=-\pi,$ se $-\pi<x<0$

1. A função é negativa ($f(x) < 0$). A primeira condição falha. <span class="text-red-600 font-semibold">NÃO é uma fdp.</span>
