---
id: "q14-dantas-cap01"
titulo: "Questão 14"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Sejam A e B dois eventos de um espaço amostral. Suponha que $P(A) = 0,4$ e $P(A \cup B) = 0,7$ e $P(B) = p$.
(a) Para que valor de $p$ os eventos A e B são mutuamente exclusivos?
(b) Para que valor de $p$ os eventos A e B são independentes?

## Solução

A lei geral da adição de probabilidades afirma que:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
Substituindo os valores dados no problema:
$$0,7 = 0,4 + p - P(A \cap B)$$
$$P(A \cap B) = p - 0,3$$

- **(a) Eventos mutuamente exclusivos**
Se $A$ e $B$ são mutuamente exclusivos, isso significa que não possuem interseção, logo $P(A \cap B) = 0$.
Substituindo na equação acima:
$$0 = p - 0,3 \implies p = 0,3$$

- **(b) Eventos independentes**
Se $A$ e $B$ são independentes, sabemos que a probabilidade da interseção é o produto das probabilidades: $P(A \cap B) = P(A)P(B) = 0,4p$.
Substituindo na equação:
$$0,4p = p - 0,3$$
$$0,3 = p - 0,4p$$
$$0,3 = 0,6p$$
$$p = \frac{0,3}{0,6} = \frac{1}{2} = 0,5$$
