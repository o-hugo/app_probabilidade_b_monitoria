---
id: "lista02-q30-moda"
titulo: "Moda"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["mediana", "moda"]
---

## Enunciado

Calcule a moda (valor que maximiza a FDP) para: a) U(a, b); b) N($\mu, \sigma^2$); c) Exp($\lambda$).

## Solução

## a) Uniforme(a, b)

A FDP é constante em $(a,b)$. Tecnicamente, todo ponto no intervalo é uma moda. Não há moda única.

## b) Normal($\mu, \sigma^2$)

A FDP $f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ atinge seu valor máximo quando o expoente negativo é minimizado, ou seja, quando $(x-\mu)^2=0$, o que ocorre em $x=\mu$.

## c) Exponencial($\lambda$)

A FDP $f(x) = \lambda e^{-\lambda x}$ é uma função estritamente decrescente para $x > 0$. O valor máximo ocorre no limite quando $x \to 0^+$. A moda é 0.
