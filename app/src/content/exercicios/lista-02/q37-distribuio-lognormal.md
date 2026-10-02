---
id: "lista02-q37-distribuio-lognormal"
titulo: "Distribuição Lognormal"
topicos: ["funcao-de-variavel-aleatoria", "modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["metodo-fda", "fgm"]
---

## Enunciado

Se $Y=\ln X \sim N(\mu, \sigma^2)$, determine a) FDP de X, b) E(X) e Var(X).

## Solução

## a) FDP de X

Usamos a transformação $X = e^Y$, então $Y = \ln X$. $\frac{dy}{dx} = 1/x$.<br>$f_X(x) = f_Y(\ln x) |\frac{dy}{dx}| = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(\ln x - \mu)^2}{2\sigma^2}} \cdot \frac{1}{x}$, para $x>0$.

## b) Média e Variância

Usamos a FGM da Normal $Y$. Por definição:

$$M_Y(t) = E[e^{tY}] = \frac{1}{\sigma\sqrt{2\pi}}\int_{-\infty}^{\infty}\exp\left\{ty - \frac{(y-\mu)^2}{2\sigma^2}\right\}dy.$$

Completando o quadrado no expoente:

$$ty - \frac{(y-\mu)^2}{2\sigma^2} = -\frac{(y-\mu-\sigma^2 t)^2}{2\sigma^2} + \mu t + \frac{\sigma^2 t^2}{2}.$$

O fator $e^{\mu t + \sigma^2 t^2/2}$ sai da integral, e o que sobra é a integral da densidade de uma $N(\mu+\sigma^2 t, \sigma^2)$, que vale 1 (com $z = (y-\mu-\sigma^2 t)/\sigma$, a integral vale $\sigma\sqrt{2\pi}$). Logo $M_Y(t) = e^{\mu t + \sigma^2 t^2/2}$.

$E[X] = E[e^Y] = M_Y(1) = e^{\mu + \sigma^2/2}$.<br>$E[X^2] = E[e^{2Y}] = M_Y(2) = e^{2\mu + 2\sigma^2}$.<br>$Var(X) = E[X^2] - (E[X])^2 = e^{2\mu + 2\sigma^2} - (e^{\mu + \sigma^2/2})^2 = (e^{\sigma^2}-1)e^{2\mu+\sigma^2}$.
