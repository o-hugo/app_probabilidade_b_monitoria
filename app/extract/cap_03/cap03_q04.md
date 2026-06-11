---
id: "dantas-cap03-q04"
titulo: "Distribuição conjunta de duas retiradas sem reposição de urna {1,2,3}"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "p(x,y) = 1/6 para x ≠ y; P(X < Y) = 1/2"
tags: ["probabilidade", "fdp-valida"]
referencia: "Dantas, Cap. 3, Q. 4"
---

# Distribuição conjunta de duas retiradas sem reposição de urna {1,2,3}

## Enunciado

Uma urna contém as bolas numeradas 1, 2 e 3. Retiram-se duas bolas **sem reposição**. Seja $X$ o número da 1ª bola e $Y$ o número da 2ª bola retirada.

**(a)** Determine a distribuição conjunta de $(X, Y)$.

**(b)** Calcule $P(X < Y)$.

---

## Passo 1: Distribuição conjunta

**Resumo:** O espaço amostral tem 6 pares ordenados equiprováveis com $x \neq y$.

Como a retirada é sem reposição, os valores de $X$ e $Y$ são sempre distintos. O espaço amostral é o conjunto de todos os pares ordenados $(x, y)$ com $x, y \in \{1, 2, 3\}$ e $x \neq y$, totalizando $3 \times 2 = 6$ pares.

Cada par tem probabilidade igual $1/6$, logo:

$$p(x, y) = P(X = x, Y = y) = \begin{cases} \dfrac{1}{6} & \text{se } x, y \in \{1,2,3\},\ x \neq y \\ 0 & \text{caso contrário.} \end{cases}$$

**Tabela conjunta** $p(x,y) \times 6$:

| $y \backslash x$ | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|
| **1** | 0 | 1 | 1 |
| **2** | 1 | 0 | 1 |
| **3** | 1 | 1 | 0 |

Soma total: 6 × $1/6$ = 1. ✓

As marginais são uniformes: $P(X = x) = 1/3$ e $P(Y = y) = 1/3$ para $x, y \in \{1, 2, 3\}$.

---

## Passo 2: Calcular P(X < Y)

**Resumo:** Soma as probabilidades dos pares com $x < y$.

Os pares com $X < Y$ são: $(1,2)$, $(1,3)$, $(2,3)$.

$$P(X < Y) = p(1,2) + p(1,3) + p(2,3) = \frac{1}{6} + \frac{1}{6} + \frac{1}{6} = \frac{3}{6} = \frac{1}{2}.$$

Por simetria entre os pares $(x, y)$ com $x < y$ e $(x, y)$ com $x > y$, o resultado $P(X < Y) = 1/2$ era esperado (como $P(X = Y) = 0$ aqui).
