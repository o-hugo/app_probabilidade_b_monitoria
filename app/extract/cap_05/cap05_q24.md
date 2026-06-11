---
id: "dantas-cap05-q24"
titulo: "Função Geradora de Momentos da Uniforme"
topicos: ["02-funcao-geradora-momentos"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "φ(t) = (e^{tb} - e^{ta}) / (t(b-a))"
tags: ["fgm"]
referencia: "Dantas, Cap. 5, Q. 24"
---

## Enunciado

Determine a função geradora de momentos de $X \sim U(a,b)$.

## Solução

$$\phi(t) = E(e^{tX}) = \int_a^b e^{tx} \frac{1}{b-a}\,dx = \frac{1}{b-a}\cdot\frac{e^{tx}}{t}\Bigg|_a^b = \frac{e^{tb} - e^{ta}}{t(b-a)}, \quad t \neq 0.$$

Para $t = 0$: $\phi(0) = 1$.

Como verificação: $\phi'(0) = E[X] = (a+b)/2$ e $\phi''(0) = E[X^2] = (a^2+ab+b^2)/3$.
