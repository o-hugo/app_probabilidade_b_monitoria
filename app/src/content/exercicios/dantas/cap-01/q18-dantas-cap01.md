---
id: "dantas-cap01-q18"
titulo: "Dado Viciado: Par Duas Vezes Mais Provavel"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 1, Q. 18"
---

## Enunciado
Um dado é viciado de modo que um número par é duas vezes mais provável que um número ímpar. Encontre a probabilidade de que: 
(a) um número par ocorra; 
(b) um número primo ocorra; 
(c) um número primo par ocorra em um lançamento.

## Solução

Seja $p$ a probabilidade de sair uma face ímpar. Então, a probabilidade de sair uma face par é $2p$.
Como o dado possui 6 faces (3 ímpares e 3 pares), a soma das probabilidades de todas as faces deve ser 1.
$$ P(\text{1}) + P(\text{3}) + P(\text{5}) + P(\text{2}) + P(\text{4}) + P(\text{6}) = 1 $$
$$ p + p + p + 2p + 2p + 2p = 1 $$
$$ 9p = 1 \implies p = \frac{1}{9} $$

Logo, qualquer face ímpar tem probabilidade $\frac{1}{9}$ e qualquer face par tem probabilidade $\frac{2}{9}$.

- **(a) Um número par ocorra:**
$$ P(\text{Par}) = P(2) + P(4) + P(6) = \frac{2}{9} + \frac{2}{9} + \frac{2}{9} = \frac{6}{9} = \frac{2}{3} $$

- **(b) Um número primo ocorra:**
Os números primos no dado são $\{2, 3, 5\}$. Notemos que $2$ é par e $3, 5$ são ímpares.
$$ P(\text{Primo}) = P(2) + P(3) + P(5) = \left(\frac{2}{9}\right) + \left(\frac{1}{9}\right) + \left(\frac{1}{9}\right) = \frac{4}{9} $$

- **(c) Um número primo par ocorra em um lançamento:**
O único número par que também é primo é o 2.
$$ P(\text{Primo Par}) = P(2) = \frac{2}{9} $$
