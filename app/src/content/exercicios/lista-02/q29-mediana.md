---
id: "lista02-q29-mediana"
titulo: "Mediana"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Determine a mediana $m$ (onde $F(m)=1/2$) para: a) U(a, b); b) N($\mu, \sigma^2$); c) Exp($\lambda$).

## Solução

## a) Uniforme(a, b)

$F(m) = \frac{m-a}{b-a} = \frac{1}{2} \implies 2(m-a) = b-a \implies m = \frac{a+b}{2}$.

## b) Normal($\mu, \sigma^2$)

A Normal é simétrica em torno da média. A média, mediana e moda coincidem. $m = \mu$.

## c) Exponencial($\lambda$)

$F(m) = 1 - e^{-\lambda m} = \frac{1}{2} \implies e^{-\lambda m} = \frac{1}{2} \implies -\lambda m = \ln(1/2) = -\ln(2) \implies m = \frac{\ln(2)}{\lambda}$.
