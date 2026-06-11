---
id: "dantas-cap03-q35"
titulo: "Decomposição da Esperança por Partição"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "condicional"]
referencia: "Dantas, Cap. 3, Q. 35"
---

## Enunciado

Mostre que:

$$E(X) = E(X \mid X < a)\,P(X < a) + E(X \mid X \ge a)\,P(X \ge a).$$

## Solução

Pela definição de esperança condicional e a lei da probabilidade total:

$$E(X) = \sum_x x\,P[X = x].$$

Particionando o espaço amostral nos eventos $A = \{X < a\}$ e $A^c = \{X \ge a\}$:

$$E(X) = \sum_{x < a} x\,P[X = x] + \sum_{x \ge a} x\,P[X = x].$$

Multiplicando e dividindo cada soma por $P(A)$ e $P(A^c)$ respectivamente (assumindo $P(A), P(A^c) > 0$):

$$= \left(\sum_{x < a} x\,\frac{P[X=x]}{P(A)}\right) P(A) + \left(\sum_{x \ge a} x\,\frac{P[X=x]}{P(A^c)}\right) P(A^c)$$

$$= E(X \mid X < a)\,P(X < a) + E(X \mid X \ge a)\,P(X \ge a). \qquad \blacksquare$$
