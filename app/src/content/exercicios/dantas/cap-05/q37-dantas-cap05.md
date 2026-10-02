---
id: "dantas-cap05-q37"
titulo: "Distribuição Lognormal — Densidade, Média e Variância"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "esperanca", "variancia", "metodo-fda", "fgm"]
referencia: "Dantas, Cap. 5, Q. 37"
---

## Enunciado

$Y = \log X \sim N(\mu, \sigma^2)$, $X > 0$ (lognormal). Determine: (a) $f_X(x)$; (b) $E(X)$ e $\text{Var}(X)$.

## Passo 1: Item (a) — Densidade

$F_X(x) = P(X \le x) = P(Y \le \log x) = \Phi\!\left(\frac{\log x - \mu}{\sigma}\right)$.

Derivando:

$$f_X(x) = \frac{1}{x\sigma\sqrt{2\pi}}\exp\!\left\{-\frac{(\log x - \mu)^2}{2\sigma^2}\right\}, \quad x > 0.$$

**Resumo:** Densidade lognormal via mudança de variável $y = \log x$.

## Passo 2: FGM de $Y \sim N(\mu, \sigma^2)$

$$\phi_Y(t) = E(e^{tY}) = \frac{1}{\sigma\sqrt{2\pi}}\int_{-\infty}^{\infty}\exp\!\left\{ty - \frac{(y-\mu)^2}{2\sigma^2}\right\}dy.$$

Completando o quadrado no expoente:

$$ty - \frac{(y-\mu)^2}{2\sigma^2} = -\frac{1}{2\sigma^2}\left[(y-\mu-\sigma^2 t)^2 - (\mu+\sigma^2 t)^2 + \mu^2\right] = -\frac{(y-\mu-\sigma^2 t)^2}{2\sigma^2} + \mu t + \frac{\sigma^2 t^2}{2}.$$

Logo:

$$\phi_Y(t) = e^{\mu t + \sigma^2 t^2/2}\cdot\underbrace{\frac{1}{\sigma\sqrt{2\pi}}\int_{-\infty}^{\infty}\exp\!\left\{-\frac{(y-\mu-\sigma^2 t)^2}{2\sigma^2}\right\}dy}_{=\,1} = e^{\mu t + \sigma^2 t^2/2},$$

pois, com $z = (y-\mu-\sigma^2 t)/\sigma$, a integral vale $\sigma\int_{-\infty}^{\infty}e^{-z^2/2}\,dz = \sigma\sqrt{2\pi}$.

**Resumo:** $\phi_Y(t) = e^{\mu t + \sigma^2 t^2/2}$, obtida completando o quadrado.

## Passo 3: Item (b) — $E(X)$

$$E(X) = E(e^Y) = \phi_Y(1) = e^{\mu + \sigma^2/2}.$$

**Resumo:** $E(X)$ é a FGM de $Y$ avaliada em $t = 1$.

## Passo 4: $\text{Var}(X)$

$$E(X^2) = E(e^{2Y}) = \phi_Y(2) = e^{2\mu + 2\sigma^2}.$$

$$\text{Var}(X) = e^{2\mu+2\sigma^2} - e^{2\mu+\sigma^2} = e^{2\mu+\sigma^2}(e^{\sigma^2}-1).$$
