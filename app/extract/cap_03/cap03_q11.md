---
id: "dantas-cap03-q11"
titulo: "Distribuição conjunta de experimento em duas etapas com uniforme aninhada"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "X e Y não são independentes; marginal de Y: p_Y(y) = sum sobre x de 1/(11(2x+1))"
tags: ["probabilidade", "fdp-valida", "condicional"]
referencia: "Dantas, Cap. 3, Q. 11"
---

# Exercício 11

Um experimento em duas etapas:

1. $X$ é escolhido uniformemente em $\{0, 1, 2, \ldots, 10\}$.
2. Dado $X = x$, $Y$ é escolhido uniformemente em $\{-x, -x+1, \ldots, x\}$ (conjunto com $2x+1$ elementos).

**(a)** Determine a distribuição conjunta de $(X, Y)$.

**(b)** Determine a marginal de $Y$.

**(c)** $X$ e $Y$ são independentes?

---

## Passo 1: Distribuição conjunta

**Resumo:** Usa-se a regra de probabilidade condicional $p(x,y) = P(Y=y \mid X=x) \cdot P(X=x)$.

Para $x \in \{0,1,\ldots,10\}$ e $y \in \{-x,\ldots,x\}$:

$$P(X=x) = \frac{1}{11}, \qquad P(Y=y \mid X=x) = \frac{1}{2x+1}.$$

Portanto:

$$p(x,y) = P(X=x, Y=y) = \frac{1}{11} \cdot \frac{1}{2x+1} = \frac{1}{11(2x+1)},$$

para $x \in \{0,1,\ldots,10\}$ e $y \in \{-x,-x+1,\ldots,x\}$ (e $p(x,y)=0$ caso contrário).

**Caso especial $x=0$:** o único valor possível de $Y$ é $0$, com $p(0,0) = 1/11$.

---

## Passo 2: Marginal de $Y$

**Resumo:** Para cada valor fixo de $y$, soma-se sobre todos os $x$ compatíveis com esse $y$.

O valor $Y = y$ é possível quando $x \geq |y|$, pois $y \in \{-x,\ldots,x\}$ iff $|y| \leq x$. Logo:

$$p_Y(y) = \sum_{x=|y|}^{10} \frac{1}{11(2x+1)}, \qquad y \in \{-10,-9,\ldots,10\}.$$

Por simetria, $p_Y(y) = p_Y(-y)$. Alguns valores explícitos:

$$p_Y(0) = \sum_{x=0}^{10} \frac{1}{11(2x+1)} = \frac{1}{11}\left(1 + \frac{1}{3} + \frac{1}{5} + \cdots + \frac{1}{21}\right).$$

$$p_Y(\pm 10) = \frac{1}{11 \cdot 21} = \frac{1}{231}.$$

---

## Passo 3: Independência

**Resumo:** $X$ e $Y$ não são independentes porque o suporte de $Y$ depende de $X$.

Para que $X$ e $Y$ fossem independentes, seria necessário que $p_Y(y)$ não dependesse do valor de $X$. Mas o suporte de $Y$ (os valores que $Y$ pode assumir) depende diretamente de $X$: se $X=0$, então $Y$ só pode ser $0$; se $X=5$, então $Y \in \{-5,\ldots,5\}$.

Formalmente, $p(0, 1) = 0$ mas $p_X(0) = 1/11 > 0$ e $p_Y(1) > 0$, logo $p(0,1) \neq p_X(0) p_Y(1)$.

Portanto, **$X$ e $Y$ não são independentes**.
