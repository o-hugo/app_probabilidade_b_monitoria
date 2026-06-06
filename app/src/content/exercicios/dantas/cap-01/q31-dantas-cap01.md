---
id: "q31-dantas-cap01"
titulo: "Questão 31"
topicos: []
dificuldade: "dificil"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Ache a probabilidade de que uma mão de pôquer seja um:
(a) royal flush (dez, valete, dama, rei e ás do mesmo naipe);
(b) quatro de um mesmo tipo (quatro cartas do mesmo valor);
(c) trinca e par (um par e uma trinca de cartas do mesmo valor);
(d) seguida (cinco cartas em seqüência, não importando o naipe);
(e) três cartas do mesmo tipo (três valores iguais mais duas cartas diferentes);
(f) dois pares (dois pares do mesmo valor mais uma outra carta);
(g) um par (um par de valores iguais mais três cartas diferentes).

## Solução

Em uma mão de pôquer compram-se 5 cartas de um baralho padrão de 52 cartas. O total de mãos possíveis (o espaço amostral) é:
$$n(\Omega) = \binom{52}{5} = \frac{52 \times 51 \times 50 \times 49 \times 48}{120} = 2.598.960$$

- **(a) Royal Flush (Sequência de Dez a Ás, do mesmo naipe)**
Como o naipe é livre para se escolher e os valores são estritamente fixos (10, J, Q, K, A), há apenas 1 maneira por naipe. Sendo 4 naipes:
Favoráveis = 4
$$P(\text{Royal Flush}) = \frac{4}{2.598.960} \approx 0,00015\%$$

- **(b) Quadra (Quatro cartas do mesmo valor)**
Escolhe-se 1 valor para ser a quadra (ex: 4 Ases, 4 Reis). Escolhe-se as 4 cartas desse valor, restando 1 carta para fechar a mão que deve ser qualquer uma das $52 - 4 = 48$ cartas restantes.
Favoráveis = $13 \times \binom{4}{4} \times 48 = 13 \times 1 \times 48 = 624$
$$P(\text{Quadra}) = \frac{624}{2.598.960} \approx 0,024\%$$

- **(c) Full House (Trinca e Par)**
Escolhe-se um valor para a trinca ($\binom{13}{1}$), depois 3 naipes dentre os 4 desse valor ($\binom{4}{3}$).
Em seguida, escolhe-se um valor diferente para o par ($\binom{12}{1}$) e 2 naipes dentre os 4 ($\binom{4}{2}$).
Favoráveis = $13 \times 4 \times 12 \times 6 = 3.744$
$$P(\text{Full House}) = \frac{3.744}{2.598.960} \approx 0,144\%$$

- **(d) Straight (Seguida ou Sequência simples, não sendo do mesmo naipe)**
*(Assumiremos Straight simples e excluiremos Flush/Royal Flush)*.
Existem 10 sequências possíveis de início-fim de valores no baralho (A-2-3-4-5, 2-3-4-5-6, ..., 10-J-Q-K-A). 
Para cada um dos 5 valores da sequência, o naipe é independente, gerando $4^5 = 1024$ formas de se combinar os naipes. 
Total combinando valores e naipes = $10 \times 1024 = 10.240$.
Se for tudo do mesmo naipe, isso se configura num Straight Flush, que deve ser excluído (pois "seguida" exclui Straight Flushes, que têm nomes e rankings próprios no Poker). Há $10 \times 4 = 40$ mãos de Straight Flush.
Favoráveis = $10.240 - 40 = 10.200$
$$P(\text{Straight}) = \frac{10.200}{2.598.960} \approx 0,392\%$$

- **(e) Trinca (Apenas Três do mesmo tipo, as demais isoladas)**
Escolhe-se 1 valor para trinca (13) e os 3 naipes ($\binom{4}{3} = 4$). 
Para as outras 2 cartas, escolhe-se 2 valores dos 12 restantes ($\binom{12}{2} = 66$) para não formarem par entre si. O naipe de cada uma pode ser qualquer um de 4 possíveis ($4^2 = 16$).
Favoráveis = $13 \times 4 \times 66 \times 16 = 54.912$
$$P(\text{Trinca}) = \frac{54.912}{2.598.960} \approx 2,11\%$$

- **(f) Dois Pares (Apenas dois pares e um isolado)**
Escolhe-se 2 valores para os dois pares ($\binom{13}{2} = 78$), os naipes de cada par ($\binom{4}{2} \times \binom{4}{2} = 36$). 
Escolhe-se 1 valor dos 11 restantes para a 5ª carta e seu naipe (4).
Favoráveis = $78 \times 36 \times 11 \times 4 = 123.552$
$$P(\text{Dois Pares}) = \frac{123.552}{2.598.960} \approx 4,75\%$$

- **(g) Um Par (Apenas um par)**
Escolhe-se 1 valor para o par (13) e seus naipes ($\binom{4}{2} = 6$). 
A mão precisa de mais 3 cartas, todas de valores diferentes. Escolhe-se 3 valores dos 12 restantes ($\binom{12}{3} = 220$) e 1 naipe para cada uma das 3 cartas ($4^3 = 64$).
Favoráveis = $13 \times 6 \times 220 \times 64 = 1.098.240$
$$P(\text{Um Par}) = \frac{1.098.240}{2.598.960} \approx 42,26\%$$
