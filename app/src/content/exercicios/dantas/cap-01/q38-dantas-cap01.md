---
id: "dantas-cap01-q38"
titulo: "Distribuicao de Bolas em Urnas Numeradas"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 1, Q. 38"
---

## Enunciado
De quantas maneiras diferentes r bolas distintas podem ser distribuídas, ao acaso, em n urnas numeradas de 1 a n? Qual é a probabilidade de que pelo menos uma urna tenha duas bolas? Qual é a probabilidade de cada urna conter no máximo uma bola?

## Solução

As bolas são **distintas** e as urnas são **numeradas** (também distintas). Cada bola tem exatamente $n$ escolhas de urnas.
Logo, o número total de maneiras de distribuir as $r$ bolas é:
$$ n(\Omega) = n \times n \times \dots \times n \quad (r \text{ vezes}) = n^r $$

- **Probabilidade de cada urna conter no máximo uma bola:**
Para que cada urna tenha no máximo uma bola, nenhuma urna pode receber mais do que uma. Isso significa que as $r$ bolas devem ser colocadas em $r$ urnas *diferentes*. Obviamente, para isso ser possível, é necessário que $r \le n$ (se $r > n$, pelo Princípio da Casa dos Pombos, alguma urna obrigatoriamente terá mais de uma bola, e a probabilidade será 0).
Assumindo $r \le n$:
A primeira bola tem $n$ opções de urna. A segunda bola tem $n-1$ opções (não pode ir na mesma que a primeira). E assim por diante, o que se traduz num arranjo simples de $n$ elementos tomados $r$ a $r$:
$$ A_{n,r} = \frac{n!}{(n-r)!} $$
A probabilidade é a razão entre os arranjos e o total:
$$ P(\text{no máximo 1 bola}) = \frac{n!}{(n-r)! \cdot n^r} $$

- **Probabilidade de que pelo menos uma urna tenha duas bolas (ou mais):**
Este é exatamente o evento complementar de "cada urna conter no máximo uma bola".
Logo:
$$ P(\text{pelo menos 1 urna com 2 ou mais bolas}) = 1 - P(\text{no máximo 1 bola}) $$
$$ P(\text{pelo menos 1 com } \ge 2) = 1 - \frac{n!}{(n-r)! \cdot n^r} $$
