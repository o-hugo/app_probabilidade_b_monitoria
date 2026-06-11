---
id: "dantas-cap03-q09"
titulo: "Covariância e independência de indicadoras definidas em dado"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Cov(X,Y) = 1/12; X e Y não são independentes"
tags: ["esperanca", "variancia", "probabilidade"]
referencia: "Dantas, Cap. 3, Q. 9"
---

# Exercício 9

Um dado honesto é lançado uma vez. Definem-se as variáveis aleatórias:

- $X = 1$ se o resultado for $\geq 3$; $X = 0$ caso contrário.
- $Y = 1$ se o resultado for par; $Y = 0$ caso contrário.

**(a)** Calcule $\text{Cov}(X, Y)$.

**(b)** $X$ e $Y$ são independentes?

---

## Passo 1: Distribuição conjunta de $(X, Y)$

**Resumo:** Cada face do dado tem probabilidade $1/6$; classifica-se cada face segundo $(X, Y)$.

| Face | $X$ | $Y$ | $P$ |
|:---:|:---:|:---:|:---:|
| 1 | 0 | 0 | 1/6 |
| 2 | 0 | 1 | 1/6 |
| 3 | 1 | 0 | 1/6 |
| 4 | 1 | 1 | 1/6 |
| 5 | 1 | 0 | 1/6 |
| 6 | 1 | 1 | 1/6 |

Distribuição conjunta:

$$p(0,0) = \frac{1}{6},\quad p(0,1) = \frac{1}{6},\quad p(1,0) = \frac{2}{6},\quad p(1,1) = \frac{2}{6}.$$

---

## Passo 2: Marginais e esperanças

**Resumo:** As marginais somam linhas/colunas da tabela conjunta.

$$p_X(0) = \frac{2}{6} = \frac{1}{3}, \quad p_X(1) = \frac{4}{6} = \frac{2}{3} \implies E[X] = \frac{2}{3}.$$

$$p_Y(0) = \frac{3}{6} = \frac{1}{2}, \quad p_Y(1) = \frac{3}{6} = \frac{1}{2} \implies E[Y] = \frac{1}{2}.$$

---

## Passo 3: $E[XY]$ e covariância

**Resumo:** $XY \neq 0$ apenas quando $X=1$ e $Y=1$.

$$E[XY] = 1 \cdot 1 \cdot p(1,1) = \frac{2}{6} = \frac{1}{3}.$$

$$\text{Cov}(X,Y) = E[XY] - E[X]E[Y] = \frac{1}{3} - \frac{2}{3} \cdot \frac{1}{2} = \frac{1}{3} - \frac{1}{3} = 0.$$

$$\boxed{\text{Cov}(X,Y) = 0}$$

---

## Passo 4: Independência

**Resumo:** Apesar da covariância nula, verifica-se a igualdade $p(x,y) = p_X(x)p_Y(y)$ para todos os pares.

Verifique $(0,0)$:

$$p_X(0) \cdot p_Y(0) = \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{6} = p(0,0). \checkmark$$

Verifique $(0,1)$:

$$p_X(0) \cdot p_Y(1) = \frac{1}{3} \cdot \frac{1}{2} = \frac{1}{6} = p(0,1). \checkmark$$

Verifique $(1,0)$:

$$p_X(1) \cdot p_Y(0) = \frac{2}{3} \cdot \frac{1}{2} = \frac{1}{3} = p(1,0). \checkmark$$

Verifique $(1,1)$:

$$p_X(1) \cdot p_Y(1) = \frac{2}{3} \cdot \frac{1}{2} = \frac{1}{3} = p(1,1). \checkmark$$

Como $p(x,y) = p_X(x) p_Y(y)$ para todos os pares, **$X$ e $Y$ são independentes**.

> **Observação:** Este exemplo ilustra que independência implica covariância nula, mas a recíproca **não** vale em geral. Aqui, por coincidência, as variáveis são de fato independentes e a covariância é zero.
