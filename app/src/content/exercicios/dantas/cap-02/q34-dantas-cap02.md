---
id: "q34-dantas-cap02"
titulo: "Questão 34"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Suponha que um ponto é escolhido ao acaso em um palito de comprimento unitário e que o palito é quebrado em dois pedaços neste ponto. Determine o valor esperado do comprimento do maior pedaço.

## Solução

O ponto de quebra, denotemos como variável $U$, tem distribuição Uniforme ao longo do palito de tamanho unitário. Logo, $U \sim \text{Uniforme}(0, 1)$, cuja função densidade é $f(u) = 1$.

O palito é dividido em dois pedaços de comprimentos $U$ e $1-U$.
Seja $X$ a variável que representa o comprimento do maior pedaço:
$$ X = \max(U, 1-U) $$
É imediato que o maior pedaço deve sempre ter tamanho superior (ou igual) a $0.5$ para que o menor pedaço fique com o resto do comprimento menor que 1. Logo o intervalo de $X$ é $[0.5, 1]$.

Queremos a Função de Distribuição Acumulada $F_X(x)$ de $X$:
$$ F_X(x) = P(X \le x) = P(\max(U, 1-U) \le x) $$
O máximo de dois valores só é menor do que $x$ se *ambos* forem menores ou iguais a $x$. Então:
$$ P(U \le x \text{ e } 1-U \le x) $$
Isolando $U$ nas desigualdades:
$$ U \le x \quad \text{e} \quad U \ge 1-x $$
Portanto, a variável $U$ tem que cair no intervalo matemático de $1-x$ a $x$. Como $x \in [0.5, 1]$, então o intervalo $[1-x, x]$ é válido e crescente.
$$ P(1-x \le U \le x) = x - (1-x) = 2x - 1 $$
A Função de Distribuição acumulada de $X$ no intervalo de domínio $[0.5, 1]$ é $F_X(x) = 2x - 1$.

A função densidade de probabilidade será a derivada disso:
$$ f_X(x) = \frac{d}{dx} (2x - 1) = 2 $$
Ou seja, $X$ é uniformemente distribuída entre 0.5 e 1.

O valor esperado de $X$ (o comprimento do maior pedaço) é o centro de massa desta distribuição uniforme.
$$ E(X) = \int_{0.5}^{1} x \cdot f_X(x) dx = \int_{0.5}^{1} x \cdot 2 dx $$
$$ E(X) = \left[ x^2 \right]_{0.5}^{1} = 1^2 - (0.5)^2 = 1 - 0.25 = 0.75 $$

O valor esperado do comprimento do maior pedaço é **$3/4$**.
