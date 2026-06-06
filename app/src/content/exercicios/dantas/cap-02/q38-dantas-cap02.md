---
id: "q38-dantas-cap02"
titulo: "Questão 38"
topicos: []
dificuldade: "dificil"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Para um grupo de $n$ pessoas, determine o número esperado de dias do ano que são aniversário de exatamente $k$ pessoas, $k \le n$. (Suponha que o ano tem 365 dias e que todos os arranjos são equiprováveis.)

## Solução

Neste problema, o mais fácil é definir variáveis indicadoras (dummy variables) para cada dia do ano e explorar a linearidade da esperança.

Sejam $D = 365$ os dias de um ano.
Para cada dia $i$ (onde $i = 1, 2, \dots, 365$), definimos a variável aleatória indicadora $X_i$:
$$ X_i = \begin{cases} 1, & \text{se exatamente } k \text{ pessoas fazem aniversário no dia } i \\ 0, & \text{caso contrário} \end{cases} $$

A variável aleatória total que nos interessa é $S$, o número de dias com exatamente $k$ aniversariantes:
$$ S = \sum_{i=1}^{365} X_i $$
A esperança (valor esperado) que buscamos é $E(S)$:
$$ E(S) = E\left( \sum_{i=1}^{365} X_i \right) = \sum_{i=1}^{365} E(X_i) $$

Para encontrar $E(X_i)$, que é idêntico a $P(X_i = 1)$, notamos que a alocação de pessoas em um dado dia $i$ segue uma distribuição Binomial. Temos $n$ tentativas (pessoas), e cada uma tem a probabilidade $p = \frac{1}{365}$ de cair no dia $i$, e $q = \frac{364}{365}$ de não cair no dia $i$.
Queremos exatamente $k$ sucessos (aniversariantes) naquele dia $i$:
$$ P(X_i = 1) = \binom{n}{k} \left(\frac{1}{365}\right)^k \left(\frac{364}{365}\right)^{n-k} $$

Como a distribuição de probabilidades é perfeitamente idêntica (simétrica) para cada um dos 365 dias:
$$ E(S) = 365 \cdot P(X_1 = 1) $$
$$ E(S) = 365 \binom{n}{k} \left(\frac{1}{365}\right)^k \left(\frac{364}{365}\right)^{n-k} $$

Esse é o número esperado de dias no ano em que exatamente $k$ pessoas farão aniversário.
