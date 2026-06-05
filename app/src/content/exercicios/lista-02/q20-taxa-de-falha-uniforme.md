---
id: "lista02-q20-taxa-de-falha-uniforme"
titulo: "Taxa de Falha Uniforme"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Calcule a função taxa de falha de X quando X é $U(0, a)$.

## Solução

Para $t \in (0, a)$:<br>FDP: $f(t) = 1/a$.<br>Função de Confiabilidade: $R(t) = P(X>t) = \int_t^a \frac{1}{a} dx = \frac{a-t}{a}$.<br>Taxa de Falha: $\lambda(t) = \frac{f(t)}{R(t)} = \frac{1/a}{(a-t)/a} = \frac{1}{a-t}$.<br>A taxa de falha aumenta com o tempo, tendendo ao infinito quando $t \to a$.
