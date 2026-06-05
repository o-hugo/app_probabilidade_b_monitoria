---
id: "lista02-q23-tempo-mdio-de-vida-residual"
titulo: "Tempo Médio de Vida Residual"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Se $m(t) = E[T-t|T\ge t]$. a) Mostre $m(t)=\frac{\int_{t}^{\infty}R(x)dx}{R(t)}$. b) Calcule para Exp($\lambda$). c) Calcule para U(0,A).

## Solução

## a) Prova

Usando a fórmula da Q22 para a esperança condicional:<br>$m(t) = E[T-t|T\ge t] = \int_0^\infty P(T-t > y | T \ge t) dy$.<br>$P(T-t > y | T \ge t) = \frac{P(T-t > y \text{ e } T \ge t)}{P(T\ge t)} = \frac{P(T>t+y)}{P(T\ge t)} = \frac{R(t+y)}{R(t)}$.<br>$m(t) = \int_0^\infty \frac{R(t+y)}{R(t)} dy$. Fazendo a substituição $x = t+y$, $dx=dy$.<br>$m(t) = \frac{1}{R(t)} \int_t^\infty R(x) dx$.

## b) Exponencial

$R(t) = e^{-\lambda t}$. $\int_t^\infty e^{-\lambda x}dx = [-\frac{1}{\lambda}e^{-\lambda x}]_t^\infty = \frac{1}{\lambda}e^{-\lambda t}$.<br>$m(t) = \frac{\frac{1}{\lambda}e^{-\lambda t}}{e^{-\lambda t}} = \frac{1}{\lambda}$ (propriedade de falta de memória).

## c) Uniforme

$R(t) = \frac{A-t}{A}$. $\int_t^A \frac{A-x}{A} dx = \frac{1}{A}[Ax - \frac{x^2}{2}]_t^A = \frac{(A-t)^2}{2A}$.<br>$m(t) = \frac{(A-t)^2/2A}{(A-t)/A} = \frac{A-t}{2}$.
