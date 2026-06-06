---
id: "q35-dantas-cap01"
titulo: "Questão 35"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
A probabilidade de que a porta de uma casa esteja trancada à chave é 3/5. Um chaveiro possui 25 chaves das quais três abrem essa porta. Qual a probabilidade de que um indivíduo entre na casa, se ele puder escolher, ao acaso, somente uma chave do chaveiro?

## Solução

Temos dois eventos independentes sobre o estado da casa:
- A porta estar trancada: $P(T) = \frac{3}{5}$
- A porta não estar trancada: $P(T^c) = 1 - \frac{3}{5} = \frac{2}{5}$

Sobre o chaveiro: 
O molho possui 25 chaves, sendo que apenas 3 abrem a porta. O indivíduo escolhe somente 1 chave ao acaso.
A probabilidade de escolher a chave correta é: $P(C) = \frac{3}{25}$

Existem duas situações disjuntas onde o indivíduo consegue entrar na casa:
1. A porta NÃO estava trancada (ele entra direto, não importa a chave).
2. A porta ESTAVA trancada E ele sorteou a chave correta.

Calculando a probabilidade da união desses eventos mutuamente exclusivos:
$$ P(\text{Entrar}) = P(T^c) + P(T \cap C) $$
Como o estado da porta e a escolha da chave são independentes:
$$ P(\text{Entrar}) = P(T^c) + P(T) \times P(C) $$
$$ P(\text{Entrar}) = \frac{2}{5} + \left(\frac{3}{5} \times \frac{3}{25}\right) $$
$$ P(\text{Entrar}) = \frac{2}{5} + \frac{9}{125} $$

Igualando os denominadores (multiplicando a primeira fração por 25 em cima e embaixo):
$$ P(\text{Entrar}) = \frac{50}{125} + \frac{9}{125} = \frac{59}{125} = 0,472 $$

A probabilidade de o indivíduo entrar na casa é de **47,2%**.
