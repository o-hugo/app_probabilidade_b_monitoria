---
id: "lista02-q19-taxa-de-falha-gama"
titulo: "Taxa de Falha Gama"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["taxa-de-falha"]
---

## Enunciado

Determine a função taxa de falha de uma variável aleatória Gama com parâmetros $\alpha$ e $\beta$.

## Solução

A taxa de falha é $\lambda(t) = \frac{f(t)}{R(t)}$, onde $R(t) = P(T>t) = \int_t^\infty f(x) dx$.<br>FDP Gama: $f(t) = \frac{\beta^\alpha}{\Gamma(\alpha)} t^{\alpha-1} e^{-\beta t}$.<br>$ R(t) = \int_t^\infty \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x} dx = \frac{\Gamma(\alpha, \beta t)}{\Gamma(\alpha)}$, onde $\Gamma(s,x)$ é a função gama incompleta superior.<br>Portanto, $\lambda(t) = \frac{\beta^\alpha t^{\alpha-1} e^{-\beta t}}{\Gamma(\alpha, \beta t)}$.<br>Não há uma forma fechada mais simples para o caso geral.
