---
id: "dantas-cap03-q25"
titulo: "Distribuição condicional de X dado Y=y: dois dados"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "probabilidade"]
referencia: "Dantas, Cap. 3, Q. 25"
---

## Enunciado

(Baseado no Exemplo 2c do capítulo.) Lançam-se dois dados honestos. Seja $X$ o maior valor observado e $Y$ a soma dos valores. Obtenha a distribuição condicional de $X$ dado $Y = y$, para $y \in \{2, 3, \ldots, 12\}$.

## Passo 1: Espaço amostral e distribuição conjunta

**Resumo:** O espaço tem 36 pontos equiprováveis; levanta-se a tabela de $(X, Y)$.

O espaço amostral é $\Omega = \{(i,j) : i,j \in \{1,\ldots,6\}\}$ com $|\Omega| = 36$ e probabilidade $1/36$ cada.

Para cada par $(i,j)$: $X = \max(i,j)$ e $Y = i + j$.

Constrói-se a tabela $P(X = x, Y = y)$ contando os pares $(i,j)$ que satisfazem simultaneamente as duas condições.

## Passo 2: Marginal de $Y$

**Resumo:** $P(Y = y)$ é o número de pares $(i,j)$ com $i+j=y$, dividido por 36.

| $y$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|-----|---|---|---|---|---|---|---|---|----|----|----|
| $36 \cdot P(Y=y)$ | 1 | 2 | 3 | 4 | 5 | 6 | 5 | 4 | 3 | 2 | 1 |

## Passo 3: Distribuição condicional $X \mid Y = y$

**Resumo:** Para cada $y$ fixo, divide a linha conjunta $P(X=x, Y=y)$ por $P(Y=y)$.

$$P(X = x \mid Y = y) = \frac{P(X = x, Y = y)}{P(Y = y)}.$$

**Restrição combinatória:** dado $Y = y$, os pares $(i,j)$ com $i+j=y$ são determinados. O valor de $X = \max(i,j)$ é então fixado por cada par. Portanto, para $y$ fixo, $X \mid Y = y$ assume no máximo dois valores distintos (exceto quando $y$ é par e $i=j$, em que $X$ é determinístico).

**Exemplos:**
- $y = 2$: único par $(1,1)$, logo $X = 1$ com probabilidade 1.
- $y = 3$: pares $(1,2)$ e $(2,1)$, logo $X = 2$ com probabilidade 1.
- $y = 4$: pares $(1,3),(3,1),(2,2)$; $X=3$ com prob $2/3$, $X=2$ com prob $1/3$.
- $y = 7$: pares $(1,6),(6,1),(2,5),(5,2),(3,4),(4,3)$; $X \in \{6,5,4\}$ com probs $2/6, 2/6, 2/6$.

O procedimento generaliza-se para todo $y$ de forma análoga.
