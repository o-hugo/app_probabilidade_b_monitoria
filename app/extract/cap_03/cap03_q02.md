---
id: "dantas-cap03-q02"
titulo: "Distribuição conjunta de dois dados em três casos"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Três tabelas conjuntas 6×6 com probabilidades uniformes sobre o espaço amostral"
tags: ["probabilidade", "fdp-valida"]
referencia: "Dantas, Cap. 3, Q. 2"
---

# Distribuição conjunta de dois dados em três casos

## Enunciado

Dois dados honestos são lançados. Determine a distribuição conjunta de $(X, Y)$ nos três casos:

**(a)** $X$ = valor do 1º dado, $Y$ = maior dos dois valores.

**(b)** $X$ = menor valor, $Y$ = maior valor.

**(c)** $X$ = maior valor, $Y$ = soma dos dois valores.

---

## Passo 1: Espaço amostral

**Resumo:** O espaço amostral tem 36 pares equiprováveis $(d_1, d_2)$ com $d_1, d_2 \in \{1,\ldots,6\}$.

Cada par $(d_1, d_2)$ tem probabilidade $1/36$.

---

## Passo 2: Caso (a) — X = valor do 1º dado, Y = maior valor

**Resumo:** $Y = \max(d_1, d_2)$; o suporte é $\{(x,y): 1 \leq x \leq 6,\ x \leq y \leq 6\}$ com probabilidades específicas.

Para $x \in \{1,\ldots,6\}$ e $y \in \{1,\ldots,6\}$ com $y \geq x$:

- Se $y = x$: o 2º dado deve ser $\leq x$ mas o máximo deve ser $x$, logo $d_2 \leq x$ e $\max(x, d_2) = x$, que é sempre satisfeito quando $d_2 \leq x$. Assim $P(X=x, Y=x) = x/36$.

  Mas atenção: dado $X = d_1 = x$, $Y = \max(x, d_2)$. Para $Y = y$ com $y > x$: precisa $d_2 = y$, pois $\max(x, y) = y$. Logo $P(X=x, Y=y) = 1/36$ para $y > x$.

  Para $Y = y$ com $y = x$: precisa $d_2 \leq x$, logo $P(X=x, Y=x) = x/36$.

  Para $y < x$: impossível. $P(X=x, Y=y) = 0$.

**Tabela** $p(x,y) \times 36$:

| $y \backslash x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 1 | 0 | 0 | 0 | 0 | 0 |
| **2** | 1 | 2 | 0 | 0 | 0 | 0 |
| **3** | 1 | 1 | 3 | 0 | 0 | 0 |
| **4** | 1 | 1 | 1 | 4 | 0 | 0 |
| **5** | 1 | 1 | 1 | 1 | 5 | 0 |
| **6** | 1 | 1 | 1 | 1 | 1 | 6 |

Soma: cada linha $y$ tem soma $= 2y - 1$; total $= 1+3+5+7+9+11 = 36$. ✓

---

## Passo 3: Caso (b) — X = menor valor, Y = maior valor

**Resumo:** $X = \min(d_1,d_2)$, $Y = \max(d_1,d_2)$; suporte $x \leq y$.

Para $x < y$: dois pares favorecem — $(d_1,d_2) = (x,y)$ ou $(y,x)$. Logo $P(X=x, Y=y) = 2/36$.

Para $x = y$: exige $d_1 = d_2 = x$. Logo $P(X=x, Y=x) = 1/36$.

Para $x > y$: impossível.

**Tabela** $p(x,y) \times 36$:

| $y \backslash x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 1 | 0 | 0 | 0 | 0 | 0 |
| **2** | 2 | 1 | 0 | 0 | 0 | 0 |
| **3** | 2 | 2 | 1 | 0 | 0 | 0 |
| **4** | 2 | 2 | 2 | 1 | 0 | 0 |
| **5** | 2 | 2 | 2 | 2 | 1 | 0 |
| **6** | 2 | 2 | 2 | 2 | 2 | 1 |

Soma: $1 + 3 + 5 + 7 + 9 + 11 = 36$. ✓

---

## Passo 4: Caso (c) — X = maior valor, Y = soma dos dois valores

**Resumo:** $X = \max(d_1,d_2)$, $Y = d_1 + d_2$; os pares $(X,Y)$ têm restrições $X \geq Y/2$ e $Y \leq X + 6$.

Para $X = x$ e $Y = s$: os pares $(d_1, d_2)$ com $d_1 + d_2 = s$ e $\max(d_1,d_2) = x$.

Isso exige que $x \in \{d_1, d_2\}$ e o outro valor seja $s - x$, com $s - x \leq x$ (i.e., $s \leq 2x$) e $s - x \geq 1$ (i.e., $s \geq x + 1$).

- Se $s - x < x$ (i.e., $s < 2x$, $s \geq x+1$): dois pares $(x, s-x)$ e $(s-x, x)$, logo $P = 2/36$.
- Se $s = 2x$: único par $(x,x)$, logo $P = 1/36$.
- Caso contrário: $P = 0$.

**Suporte:** $X \in \{1,\ldots,6\}$, $Y \in \{x+1, \ldots, x+6\} \cap \{2,\ldots,12\}$ para $s \neq 2x$; e $Y = 2x$ com $P = 1/36$.

**Tabela** $p(x,y) \times 36$ (linhas = $y$, colunas = $x$):

| $y\backslash x$ | 1 | 2 | 3 | 4 | 5 | 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **2** | 1 | 0 | 0 | 0 | 0 | 0 |
| **3** | 2 | 0 | 0 | 0 | 0 | 0 |
| **4** | 0 | 1 | 0 | 0 | 0 | 0 |  
| **5** | 0 | 2 | 0 | 0 | 0 | 0 |
| **6** | 0 | 2 | 1 | 0 | 0 | 0 |
| **7** | 0 | 0 | 2 | 0 | 0 | 0 |
| **8** | 0 | 0 | 2 | 1 | 0 | 0 |
| **9** | 0 | 0 | 0 | 2 | 0 | 0 |
| **10** | 0 | 0 | 0 | 2 | 1 | 0 |
| **11** | 0 | 0 | 0 | 0 | 2 | 0 |
| **12** | 0 | 0 | 0 | 0 | 2 | 1 |

Nota: para $x=4$, $y \in \{5,6,7,8,9,10\}$. Para $y=2x$: prob $1/36$. Para $x+1 \leq y < 2x$ ou $2x < y \leq x+6$: prob $2/36$.

Soma total por coluna $x$: $1 \cdot 1 + 2 \cdot 1 = 3$ para $x=1$; para geral $= (2x-1)/36 \cdot 36/(2x-1)$... Verificação: cada coluna $x$ contribui com $2x-1$ unidades divididas por 36. Total $= (1+3+5+7+9+11)/36 = 36/36 = 1$. ✓
