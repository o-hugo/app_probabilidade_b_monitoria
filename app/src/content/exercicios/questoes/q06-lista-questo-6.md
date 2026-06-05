---
id: "questoes-q06-lista-questo-6"
titulo: "Questão 6"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

Seja X com densidade $f(x)=\begin{cases}c(1-x^{2}),&-1\le x\le1,\\ 0,&caso~contrario.\end{cases}$ Calcule a média e a variância de X.

## Solução

## Passo 1: Encontrar a Constante de Normalização 'c'

Para que $f(x)$ seja uma fdp válida, a área total sob a curva deve ser igual a 1. Portanto, a integral da função em todo o seu domínio deve ser 1.

$$\int_{-1}^{1} c(1-x^{2}) \,dx = 1 \implies c \int_{-1}^{1} (1-x^{2}) \,dx = 1$$

$$c[x - \frac{x^3}{3}]_{-1}^{1} = c[(1 - \frac{1}{3}) - (-1 - \frac{(-1)^3}{3})] = c[(\frac{2}{3}) - (-1 + \frac{1}{3})] = c[(\frac{2}{3}) - (-\frac{2}{3})] = c(\frac{4}{3}) = 1$$

$$c = \frac{3}{4}$$

Assim, a fdp é $f(x) = \frac{3}{4}(1-x^2)$.

Resumo: Impomos a condição de que a integral total da fdp seja 1 para encontrar o valor da constante c.



## Passo 2: Calcular a Média (Esperança) $E(X)$

$$E(X) = \int_{-1}^{1} x \cdot f(x) \,dx = \int_{-1}^{1} x \cdot \frac{3}{4}(1-x^2) \,dx = \frac{3}{4}\int_{-1}^{1} (x - x^3) \,dx$$

O integrando, $g(x) = x - x^3$, é uma função ímpar, pois $g(-x) = (-x) - (-x)^3 = -x + x^3 = -g(x)$. A integral de uma função ímpar sobre um intervalo simétrico em relação à origem (como [-1, 1]) é sempre zero.

Portanto, $E(X) = 0$.

Resumo: A média é zero, o que é esperado, pois a fdp é uma função par e simétrica em torno de x=0.



## Passo 3: Calcular a Variância $Var(X)$

Usamos a fórmula $Var(X) = E(X^2) - [E(X)]^2$. Como $E(X) = 0$, a variância é simplesmente $Var(X) = E(X^2)$.

$$E(X^2) = \int_{-1}^{1} x^2 \cdot f(x) \,dx = \int_{-1}^{1} x^2 \cdot \frac{3}{4}(1-x^2) \,dx = \frac{3}{4}\int_{-1}^{1} (x^2 - x^4) \,dx$$

O integrando $h(x) = x^2 - x^4$ é uma função par. Podemos simplificar a integral:

$$E(X^2) = \frac{3}{4} \cdot 2 \int_{0}^{1} (x^2 - x^4) \,dx = \frac{3}{2}[\frac{x^3}{3} - \frac{x^5}{5}]_{0}^{1}$$

$$= \frac{3}{2}[(\frac{1}{3} - \frac{1}{5}) - 0] = \frac{3}{2}(\frac{5-3}{15}) = \frac{3}{2}(\frac{2}{15}) = \frac{1}{5} = 0.2$$

Resumo: Calculamos E(X²) e, como a média é zero, este valor é a própria variância.
