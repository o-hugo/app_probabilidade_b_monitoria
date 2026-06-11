---
id: "dantas-cap01-q40"
titulo: "Distribuicao Multinomial de Bolas em Urnas"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 1, Q. 40"
---

## Enunciado
Distribuindo-se r bolas distintas em n urnas numeradas de 1 a n, qual é a probabilidade de que a urna 1 seja ocupada por $r_1$ bolas, a urna 2 seja ocupada por $r_2$ bolas, ..., a urna n seja ocupada por $r_n$ bolas, de modo que $r_1 + r_2 + \cdots + r_n = r$, $r_j \geq 0, j = 1, 2, \ldots, n$?

## Solução

Como as $r$ bolas são distintas, o número total de modos de distribuí-las nas $n$ urnas é $n^r$ (cada bola tem $n$ opções independentes).

Queremos saber a quantidade de formas de particionar essas $r$ bolas de tal modo que o grupo 1 (para a urna 1) receba exatamente $r_1$ bolas específicas, o grupo 2 receba exatamente $r_2$ bolas específicas, etc.
Esse problema de alocação de objetos distintos em grupos de tamanhos pré-fixados é resolvido pelo coeficiente multinomial:
$$ \text{Total de formas} = \frac{r!}{r_1! r_2! \cdots r_n!} $$

Como todos os resultados ($n^r$) do espaço amostral são equiprováveis, a probabilidade é dada por:
$$ P = \frac{\frac{r!}{r_1! r_2! \cdots r_n!}}{n^r} $$
$$ P = \frac{r!}{r_1! r_2! \cdots r_n! \cdot n^r} $$
