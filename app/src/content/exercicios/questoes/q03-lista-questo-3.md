---
id: "questoes-q03-lista-questo-3"
titulo: "Questão 3"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista"
solucao_verificada: false
---

## Enunciado

A v.a. contínua X tem f.d.p. $f(x)=\begin{cases}3x^{2},&-1\le x\le0,\\ 0,&caso~contrario\end{cases}$ .

(a) Se b for um número que satisfaz $-1<b<0$, calcule $P(X>b|X<b/2)$.

(b) Calcule $E(X)$ e $Var(X)$.

## Solução

## Parte (a): Probabilidade Condicional


Esta parte é idêntica à Questão 1. A resolução detalhada está na aba da Questão 1.

**Resultado:** $$P(X>b|X<b/2) = \frac{-7b^{3}}{8 + b^{3}}$$


## Parte (b): Média e Variância


## Passo 1: Calcular a Esperança (Média) $E(X)$

A esperança de uma v.a. contínua é calculada por $E(X) = \int_{-\infty}^{\infty} x \cdot f(x) \,dx$.

$$E(X) = \int_{-1}^{0} x \cdot (3x^{2}) \,dx = \int_{-1}^{0} 3x^{3} \,dx$$

$$= [\frac{3x^{4}}{4}]_{-1}^{0} = (\frac{3 \cdot 0^{4}}{4}) - (\frac{3 \cdot (-1)^{4}}{4}) = 0 - \frac{3}{4} = -\frac{3}{4}$$

Resumo: Calculamos a média ponderada de todos os valores de X, onde a ponderação é a própria fdp, resultando em -0.75.



## Passo 2: Calcular $E(X^2)$

Para encontrar a variância, primeiro precisamos de $E(X^2)$, o segundo momento em relação à origem.

$$E(X^2) = \int_{-\infty}^{\infty} x^2 \cdot f(x) \,dx = \int_{-1}^{0} x^2 \cdot (3x^{2}) \,dx = \int_{-1}^{0} 3x^{4} \,dx$$

$$= [\frac{3x^{5}}{5}]_{-1}^{0} = (\frac{3 \cdot 0^{5}}{5}) - (\frac{3 \cdot (-1)^{5}}{5}) = 0 - (-\frac{3}{5}) = \frac{3}{5}$$

Resumo: Calculamos a esperança de $X^2$, um passo intermediário essencial para o cálculo da variância.



## Passo 3: Calcular a Variância $Var(X)$

A variância mede a dispersão dos dados em torno da média. A fórmula é $Var(X) = E(X^2) - [E(X)]^2$.

$$Var(X) = \frac{3}{5} - (-\frac{3}{4})^2 = \frac{3}{5} - \frac{9}{16}$$

Para subtrair as frações, encontramos um denominador comum (80):

$$Var(X) = \frac{3 \cdot 16}{5 \cdot 16} - \frac{9 \cdot 5}{16 \cdot 5} = \frac{48}{80} - \frac{45}{80} = \frac{3}{80}$$

Resumo: Usando os resultados dos passos anteriores, aplicamos a fórmula da variância e obtemos 3/80 ou 0.0375.
