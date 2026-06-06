---
id: "q31-dantas-cap02"
titulo: "Questão 31"
topicos: []
dificuldade: "dificil"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Uma urna contém bolas numeradas de 1 a N. Uma pessoa retira uma bola e a devolve, retira uma segunda bola e a devolve, e procede desta forma até obter uma bola pela segunda vez, isto é, até obter uma bola já retirada anteriormente. Seja X o número total de extrações necessárias para obter esta repetição. 
(a) Obtenha a distribuição de X (dica: calcule $P(X>k)$). 
(b) Mostre que $E(X) = 2 + (1 - \frac{1}{N}) + (1 - \frac{1}{N})(1 - \frac{2}{N}) + \dots + (1 - \frac{1}{N})(1 - \frac{2}{N})\dots(1 - \frac{N-1}{N})$.

## Solução

Este problema é análogo ao célebre "Problema do Aniversário" (Birthday Paradox). A variável $X$ conta quantos sorteios com reposição são realizados até haver a primeira "colisão" (duplicata).

- **(a) Obtenha a distribuição de X:**
Calcularemos $P(X > k)$, ou seja, a probabilidade de precisarmos de mais do que $k$ extrações. Isso equivale ao evento no qual as **primeiras $k$ bolas sorteadas são todas distintas entre si**.
O total de modos de tirar $k$ bolas em sequência (com reposição) é $N^k$.
O número de modos favoráveis (tirar $k$ bolas todas distintas) é o arranjo sem repetição $N \cdot (N-1) \cdot (N-2) \cdots (N-k+1)$.
Portanto, a probabilidade é:
$$ P(X > k) = \frac{N \cdot (N-1) \cdots (N-k+1)}{N^k} $$
Dividindo termo a termo pelo $N$ no denominador:
$$ P(X > k) = 1 \cdot \left(1 - \frac{1}{N}\right) \left(1 - \frac{2}{N}\right) \cdots \left(1 - \frac{k-1}{N}\right) $$
*(Isso vale para $1 \le k \le N$. Se $k \ge N+1$, não há como ter mais que N elementos distintos, logo $P(X > N) = 0$. E para $k=0$ e $k=1$, é óbvio que $P(X>0)=1$ e $P(X>1)=1$, pois é impossível repetir bola em menos de 2 sorteios).*
Com a probabilidade de sobrevivência obtida, a Função de Probabilidade da variável discreta $X$ fica:
$$ P(X = k) = P(X > k-1) - P(X > k) $$
para $k \in \{2, 3, \dots, N+1\}$.

- **(b) Mostre a expressão para a Esperança $E(X)$:**
Uma propriedade importante de variáveis aleatórias discretas inteiras não-negativas permite o cálculo da esperança a partir da função de sobrevivência:
$$ E(X) = \sum_{k=0}^{\infty} P(X > k) $$
Separando os primeiros termos:
$$ E(X) = P(X > 0) + P(X > 1) + \sum_{k=2}^{N} P(X > k) $$
Como a primeira extração nunca é repetida e a repetição exige ao menos 2 sorteios, $P(X>0) = 1$ e $P(X>1) = 1$. Logo:
$$ E(X) = 1 + 1 + P(X > 2) + P(X > 3) + \dots + P(X > N) $$
Substituindo cada um dos $P(X > k)$ com base na fórmula derivada em (a):
$$ E(X) = 2 + \left(1 - \frac{1}{N}\right) + \left(1 - \frac{1}{N}\right)\left(1 - \frac{2}{N}\right) + \dots + \left(1 - \frac{1}{N}\right)\cdots\left(1 - \frac{N-1}{N}\right) $$
O que comprova a expressão solicitada. *(Nota: O enunciado usa "n", mas a lógica aplica-se usando o N maiúsculo conforme ajustado na solução para não misturar com contadores k).*
