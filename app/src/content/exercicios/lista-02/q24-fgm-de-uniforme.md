---
id: "lista02-q24-fgm-de-uniforme"
titulo: "FGM de Uniforme"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Determine a função geradora de momentos (FGM) de $X \sim U(a, b)$.

## Solução

A FGM é $M_X(t) = E[e^{tX}] = \int_a^b e^{tx} f(x) dx$.

$$ M_X(t) = \int_a^b e^{tx} \frac{1}{b-a} dx = \frac{1}{b-a} \left[ \frac{e^{tx}}{t} \right]_a^b = \frac{1}{t(b-a)} (e^{tb} - e^{ta}) $$
