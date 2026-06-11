---
id: "dantas-cap03-q07"
titulo: "Probabilidades e independência a partir de distribuição conjunta dada"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "X e Y não são independentes"
tags: ["probabilidade", "fdp-valida", "condicional"]
referencia: "Dantas, Cap. 3, Q. 7"
---

# Exercício 7

A distribuição conjunta de $(X, Y)$ é dada por:

| $p(x,y)$ | $Y=1$ | $Y=2$ |
|:---:|:---:|:---:|
| $X=1$ | $1/8$ | $1/4$ |
| $X=2$ | $1/8$ | $1/2$ |

**(a)** Calcule $P(XY \leq 3)$, $P(X+Y > 2)$ e $P(X=1 \mid Y > 1)$.

**(b)** $X$ e $Y$ são independentes?

---

## Passo 1: Verificação e marginais

**Resumo:** A soma total é $1/8+1/4+1/8+1/2 = 1$, confirmando validade. Calculam-se as marginais.

$$p_X(1) = \frac{1}{8} + \frac{1}{4} = \frac{3}{8}, \qquad p_X(2) = \frac{1}{8} + \frac{1}{2} = \frac{5}{8}.$$

$$p_Y(1) = \frac{1}{8} + \frac{1}{8} = \frac{1}{4}, \qquad p_Y(2) = \frac{1}{4} + \frac{1}{2} = \frac{3}{4}.$$

---

## Passo 2: $P(XY \leq 3)$

**Resumo:** Lista-se cada par e o produto $xy$; excluem-se os pares onde $xy > 3$.

Os pares possíveis e seus produtos:

| $(x,y)$ | $xy$ | $xy \leq 3$? |
|:---:|:---:|:---:|
| $(1,1)$ | $1$ | Sim |
| $(1,2)$ | $2$ | Sim |
| $(2,1)$ | $2$ | Sim |
| $(2,2)$ | $4$ | **Não** |

$$P(XY \leq 3) = p(1,1) + p(1,2) + p(2,1) = \frac{1}{8} + \frac{1}{4} + \frac{1}{8} = \frac{4}{8} = \frac{1}{2}.$$

---

## Passo 3: $P(X+Y > 2)$

**Resumo:** Exclui-se o único par com $x+y \leq 2$, que é $(1,1)$ com $x+y=2$.

$$P(X+Y > 2) = 1 - P(X+Y \leq 2) = 1 - p(1,1) = 1 - \frac{1}{8} = \frac{7}{8}.$$

---

## Passo 4: $P(X=1 \mid Y > 1)$

**Resumo:** $Y > 1$ equivale a $Y = 2$; aplica-se a definição de probabilidade condicional.

$$P(X=1 \mid Y > 1) = P(X=1 \mid Y=2) = \frac{p(1,2)}{p_Y(2)} = \frac{1/4}{3/4} = \frac{1}{3}.$$

---

## Passo 5: Independência de $X$ e $Y$

**Resumo:** Verifica-se se $p(x,y) = p_X(x)\cdot p_Y(y)$ para todos os pares.

Para $(x,y)=(1,1)$:

$$p_X(1)\cdot p_Y(1) = \frac{3}{8} \cdot \frac{1}{4} = \frac{3}{32} \neq \frac{1}{8} = \frac{4}{32}.$$

Como a condição falha, **$X$ e $Y$ não são independentes**.
