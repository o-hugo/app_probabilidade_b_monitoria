---
id: "lista02-q13-localizao-de-bombeiros"
titulo: "Localização de Bombeiros"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Incêndios $X \sim U(0, A)$. Onde instalar o corpo de bombeiros (ponto 'a') para minimizar $E[|X-a|]$?

## Solução

Queremos minimizar $g(a) = E[|X-a|] = \int_0^A |x-a| f(x) dx = \frac{1}{A} \int_0^A |x-a| dx$.<br>Separamos a integral no ponto 'a':<br>$g(a) = \frac{1}{A} \left( \int_0^a (a-x) dx + \int_a^A (x-a) dx \right)$<br>$= \frac{1}{A} \left( [ax - \frac{x^2}{2}]_0^a + [\frac{x^2}{2} - ax]_a^A \right) = \frac{1}{A} (\frac{a^2}{2} + (\frac{A^2}{2}-aA) - (\frac{a^2}{2}-a^2)) = \frac{a^2 - aA + A^2/2}{A}$.<br>Para minimizar, derivamos em $a$ e igualamos a zero: $g'(a) = \frac{2a - A}{A} = 0 \implies a = \frac{A}{2}$. O local ótimo é o ponto médio.
