---
id: "dantas-cap03-q03"
titulo: "Distribuição conjunta do número de testes para achar transistores defeituosos"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Tabela conjunta de (N₁, N₂) com N₁ ∈ {1,2,3,4}, N₂ ∈ {1,...,5-N₁}"
tags: ["probabilidade", "fdp-valida"]
referencia: "Dantas, Cap. 3, Q. 3"
---

# Distribuição conjunta do número de testes para transistores defeituosos

## Enunciado

Um pacote contém 5 transistores, dos quais 2 são defeituosos. Os transistores são testados um a um (sem reposição) até que ambos os defeituosos sejam identificados. Defina:

- $N_1$ = número de testes necessários para encontrar o **1º defeituoso**;
- $N_2$ = número de testes **adicionais** (após o 1º defeituoso) para encontrar o **2º defeituoso**.

Determine a distribuição conjunta de $(N_1, N_2)$.

---

## Passo 1: Suporte e interpretação

**Resumo:** Identifica os valores possíveis de $N_1$ e $N_2$ com base na sequência de testes.

Há 2 defeituosos (D) e 3 bons (B) entre 5 transistores.

- $N_1 \in \{1, 2, 3, 4\}$: o 1º defeituoso pode aparecer na posição 1, 2, 3 ou 4 (não na 5ª, pois haveria 2 defeituosos entre 5).
- $N_2 \in \{1, 2, \ldots, 5 - N_1\}$: os testes adicionais vão de 1 até o máximo restante.

O número total de testes até encontrar ambos é $N_1 + N_2 \leq 5$.

---

## Passo 2: Fórmula de probabilidade

**Resumo:** Usa a estrutura combinatória dos arranjos de 5 transistores.

Considere a sequência aleatória dos 5 transistores. O 1º defeituoso está na posição $N_1 = n_1$ se:
- As primeiras $n_1 - 1$ posições são bons.
- A posição $n_1$ é um defeituoso.

O 2º defeituoso está na posição $n_1 + n_2$ se:
- As posições $n_1 + 1, \ldots, n_1 + n_2 - 1$ são bons.
- A posição $n_1 + n_2$ é o 2º defeituoso.

$$P(N_1 = n_1, N_2 = n_2) = \frac{\text{(nº de arranjos favoráveis)}}{\text{(nº total de arranjos)}}$$

O número total de maneiras de dispor as posições dos 2 defeituosos em 5 posições é $\binom{5}{2} = 10$.

Para o evento $\{N_1 = n_1, N_2 = n_2\}$: o 1º defeituoso está na posição $n_1$ e o 2º na posição $n_1 + n_2$. Isso é **um único par de posições** para os defeituosos.

Logo:

$$P(N_1 = n_1, N_2 = n_2) = \frac{1}{10}, \quad \text{para cada par válido } (n_1, n_2).$$

---

## Passo 3: Tabela conjunta

**Resumo:** Lista todos os pares $(n_1, n_2)$ com $n_1 + n_2 \leq 5$ e atribui probabilidade $1/10$ a cada.

Os pares válidos são aqueles com $n_1 \geq 1$, $n_2 \geq 1$, $n_1 + n_2 \leq 5$:

| $n_2 \backslash n_1$ | 1 | 2 | 3 | 4 |
|:---:|:---:|:---:|:---:|:---:|
| **1** | 1/10 | 1/10 | 1/10 | 1/10 |
| **2** | 1/10 | 1/10 | 1/10 | 0 |
| **3** | 1/10 | 1/10 | 0 | 0 |
| **4** | 1/10 | 0 | 0 | 0 |

Total: 10 pares × $1/10$ = 1. ✓

---

## Passo 4: Marginais

**Resumo:** Calcula as distribuições marginais de $N_1$ e $N_2$.

**Marginal de $N_1$:**

$$P(N_1 = 1) = \frac{4}{10}, \quad P(N_1 = 2) = \frac{3}{10}, \quad P(N_1 = 3) = \frac{2}{10}, \quad P(N_1 = 4) = \frac{1}{10}.$$

Isso corresponde a $P(N_1 = n_1) = (5 - n_1)/10$, pois existem $5 - n_1$ posições possíveis para o 2º defeituoso após a posição $n_1$.

**Marginal de $N_2$:**

$$P(N_2 = 1) = \frac{4}{10}, \quad P(N_2 = 2) = \frac{3}{10}, \quad P(N_2 = 3) = \frac{2}{10}, \quad P(N_2 = 4) = \frac{1}{10}.$$

Por simetria, $N_1$ e $N_2$ têm a mesma distribuição marginal (ambas uniformes em $\{1,2,3,4\}$ com pesos decrescentes).
