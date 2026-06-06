---
id: "questoes-q25-livro-exemplo-241-moeda"
titulo: "Exemplo 2.4.1 (Moeda)"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Determinar a função de distribuição da variável aleatória X do exemplo 2.1.1, que é igual ao número de caras em dois lançamentos de uma moeda.

## Solução

## Passo 1: Definir a Distribuição de Probabilidade de X

X é o número de caras em 2 lançamentos. Os possíveis resultados são {CC, C$\bar{C}$, $\bar{C}$C, $\bar{C}\bar{C}$}.<br>Os valores de X são {0, 1, 2}.

$P(X=0) = P(\{\bar{C}\bar{C}\}) = 1/4$

$P(X=1) = P(\{C\bar{C}, \bar{C}C\}) = 2/4 = 1/2$

$P(X=2) = P(\{CC\}) = 1/4$

Resumo: Primeiro, estabelecemos a distribuição de probabilidade da variável aleatória discreta X.



## Passo 2: Calcular a FDA, $F(x) = P(X \le x)$, por intervalos

A FDA é calculada acumulando as probabilidades.

**Para $x < 0$:** Não há valores de X menores que 0. $F(x) = P(X \le x) = 0$.

**Para $0 \le x < 1$:** O único valor de X $\le x$ é 0. $F(x) = P(X \le 0) = P(X=0) = 1/4$.

**Para $1 \le x < 2$:** Os valores de X $\le x$ são 0 e 1. $F(x) = P(X \le 1) = P(X=0) + P(X=1) = 1/4 + 1/2 = 3/4$.

**Para $x \ge 2$:** Todos os valores de X são $\le x$. $F(x) = P(X \le 2) = P(X=0)+P(X=1)+P(X=2) = 1/4+1/2+1/4 = 1$.

Resumo: Calculamos a probabilidade acumulada para cada intervalo de x, somando as probabilidades dos valores de X contidos no intervalo $(-\infty, x]$.



## Passo 3: Escrever a FDA Completa

Juntando os resultados, a FDA é uma função em degraus:

$$ F(x) = \begin{cases} 0, & x < 0 \\ 1/4, & 0 \le x < 1 \\ 3/4, & 1 \le x < 2 \\ 1, & x \ge 2 \end{cases} $$
