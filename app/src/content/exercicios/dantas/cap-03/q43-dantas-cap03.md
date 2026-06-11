---
id: "dantas-cap03-q43"
titulo: "Estatísticas de Ordem: Mínimo, Máximo e Distribuição Conjunta"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["fda", "probabilidade", "metodo-fda"]
referencia: "Dantas, Cap. 3, Q. 43"
---

## Enunciado

Sejam $X_1, \ldots, X_n$ i.i.d. com f.d.a. $F$. Defina as estatísticas de ordem $X_{(1)} \leq X_{(2)} \leq \cdots \leq X_{(n)}$.

**(a)** Verifique que $F_{X_{(1)}}(x) = 1 - [1-F(x)]^n$ e $F_{X_{(n)}}(x) = [F(x)]^n$.

**(b)** Obtenha a f.d.a. conjunta de $(X_{(1)}, X_{(n)})$, i.e., $P(X_{(1)} \leq a,\, X_{(n)} \leq b)$.

## Passo 1: Item (a) — F.d.a. do máximo $X_{(n)}$

$X_{(n)} = \max\{X_1,\ldots,X_n\} \leq x$ se e somente se todos $X_i \leq x$. Por independência:

$$F_{X_{(n)}}(x) = P(X_1 \leq x, \ldots, X_n \leq x) = [F(x)]^n.$$

**Resumo:** $F_{X_{(n)}}(x) = [F(x)]^n$.

## Passo 2: F.d.a. do mínimo $X_{(1)}$

$X_{(1)} = \min\{X_1,\ldots,X_n\} > x$ se e somente se todos $X_i > x$. Portanto:

$$P(X_{(1)} > x) = [1-F(x)]^n \implies F_{X_{(1)}}(x) = 1 - [1-F(x)]^n.$$

**Resumo:** $F_{X_{(1)}}(x) = 1-[1-F(x)]^n$.

## Passo 3: Item (b) — Distribuição conjunta de $(X_{(1)}, X_{(n)})$

Para $a \leq b$:

$$P(X_{(1)} \leq a,\, X_{(n)} \leq b) = P(X_{(n)} \leq b) - P(X_{(1)} > a,\, X_{(n)} \leq b).$$

O evento $\{X_{(1)} > a, X_{(n)} \leq b\}$ = todos os $X_i$ pertencem ao intervalo $(a, b]$:

$$P(X_{(1)} > a,\, X_{(n)} \leq b) = [F(b) - F(a)]^n.$$

Portanto, para $a \leq b$:

$$P(X_{(1)} \leq a,\, X_{(n)} \leq b) = [F(b)]^n - [F(b) - F(a)]^n.$$

Para $a > b$: $P(X_{(1)} \leq a, X_{(n)} \leq b) = P(X_{(n)} \leq b) = [F(b)]^n$.

**Resumo:** $P(X_{(1)}\leq a, X_{(n)}\leq b) = [F(b)]^n - [F(b)-F(a)]^n$ para $a\leq b$.
