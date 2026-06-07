---
id: "dantas-cap01-q28"
titulo: "Probabilidade em Extracao de Cartas do Baralho"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 1, Q. 28"
---

## Enunciado
Duas cartas são retiradas simultaneamente de um baralho. Qual é a probabilidade de que: 
(a) ambas sejam de espadas; 
(b) uma seja de espadas e a outra de copas.

## Solução

Um baralho tradicional possui 52 cartas, divididas em 4 naipes de 13 cartas cada (Espadas, Copas, Ouros, Paus).
Como 2 cartas são retiradas simultaneamente, a ordem não importa. O total de formas de retirar 2 cartas do baralho é:
$$ n(\Omega) = \binom{52}{2} = \frac{52 \times 51}{2} = 1326 $$

- **(a) Ambas sejam de espadas:**
Existem 13 cartas de espadas. O número de maneiras de escolher 2 espadas é:
$$ n(A) = \binom{13}{2} = \frac{13 \times 12}{2} = 78 $$
A probabilidade é:
$$ P(A) = \frac{78}{1326} = \frac{1}{17} \approx 0,0588 $$

- **(b) Uma seja de espadas e a outra de copas:**
Existem 13 cartas de espadas e 13 cartas de copas. Como devemos escolher uma de cada naipe simultaneamente:
$$ n(B) = \binom{13}{1} \times \binom{13}{1} = 13 \times 13 = 169 $$
A probabilidade é:
$$ P(B) = \frac{169}{1326} = \frac{13}{102} \approx 0,1274 $$
