---
id: "q42-dantas-cap01"
titulo: "Questão 42"
topicos: []
dificuldade: "dificil"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
De uma urna com n bolas numeradas de 1, 2, ..., n, seleciona-se ao acaso e sem reposição todas as bolas, uma de cada vez. Dizemos que ocorre um pareamento na j-ésima seleção (1 ≤ j ≤ n), se nessa seleção for selecionada a bola de número j. Determine a probabilidade de que 
(a) ocorra pelo menos um pareamento; 
(b) não ocorra pareamento algum; 
(c) ocorram exatamente r pareamentos, r = 0, 1, ..., n.

## Solução

Este é o clássico **Problema dos Encontros** (ou Problema dos Chapéus / *Derangements*).
Selecionar $n$ bolas sem reposição gera uma permutação dos números de 1 a $n$. O total de permutações é $n!$.
Um pareamento é um "ponto fixo" na permutação.

- **(b) Não ocorra pareamento algum:**
Permutações sem pontos fixos são chamadas de *Derangements* ($D_n$). A fórmula para $D_n$, obtida pelo Princípio da Inclusão-Exclusão, é:
$$ D_n = n! \sum_{k=0}^{n} \frac{(-1)^k}{k!} $$
A probabilidade de não haver pareamento é $\frac{D_n}{n!}$:
$$ P(\text{nenhum pareamento}) = \sum_{k=0}^{n} \frac{(-1)^k}{k!} $$
*(Para $n$ grande, isso se aproxima de $e^{-1} \approx 0,3678$.)*

- **(a) Ocorra pelo menos um pareamento:**
É o evento complementar de não ocorrer nenhum pareamento.
$$ P(\text{pelo menos um}) = 1 - P(\text{nenhum}) = 1 - \sum_{k=0}^{n} \frac{(-1)^k}{k!} $$

- **(c) Ocorram exatamente $r$ pareamentos:**
Para que haja exatamente $r$ pareamentos, devemos escolher QUAIS $r$ posições terão pareamento (pontos fixos). O número de maneiras de escolhê-las é $\binom{n}{r}$.
As demais $n - r$ posições não podem ter nenhum pareamento entre si, o que corresponde aos derangements de $n-r$ elementos, ou seja, $D_{n-r}$.
O número total de permutações com exatamente $r$ pontos fixos é:
$$ \binom{n}{r} D_{n-r} = \frac{n!}{r!(n-r)!} (n-r)! \sum_{k=0}^{n-r} \frac{(-1)^k}{k!} = \frac{n!}{r!} \sum_{k=0}^{n-r} \frac{(-1)^k}{k!} $$
Dividindo pelo total de permutações $n!$, temos a probabilidade:
$$ P(\text{exatamente } r) = \frac{\frac{n!}{r!} \sum_{k=0}^{n-r} \frac{(-1)^k}{k!}}{n!} = \frac{1}{r!} \sum_{k=0}^{n-r} \frac{(-1)^k}{k!} $$
