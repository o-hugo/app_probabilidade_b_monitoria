---
id: "02-funcao-geradora-momentos"
titulo: "Função Geradora de Momentos (FGM)"
ordem: 2
ementa_ref: "Função geradora de momentos"
tags: ["fgm", "momentos", "esperança", "unicidade"]
---

# Função Geradora de Momentos (FGM)

## Teoria Aprofundada

A Função Geradora de Momentos (FGM) de uma variável aleatória contínua $X$ é definida como:

$$M_X(t) = E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} f(x) dx$$

Ela é chamada "geradora" porque suas derivadas avaliadas em $t=0$ geram os momentos de $X$. O k-ésimo momento em relação à origem, $E[X^k]$, é dado por:

$$E[X^k] = M_X^{(k)}(0) = \left. \frac{d^k}{dt^k} M_X(t) \right|_{t=0}$$

Por exemplo:
- **Média:** $E[X] = M'_X(0)$
- **Segundo momento:** $E[X^2] = M''_X(0)$
- **Variância:** $Var(X) = M''_X(0) - (M'_X(0))^2$

### Propriedade de Unicidade

> "Let $X$ and $Y$ be random variables. If $M_X(t) = M_Y(t)$ for all $t$ in an open interval around 0, then $X \stackrel{d}{=} Y$."
> -- Wasserman, L. (2004). All of Statistics. p. 57.

Esta **propriedade de unicidade** é crucial: se duas variáveis aleatórias têm a mesma FGM, elas têm a mesma distribuição de probabilidade. Isso é frequentemente usado para identificar a distribuição da soma de variáveis independentes.

### Soma de Variáveis Independentes

Se $X$ e $Y$ são independentes, a FGM da soma $Z = X + Y$ é o produto das FGMs:

$$M_{X+Y}(t) = M_X(t) \cdot M_Y(t)$$

## Usabilidade e Aplicações

A FGM é uma ferramenta teórica poderosa:

- **Prova de Teoremas:** É usada para provar o **Teorema do Limite Central (TLC)**, que é a base de grande parte da inferência estatística.
- **Ciências Atuariais e Finanças:** A FGM da soma de sinistros independentes é o produto de suas FGMs. Isso simplifica o cálculo da distribuição do risco ou sinistro agregado, o que é essencial para calcular prêmios de seguro e reservas.
- **Somas de Variáveis:** Facilita muito encontrar a distribuição da soma de distribuições conhecidas (por exemplo, a soma de normais independentes é normal, a soma de exponenciais independentes é gama).
