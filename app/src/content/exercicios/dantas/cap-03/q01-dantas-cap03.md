---
id: "dantas-cap03-q01"
titulo: "Distribuição conjunta de bolas coloridas retiradas de urna"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Tabela conjunta de (X,Y) com X+Y ≤ 3; P(X=Y) = 12/55"
tags: ["probabilidade", "fdp-valida"]
referencia: "Dantas, Cap. 3, Q. 1"
---

# Distribuição conjunta de bolas coloridas retiradas de urna

## Enunciado

Uma urna contém 3 bolas vermelhas, 4 brancas e 5 azuis. Selecionam-se 3 bolas ao acaso (sem reposição). Seja $X$ o número de bolas vermelhas e $Y$ o número de bolas brancas selecionadas.

**(a)** Determine a distribuição conjunta de $(X, Y)$.

**(b)** Determine as distribuições marginais de $X$ e de $Y$.

**(c)** Calcule $P(X = Y)$.

---

## Passo 1: Espaço de valores e fórmula geral

**Resumo:** Identifica o suporte e a fórmula hipergeométrica multivariada.

O número total de bolas é $N = 3 + 4 + 5 = 12$. Retiramos $n = 3$ bolas. O número de azuis selecionadas é $Z = 3 - X - Y$.

Os valores possíveis são $x \in \{0,1,2,3\}$, $y \in \{0,1,2,3\}$ com $x + y \leq 3$.

A distribuição hipergeométrica multivariada dá:

$$p(x, y) = P(X = x, Y = y) = \frac{\binom{3}{x}\binom{4}{y}\binom{5}{3-x-y}}{\binom{12}{3}}, \quad x + y \leq 3,\ x,y \geq 0.$$

O denominador é $\binom{12}{3} = 220$.

---

## Passo 2: Calcular todas as probabilidades conjuntas

**Resumo:** Preenche a tabela com os valores de $p(x,y)$.

Calculando cada célula:

| $y \backslash x$ | 0 | 1 | 2 | 3 |
|:---:|:---:|:---:|:---:|:---:|
| **0** | $\frac{\binom{3}{0}\binom{4}{0}\binom{5}{3}}{220} = \frac{10}{220}$ | $\frac{\binom{3}{1}\binom{4}{0}\binom{5}{2}}{220} = \frac{30}{220}$ | $\frac{\binom{3}{2}\binom{4}{0}\binom{5}{1}}{220} = \frac{15}{220}$ | $\frac{\binom{3}{3}\binom{4}{0}\binom{5}{0}}{220} = \frac{1}{220}$ |
| **1** | $\frac{\binom{3}{0}\binom{4}{1}\binom{5}{2}}{220} = \frac{40}{220}$ | $\frac{\binom{3}{1}\binom{4}{1}\binom{5}{1}}{220} = \frac{60}{220}$ | $\frac{\binom{3}{2}\binom{4}{1}\binom{5}{0}}{220} = \frac{12}{220}$ | 0 |
| **2** | $\frac{\binom{3}{0}\binom{4}{2}\binom{5}{1}}{220} = \frac{30}{220}$ | $\frac{\binom{3}{1}\binom{4}{2}\binom{5}{0}}{220} = \frac{18}{220}$ | 0 | 0 |
| **3** | $\frac{\binom{3}{0}\binom{4}{3}\binom{5}{0}}{220} = \frac{4}{220}$ | 0 | 0 | 0 |

Verificação: $10+30+15+1+40+60+12+30+18+4 = 220$. ✓

---

## Passo 3: Marginais de X e Y

**Resumo:** Soma as linhas/colunas da tabela conjunta.

**Marginal de $X$** (soma nas linhas de $y$):

$$P(X=0) = \frac{10+40+30+4}{220} = \frac{84}{220}, \quad P(X=1) = \frac{30+60+18}{220} = \frac{108}{220}$$

$$P(X=2) = \frac{15+12}{220} = \frac{27}{220}, \quad P(X=3) = \frac{1}{220}$$

Verificação: $84+108+27+1 = 220$. ✓

Equivalentemente, $X \sim \text{Hipergeométrica}(N=12, K=3, n=3)$, então $P(X=x) = \dfrac{\binom{3}{x}\binom{9}{3-x}}{\binom{12}{3}}$.

**Marginal de $Y$** (soma nas colunas de $x$):

$$P(Y=0) = \frac{10+30+15+1}{220} = \frac{56}{220}, \quad P(Y=1) = \frac{40+60+12}{220} = \frac{112}{220}$$

$$P(Y=2) = \frac{30+18}{220} = \frac{48}{220}, \quad P(Y=3) = \frac{4}{220}$$

Verificação: $56+112+48+4 = 220$. ✓

Equivalentemente, $Y \sim \text{Hipergeométrica}(N=12, K=4, n=3)$.

---

## Passo 4: Calcular P(X = Y)

**Resumo:** Soma as probabilidades conjuntas ao longo da diagonal $x = y$.

$$P(X = Y) = p(0,0) + p(1,1) + p(2,2) + p(3,3)$$

$$= \frac{10}{220} + \frac{60}{220} + 0 + 0 = \frac{70}{220} = \frac{7}{22} \approx 0{,}318.$$

Nota: $p(2,2)$ e $p(3,3)$ são zero pois exigiriam $x + y > 3$.
