---
id: "dantas-cap03-q23"
titulo: "Distribuição multinomial: esperança, variância e covariância"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "variancia", "probabilidade"]
referencia: "Dantas, Cap. 3, Q. 23"
---

## Enunciado

Considere $n$ experimentos independentes, cada um com $r$ resultados possíveis com probabilidades $p_1, p_2, \ldots, p_r$ (com $\sum_{i=1}^r p_i = 1$). Seja $X_i$ o número de resultados do tipo $i$ nos $n$ experimentos. A distribuição conjunta é a **multinomial**:

$$P(X_1 = n_1, \ldots, X_r = n_r) = \frac{n!}{n_1! \cdots n_r!} p_1^{n_1} \cdots p_r^{n_r}, \quad \sum_{i=1}^r n_i = n.$$

Usando variáveis indicadoras $I_i(k) = \mathbf{1}[\text{experimento } k \text{ produz resultado do tipo } i]$, determine:

**(a)** $E(X_i)$

**(b)** $\text{Var}(X_i)$

**(c)** $\text{Cov}(X_i, X_j)$ para $i \neq j$

## Passo 1: Definição das variáveis indicadoras

**Resumo:** Escreve $X_i$ como soma de indicadores independentes para aplicar esperança e variância linearmente.

Para cada experimento $k = 1, \ldots, n$, defina:

$$I_i(k) = \begin{cases} 1 & \text{se o experimento } k \text{ produz resultado do tipo } i \\ 0 & \text{caso contrário} \end{cases}$$

Então $X_i = \sum_{k=1}^n I_i(k)$. Cada $I_i(k)$ é Bernoulli$(p_i)$, portanto:

$$E[I_i(k)] = p_i, \quad \text{Var}[I_i(k)] = p_i(1-p_i).$$

Para $i \neq j$: $E[I_i(k) \cdot I_j(k)] = 0$ pois um experimento não pode produzir resultado $i$ e $j$ simultaneamente.

## Passo 2: Cálculo de $E(X_i)$

**Resumo:** Pela linearidade da esperança, $E(X_i) = np_i$.

$$E(X_i) = E\!\left[\sum_{k=1}^n I_i(k)\right] = \sum_{k=1}^n E[I_i(k)] = np_i.$$

$$\boxed{E(X_i) = n p_i}$$

## Passo 3: Cálculo de $\text{Var}(X_i)$

**Resumo:** Como os $I_i(k)$ são independentes entre experimentos, $\text{Var}(X_i) = np_i(1-p_i)$.

Os indicadores $I_i(1), \ldots, I_i(n)$ são independentes (experimentos independentes), logo:

$$\text{Var}(X_i) = \sum_{k=1}^n \text{Var}[I_i(k)] = np_i(1-p_i).$$

$$\boxed{\text{Var}(X_i) = n p_i (1 - p_i)}$$

## Passo 4: Cálculo de $\text{Cov}(X_i, X_j)$ para $i \neq j$

**Resumo:** A covariância resulta $-np_ip_j$, negativa por conta da restrição $\sum X_i = n$.

$$\text{Cov}(X_i, X_j) = \sum_{k=1}^n \sum_{l=1}^n \text{Cov}(I_i(k), I_j(l)).$$

- Para $k \neq l$: independência implica $\text{Cov}(I_i(k), I_j(l)) = 0$.
- Para $k = l$: $\text{Cov}(I_i(k), I_j(k)) = E[I_i(k)I_j(k)] - p_ip_j = 0 - p_ip_j = -p_ip_j$.

Portanto:

$$\text{Cov}(X_i, X_j) = \sum_{k=1}^n (-p_ip_j) = -np_ip_j.$$

$$\boxed{\text{Cov}(X_i, X_j) = -n p_i p_j \quad (i \neq j)}$$
