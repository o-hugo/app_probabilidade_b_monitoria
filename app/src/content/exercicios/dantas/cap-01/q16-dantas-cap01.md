---
id: "q16-dantas-cap01"
titulo: "Questão 16"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Mostre que:  $P(E^c \cap F^c) = 1 - P(E) - P(F) + P(E \cap F)$.

## Solução

A expressão pedida pode ser deduzida utilizando as Leis de De Morgan e as propriedades da probabilidade do complementar.

1. Pela Lei de De Morgan, a interseção dos complementares é igual ao complementar da união:
   $$E^c \cap F^c = (E \cup F)^c$$

2. A probabilidade do evento complementar $(E \cup F)^c$ é dada por:
   $$P((E \cup F)^c) = 1 - P(E \cup F)$$

3. Pela regra geral da adição de probabilidades para dois eventos quaisquer, sabemos que:
   $$P(E \cup F) = P(E) + P(F) - P(E \cap F)$$

4. Substituindo a equação 3 na equação 2, temos:
   $$P(E^c \cap F^c) = 1 - [P(E) + P(F) - P(E \cap F)]$$
   $$P(E^c \cap F^c) = 1 - P(E) - P(F) + P(E \cap F)$$

A identidade está provada.
