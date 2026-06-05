---
id: "questoes-q31-livro-exemplo-282-esperana-infinita"
titulo: "Exemplo 2.8.2 (Esperança Infinita)"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Seja X uma variável aleatória discreta que assume os valores $1, 2, ..., 2^n, ...$ com probabilidades: $P[X=2^{n}] = 1/2^{n}$ para $n=1, 2, ...$. Mostre que sua esperança é infinita.

## Solução

## Passo 1: Montar a Soma para a Esperança

A esperança de uma variável discreta é dada por $E(X) = \sum_{i} x_i P(X=x_i)$.

Neste caso, os valores $x_i$ são as potências de 2, $2^n$, e as probabilidades são $1/2^n$.

$$E(X) = \sum_{n=1}^{\infty} (2^n) \cdot P(X=2^n) = \sum_{n=1}^{\infty} 2^n \cdot \frac{1}{2^n}$$

Resumo: Substituímos os valores e as probabilidades na fórmula da esperança para obter a série que precisamos analisar.



## Passo 2: Analisar a Série

Simplificando o termo dentro da soma:

$$E(X) = \sum_{n=1}^{\infty} \frac{2^n}{2^n} = \sum_{n=1}^{\infty} 1$$

A série é a soma infinita do número 1:

$$E(X) = 1 + 1 + 1 + 1 + ...$$

Esta é uma série divergente, e sua soma tende ao infinito.

$$E(X) = \infty$$

Resumo: A série resultante é uma soma de infinitos termos iguais a 1, o que claramente diverge para o infinito, provando que a esperança não existe (é infinita).
