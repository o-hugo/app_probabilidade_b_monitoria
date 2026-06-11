---
id: "dantas-cap05-q37"
titulo: "Distribuição Lognormal — Densidade, Média e Variância"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "esperanca", "variancia", "metodo-fda"]
referencia: "Dantas, Cap. 5, Q. 37"
---

## Enunciado

$Y = \log X \sim N(\mu, \sigma^2)$, $X > 0$ (lognormal). Determine: (a) $f_X(x)$; (b) $E(X)$ e $\text{Var}(X)$.

## Passo 1: Item (a) — Densidade

$F_X(x) = P(X \le x) = P(Y \le \log x) = \Phi\!\left(\frac{\log x - \mu}{\sigma}\right)$.

Derivando:

$$f_X(x) = \frac{1}{x\sigma\sqrt{2\pi}}\exp\!\left\{-\frac{(\log x - \mu)^2}{2\sigma^2}\right\}, \quad x > 0.$$

**Resumo:** Densidade lognormal via mudança de variável $y = \log x$.

## Passo 2: Item (b) — $E(X)$

$$E(X) = E(e^Y) = \phi_Y(1)$$

onde $\phi_Y(t) = e^{\mu t + \sigma^2 t^2/2}$ é a FGM de $Y \sim N(\mu,\sigma^2)$. Logo:

$$E(X) = e^{\mu + \sigma^2/2}.$$

## Passo 3: $\text{Var}(X)$

$$E(X^2) = E(e^{2Y}) = \phi_Y(2) = e^{2\mu + 2\sigma^2}.$$

$$\text{Var}(X) = e^{2\mu+2\sigma^2} - e^{2\mu+\sigma^2} = e^{2\mu+\sigma^2}(e^{\sigma^2}-1).$$
