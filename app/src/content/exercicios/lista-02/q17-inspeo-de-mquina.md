---
id: "lista02-q17-inspeo-de-mquina"
titulo: "Inspeção de Máquina"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Máquina falha em $X \sim Exp(1/10)$. Se retornar antes da falha (tempo t), custo B. Se depois, custo C por hora parada. Qual o tempo ótimo de retorno 't'?

## Solução

O custo $C(t)$ é uma variável aleatória:<br> $C(t) = B$ se $X > t$ (retorno antes da falha).<br> $C(t) = C(t-X)$ se $X \le t$ (retorno após a falha).<br>O custo esperado $E[C(t)]$ é:<br>$E[C(t)] = B \cdot P(X>t) + \int_0^t C(t-x) f(x) dx$<br>$ = B e^{-t/10} + C \int_0^t (t-x) \frac{1}{10}e^{-x/10} dx$.<br>Integrando por partes: $= B e^{-t/10} + C(t - 10 + 10e^{-t/10})$.<br>Para minimizar, derivamos em $t$ e igualamos a 0:<br>$\frac{dE}{dt} = -\frac{B}{10}e^{-t/10} + C - Ce^{-t/10} = 0 \implies e^{-t/10}(C + B/10) = C \implies t = 10 \ln(\frac{C+B/10}{C})$.
