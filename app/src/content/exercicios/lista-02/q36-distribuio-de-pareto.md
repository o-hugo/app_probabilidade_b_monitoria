---
id: "lista02-q36-distribuio-de-pareto"
titulo: "Distribuição de Pareto"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["esperanca", "variancia"]
---

## Enunciado

Para $X \sim Pareto(\alpha, \beta)$, mostre que $E(X)=\frac{\alpha\beta}{\alpha-1}$ e $Var(X)=\frac{\alpha\beta^2}{(\alpha-1)^2(\alpha-2)}$.

## Solução

FDP: $f(x) = \frac{\alpha \beta^\alpha}{x^{\alpha+1}}$ para $x > \beta$.

## Média (para $\alpha>1$)

$E[X] = \int_\beta^\infty x \frac{\alpha \beta^\alpha}{x^{\alpha+1}} dx = \alpha \beta^\alpha \int_\beta^\infty x^{-\alpha} dx = \alpha \beta^\alpha [\frac{x^{-\alpha+1}}{-\alpha+1}]_\beta^\infty $<br>$= \alpha \beta^\alpha (0 - \frac{\beta^{-\alpha+1}}{-\alpha+1}) = \frac{\alpha\beta}{\alpha-1}$.

## Variância (para $\alpha>2$)

$E[X^2] = \int_\beta^\infty x^2 \frac{\alpha \beta^\alpha}{x^{\alpha+1}} dx = \alpha \beta^\alpha \int_\beta^\infty x^{-\alpha+1} dx = \frac{\alpha\beta^2}{\alpha-2}$.<br>$Var(X) = E[X^2] - (E[X])^2 = \frac{\alpha\beta^2}{\alpha-2} - (\frac{\alpha\beta}{\alpha-1})^2 = \frac{\alpha\beta^2}{(\alpha-1)^2(\alpha-2)}$.
