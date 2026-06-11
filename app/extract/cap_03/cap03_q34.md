---
id: "dantas-cap03-q34"
titulo: "Lançamentos até R caras consecutivas: E[T_R]"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "condicional"]
referencia: "Dantas, Cap. 3, Q. 34"
---

## Enunciado

Uma moeda é lançada repetidamente até obter $R$ caras consecutivas. Seja $p$ a probabilidade de cara em cada lançamento (independentes), $q = 1-p$. Seja $T_R$ o número de lançamentos necessários para obter $R$ caras consecutivas.

**(a)** Determine $E[T_R \mid T_{R-1}]$.

**(b)** Determine $E[T_R]$ em termos de $E[T_{R-1}]$.

**(c)** Calcule $E[T_1]$.

**(d)** Determine $E[T_R]$ em forma fechada.

## Passo 1: Item (a) — $E[T_R \mid T_{R-1}]$

**Resumo:** Após atingir $R-1$ caras consecutivas, o próximo lançamento é cara (prob $p$) ou coroa (prob $q$), reiniciando o processo.

Seja $t = T_{R-1}$ o momento em que se completam $R-1$ caras consecutivas. Após esse instante:

- Com probabilidade $p$: o próximo lançamento é cara → $R$ caras consecutivas completas em $T_{R-1} + 1$ lançamentos.
- Com probabilidade $q$: o próximo lançamento é coroa → o processo reinicia do zero após $T_{R-1} + 1$ lançamentos.

Portanto, condicionando em $T_{R-1} = t$:

$$E[T_R \mid T_{R-1} = t] = p(t+1) + q(t + 1 + E[T_R]) = t + 1 + q \cdot E[T_R].$$

Em notação de v.a.:

$$\boxed{E[T_R \mid T_{R-1}] = T_{R-1} + 1 + q \cdot E[T_R].}$$

## Passo 2: Item (b) — $E[T_R]$ em termos de $E[T_{R-1}]$

**Resumo:** Toma a esperança incondicional do resultado do passo anterior.

Tomando $E[\cdot]$ no resultado do passo 1:

$$E[T_R] = E[T_{R-1}] + 1 + q \cdot E[T_R].$$

$$E[T_R](1 - q) = E[T_{R-1}] + 1 \implies p \cdot E[T_R] = E[T_{R-1}] + 1.$$

$$\boxed{E[T_R] = \frac{E[T_{R-1}] + 1}{p}.}$$

## Passo 3: Item (c) — $E[T_1]$

**Resumo:** $T_1$ é o tempo até a primeira cara: geométrica com parâmetro $p$, logo $E[T_1] = 1/p$.

$T_1 \sim \text{Geométrica}(p)$ (número de lançamentos até o primeiro sucesso), portanto:

$$\boxed{E[T_1] = \frac{1}{p}.}$$

Alternativamente pela recorrência com $E[T_0] = 0$: $E[T_1] = (E[T_0]+1)/p = 1/p$. ✓

## Passo 4: Item (d) — Fórmula fechada para $E[T_R]$

**Resumo:** Aplica a recorrência $R$ vezes a partir de $E[T_0]=0$.

Da recorrência $E[T_R] = \frac{E[T_{R-1}] + 1}{p}$, aplicando iterativamente:

$$E[T_R] = \frac{E[T_{R-1}] + 1}{p} = \frac{1}{p}\left(\frac{E[T_{R-2}]+1}{p} + 1\right) = \frac{E[T_{R-2}]}{p^2} + \frac{1}{p^2} + \frac{1}{p}.$$

Por indução (com $E[T_0] = 0$):

$$E[T_R] = \frac{1}{p} + \frac{1}{p^2} + \cdots + \frac{1}{p^R} = \sum_{k=1}^R \frac{1}{p^k}.$$

$$\boxed{E[T_R] = \sum_{k=1}^{R} \frac{1}{p^k} = \frac{1}{p} \cdot \frac{1 - (1/p)^R}{1 - 1/p} = \frac{1 - p^{-R}}{1-p} \cdot \frac{1}{p^0} = \frac{p^{-1} - p^{-(R+1)}}{1 - p^{-1}} \cdot \ldots}$$

Forma mais limpa: $E[T_R] = \dfrac{1}{p} + \dfrac{1}{p^2} + \cdots + \dfrac{1}{p^R}$.

Para $p = 1/2$: $E[T_R] = 2 + 4 + \cdots + 2^R = 2^{R+1} - 2$.
