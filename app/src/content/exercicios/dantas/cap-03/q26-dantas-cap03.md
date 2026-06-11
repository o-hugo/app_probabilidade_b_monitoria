---
id: "dantas-cap03-q26"
titulo: "Distribuição condicional Y|X e esperança condicional (tabela 2×2)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 26"
---

## Enunciado

(Baseado no Exemplo 7 do capítulo.) A distribuição conjunta de $(X, Y)$ é:

| | $Y=1$ | $Y=2$ |
|---|---|---|
| $X=1$ | $1/8$ | $1/4$ |
| $X=2$ | $1/8$ | $1/2$ |

**(a)** Determine a distribuição condicional de $Y$ dado $X = x$, para $x = 1, 2$.

**(b)** Calcule $E(Y \mid X = x)$ para $x = 1, 2$.

**(c)** Calcule $E(Y)$ usando os resultados de **(b)** e a lei da esperança total.

## Passo 1: Marginais de $X$

**Resumo:** As marginais são $P(X=1) = 3/8$ e $P(X=2) = 5/8$.

$$P(X=1) = \frac{1}{8} + \frac{1}{4} = \frac{3}{8}, \qquad P(X=2) = \frac{1}{8} + \frac{1}{2} = \frac{5}{8}.$$

## Passo 2: Distribuição condicional $Y \mid X = x$

**Resumo:** Divide cada linha da tabela pela marginal correspondente.

**Para $X = 1$:**

$$P(Y=1 \mid X=1) = \frac{1/8}{3/8} = \frac{1}{3}, \qquad P(Y=2 \mid X=1) = \frac{1/4}{3/8} = \frac{2}{3}.$$

**Para $X = 2$:**

$$P(Y=1 \mid X=2) = \frac{1/8}{5/8} = \frac{1}{5}, \qquad P(Y=2 \mid X=2) = \frac{1/2}{5/8} = \frac{4}{5}.$$

## Passo 3: Esperança condicional $E(Y \mid X = x)$

**Resumo:** $E(Y|X=1) = 5/3$ e $E(Y|X=2) = 9/5$.

$$E(Y \mid X=1) = 1 \cdot \frac{1}{3} + 2 \cdot \frac{2}{3} = \frac{1+4}{3} = \frac{5}{3}.$$

$$E(Y \mid X=2) = 1 \cdot \frac{1}{5} + 2 \cdot \frac{4}{5} = \frac{1+8}{5} = \frac{9}{5}.$$

## Passo 4: $E(Y)$ pela lei da esperança total

**Resumo:** $E(Y) = E[E(Y|X)] = 5/3 \cdot 3/8 + 9/5 \cdot 5/8 = 7/4$.

$$E(Y) = E(Y \mid X=1) \cdot P(X=1) + E(Y \mid X=2) \cdot P(X=2)$$

$$= \frac{5}{3} \cdot \frac{3}{8} + \frac{9}{5} \cdot \frac{5}{8} = \frac{5}{8} + \frac{9}{8} = \frac{14}{8} = \frac{7}{4}.$$

**Verificação direta:** $P(Y=1) = 1/8 + 1/8 = 1/4$; $P(Y=2) = 1/4 + 1/2 = 3/4$.

$$E(Y) = 1 \cdot \frac{1}{4} + 2 \cdot \frac{3}{4} = \frac{7}{4}. \checkmark$$
