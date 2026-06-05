---
id: "lista02-q37-distribuio-lognormal"
titulo: "Distribuição Lognormal"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Se $Y=\ln X \sim N(\mu, \sigma^2)$, determine a) FDP de X, b) E(X) e Var(X).

## Solução

## a) FDP de X

Usamos a transformação $X = e^Y$, então $Y = \ln X$. $\frac{dy}{dx} = 1/x$.<br>$f_X(x) = f_Y(\ln x) |\frac{dy}{dx}| = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}} \cdot \frac{1}{x}$, para $x>0$.

## b) Média e Variância

Usamos a FGM da Normal $Y$: $M_Y(t) = E[e^{tY}] = e^{\mu t + \sigma^2 t^2/2}$.<br>$E[X] = E[e^Y] = M_Y(1) = e^{\mu + \sigma^2/2}$.<br>$E[X^2] = E[e^{2Y}] = M_Y(2) = e^{2\mu + 2\sigma^2}$.<br>$Var(X) = E[X^2] - (E[X])^2 = e^{2\mu + 2\sigma^2} - (e^{\mu + \sigma^2/2})^2 = (e^{\sigma^2}-1)e^{2\mu+\sigma^2}$.
