---
id: "questoes-q32-livro-exemplo-283-fgm-bernoulli"
titulo: "Exemplo 2.8.3 (FGM Bernoulli)"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Seja X uma variável aleatória que assume os valores zero e um, com probabilidades iguais a $1-p$ e $p$ respectivamente. Determinar a função geradora de momentos de X.

## Solução

## Passo 1: Identificar a Distribuição

Uma variável aleatória que assume apenas os valores 0 e 1 é conhecida como variável de Bernoulli. Sua distribuição de probabilidade é:

$P(X=1) = p$

$P(X=0) = 1-p$



## Passo 2: Usar a Definição de FGM para Variáveis Discretas

A Função Geradora de Momentos (FGM) é $\phi_X(t) = E(e^{tX})$. Para uma variável discreta, isso é $\sum_i e^{tx_i} P(X=x_i)$.

Temos dois valores para X: 0 e 1.

$$\phi_X(t) = e^{t \cdot 0} P(X=0) + e^{t \cdot 1} P(X=1)$$

Resumo: Aplicamos a definição da FGM, criando uma soma com um termo para cada valor possível de X.



## Passo 3: Substituir as Probabilidades e Simplificar

$$ \phi_X(t) = (e^0)(1-p) + (e^t)(p) $$

Como $e^0 = 1$, a expressão se simplifica para:

$$ \phi_X(t) = 1(1-p) + p e^t = 1 - p + pe^t $$

Esta esperança é finita para todos os valores reais de $t$, então a FGM está definida em $(-\infty, \infty)$.

Resumo: Substituímos as probabilidades e simplificamos a expressão para encontrar a forma final da FGM de uma variável de Bernoulli.
