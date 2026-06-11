---
id: "dantas-cap03-q10"
titulo: "Covariância nula sem independência: distribuição 3×3"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Cov(X,Y) = 0; X e Y não são independentes"
tags: ["esperanca", "variancia"]
referencia: "Dantas, Cap. 3, Q. 10"
---

# Exercício 10

A distribuição conjunta de $(X, Y)$ é dada pela tabela abaixo (probabilidades não listadas são zero):

| $Y \backslash X$ | $-1$ | $0$ | $1$ |
|:---:|:---:|:---:|:---:|
| $-1$ | $0$ | $1/5$ | $0$ |
| $0$ | $1/5$ | $1/5$ | $1/5$ |
| $1$ | $0$ | $1/5$ | $0$ |

**(a)** Calcule $\text{Cov}(X, Y)$.

**(b)** $X$ e $Y$ são independentes?

---

## Passo 1: Marginais

**Resumo:** Somam-se linhas e colunas para obter as distribuições marginais.

$$p_X(-1) = \frac{1}{5}, \quad p_X(0) = \frac{3}{5}, \quad p_X(1) = \frac{1}{5}.$$

$$p_Y(-1) = \frac{1}{5}, \quad p_Y(0) = \frac{3}{5}, \quad p_Y(1) = \frac{1}{5}.$$

Por simetria das duas marginais:

$$E[X] = (-1)\cdot\frac{1}{5} + 0\cdot\frac{3}{5} + 1\cdot\frac{1}{5} = 0, \qquad E[Y] = 0.$$

---

## Passo 2: $E[XY]$ e covariância

**Resumo:** O produto $xy \neq 0$ apenas quando ambos $x \neq 0$ e $y \neq 0$, mas nesses pares a probabilidade é zero.

Apenas os pares com $p(x,y) > 0$ são: $(-1,0)$, $(0,-1)$, $(0,0)$, $(1,0)$, $(0,1)$. Em todos esses pares, $x=0$ ou $y=0$, portanto $xy = 0$.

$$E[XY] = \sum_{x,y} xy \cdot p(x,y) = 0.$$

$$\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = 0 - 0 \cdot 0 = 0.$$

$$\boxed{\text{Cov}(X,Y) = 0}$$

---

## Passo 3: Independência

**Resumo:** A igualdade $p(x,y) = p_X(x)p_Y(y)$ falha para o par $(-1,-1)$.

$$p_X(-1)\cdot p_Y(-1) = \frac{1}{5} \cdot \frac{1}{5} = \frac{1}{25} \neq 0 = p(-1,-1).$$

Portanto, **$X$ e $Y$ não são independentes**, apesar de $\text{Cov}(X,Y) = 0$.

> **Conclusão importante:** Covariância nula **não** implica independência. Este exemplo é um contraexemplo clássico: as variáveis são não-correlacionadas mas dependentes (há uma relação: $Y \neq 0$ implica $X = 0$).
