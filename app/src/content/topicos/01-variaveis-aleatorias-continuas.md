---
id: "variaveis-aleatorias-continuas"
titulo: "Variaveis Aleatorias Continuas"
ordem: 1
ementa_ref: "Variaveis aleatorias continuas"
tags: ["fdp", "fda", "esperanca", "variancia", "mediana"]
---

# Variaveis Aleatorias Continuas

## Definicao

Uma variavel aleatoria (v.a.) e dita **continua** se seus possiveis valores pertencem a um intervalo de numeros reais. Diferente do caso discreto, a probabilidade de uma v.a. continua assumir um valor especifico e zero: $P(X = c) = 0$.

> "A random variable X is continuous if there exists a function $f_X$ such that $f_X(x) \ge 0$ for all x, $\int_{-\infty}^{\infty} f_X(x)dx = 1$ and for every $a \le b$, $P(a < X < b) = \int_a^b f_X(x)dx$."
> -- Wasserman, L. (2004). All of Statistics. p. 23.

## Funcao Densidade de Probabilidade (FDP)

A funcao $f_X(x)$ e a **Funcao Densidade de Probabilidade (FDP)**. Para que uma funcao seja uma FDP valida, ela deve satisfazer duas condicoes:

1. **Nao-negatividade:** $f(x) \ge 0$ para todo $x$
2. **Normalizacao:** $\int_{-\infty}^{\infty} f(x) dx = 1$

A probabilidade e calculada como a **area sob a curva** da FDP:

$$P(a \le X \le b) = \int_a^b f_X(x) dx$$

Note que para variaveis continuas, $P(a \le X \le b) = P(a < X < b)$, pois $P(X = a) = P(X = b) = 0$.

## Funcao de Distribuicao Acumulada (FDA)

A **Funcao de Distribuicao Acumulada (FDA)**, $F_X(x)$, acumula a probabilidade ate o ponto $x$:

$$F_X(x) = P(X \le x) = \int_{-\infty}^{x} f_X(t) \, dt$$

A FDP pode ser recuperada da FDA pela derivacao:

$$f_X(x) = F_X'(x) = \frac{d}{dx} F_X(x)$$

### Propriedades da FDA

- $0 \le F(x) \le 1$ para todo $x$
- $F$ e nao-decrescente
- $\lim_{x \to -\infty} F(x) = 0$ e $\lim_{x \to \infty} F(x) = 1$
- $P(a < X \le b) = F(b) - F(a)$

## Esperanca e Variancia

A **esperanca** (ou media) de uma v.a. continua $X$ e:

$$E[X] = \mu = \int_{-\infty}^{\infty} x \cdot f(x) \, dx$$

O **k-esimo momento** em relacao a origem e:

$$E[X^k] = \int_{-\infty}^{\infty} x^k \cdot f(x) \, dx$$

A **variancia** mede a dispersao dos valores em torno da media:

$$Var(X) = \sigma^2 = E[X^2] - (E[X])^2 = \int_{-\infty}^{\infty} (x - \mu)^2 f(x) \, dx$$

## Mediana e Moda

- A **mediana** $m$ satisfaz $F(m) = 1/2$, ou seja, $P(X \le m) = 0.5$
- A **moda** e o valor de $x$ que maximiza $f(x)$

## Aplicacoes

Variaveis continuas sao fundamentais para modelar fenomenos do mundo real:

- **Engenharia de confiabilidade:** o tempo de vida de um componente eletronico e modelado como uma v.a. continua. A FDP descreve a distribuicao dos tempos de falha, permitindo calcular a probabilidade de o componente sobreviver alem de um tempo especifico.

- **Financas:** os retornos diarios de uma acao sao tratados como continuos para avaliar riscos e construir portfolios. A FDA permite calcular a probabilidade de perdas acima de um limiar (Value at Risk).

- **Fisica:** a posicao de uma particula em um dado instante e uma v.a. continua, conceito fundamental na mecanica quantica. A densidade de probabilidade de encontrar um eletron em uma determinada posicao e dada pelo quadrado da funcao de onda.

- **Controle de qualidade:** o diametro de pecas produzidas por uma maquina varia continuamente. A FDP modela essa variacao e permite estimar a fracao de pecas fora de especificacao.
