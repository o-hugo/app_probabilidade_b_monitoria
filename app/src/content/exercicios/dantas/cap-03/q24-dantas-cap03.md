---
id: "dantas-cap03-q24"
titulo: "Distribuição condicional Y|X e esperanças iteradas"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 24"
---

## Enunciado

(Baseado no Exemplo 1 do capítulo.) Seja $(X, Y)$ com distribuição conjunta discreta, $X \in \{0,1,2,3\}$.

**(a)** Determine a distribuição condicional de $Y$ dado $X = x$ para cada $x = 0, 1, 2, 3$.

**(b)** Calcule a esperança condicional $E(Y \mid X = x)$ para cada $x$.

**(c)** Calcule $E(Y)$ usando os valores do item **(b)** e o **lema das esperanças iteradas** (lei da esperança total):

$$E(Y) = E[E(Y \mid X)].$$

## Passo 1: Distribuição condicional $Y \mid X = x$

**Resumo:** Divide cada linha da tabela conjunta pela marginal de $X$.

A distribuição condicional é definida por:

$$P(Y = y \mid X = x) = \frac{P(X = x, Y = y)}{P(X = x)}.$$

Para cada $x$, calcule a marginal $P(X = x) = \sum_y P(X=x, Y=y)$ e depois normalize cada entrada da linha.

## Passo 2: Esperança condicional $E(Y \mid X = x)$

**Resumo:** Para cada valor fixo $x$, calcula-se a média ponderada de $Y$ pela condicional.

$$E(Y \mid X = x) = \sum_y y \cdot P(Y = y \mid X = x).$$

Obtemos assim uma função $g(x) = E(Y \mid X = x)$ definida para $x = 0, 1, 2, 3$.

## Passo 3: Aplicação das esperanças iteradas

**Resumo:** $E(Y) = \sum_x E(Y \mid X = x) P(X = x)$ — a lei da esperança total.

Pelo lema das esperanças iteradas:

$$E(Y) = E[E(Y \mid X)] = \sum_{x=0}^{3} E(Y \mid X = x) \cdot P(X = x).$$

Substituindo os valores obtidos nos passos anteriores:

$$E(Y) = g(0) \cdot P(X=0) + g(1) \cdot P(X=1) + g(2) \cdot P(X=2) + g(3) \cdot P(X=3).$$

Este resultado deve coincidir com $E(Y) = \sum_y y \cdot P(Y=y)$ calculado diretamente pela marginal de $Y$, servindo como verificação.
