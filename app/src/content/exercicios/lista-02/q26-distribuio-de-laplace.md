---
id: "lista02-q26-distribuio-de-laplace"
titulo: "Distribuição de Laplace"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["fda"]
---

## Enunciado

Para $X$ com FDP $f(x) = \frac{1}{2}\lambda e^{-\lambda|x|}$, determine a função de distribuição $F(x)$.

## Solução

A FDA é $F(x) = \int_{-\infty}^x f(t)dt$.

## Caso 1: $x < 0$

Neste intervalo, $|t| = -t$.<br>$ F(x) = \int_{-\infty}^x \frac{1}{2}\lambda e^{\lambda t} dt = \frac{1}{2}\lambda [\frac{e^{\lambda t}}{\lambda}]_{-\infty}^x = \frac{1}{2}e^{\lambda x} $

## Caso 2: $x \ge 0$

$ F(x) = \int_{-\infty}^0 f(t)dt + \int_0^x f(t)dt = F(0) + \int_0^x \frac{1}{2}\lambda e^{-\lambda t} dt $<br>$ = \frac{1}{2} + \frac{1}{2}\lambda [-\frac{e^{-\lambda t}}{\lambda}]_0^x = \frac{1}{2} - \frac{1}{2}(e^{-\lambda x} - 1) = 1 - \frac{1}{2}e^{-\lambda x} $
