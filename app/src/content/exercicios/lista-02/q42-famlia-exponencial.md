---
id: "lista02-q42-famlia-exponencial"
titulo: "Família Exponencial"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["fdp-valida"]
---

## Enunciado

Verifique quais distribuições pertencem à família exponencial: $f(x, \theta) = S(x)t(\theta)e^{a(x)b(\theta)}$.

## Solução

**Definição:** Uma FDP pertence à família exponencial se $f(x, \theta) = S(x)t(\theta)e^{a(x)b(\theta)}$ e o suporte não depende de $\theta$.

## a) Uniforme(0, A), $\theta=A$

O suporte $(0,A)$ depende de A. **Não pertence.**

## b) Normal($\mu, 4$), $\theta=\mu$

$f(x,\mu) = \frac{1}{\sqrt{8\pi}}e^{-\frac{(x-\mu)^2}{8}} = (\frac{e^{-x^2/8}}{\sqrt{8\pi}})(e^{-\mu^2/8})e^{x(\mu/4)}$. **Pertence.**

## c) Exponencial($\lambda$), $\theta=\lambda$

$f(x,\lambda) = \lambda e^{-\lambda x} = (1)(\lambda)e^{x(-\lambda)}$. **Pertence.**

## d) Beta($\alpha, \beta$), $\alpha$ conhecido, $\theta=\beta$

$f(x,\beta) = C x^{\alpha-1}(1-x)^{\beta-1} = C x^{\alpha-1}e^{(\beta-1)\ln(1-x)}$. **Pertence.**
