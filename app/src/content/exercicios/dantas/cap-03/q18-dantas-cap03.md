---
id: "dantas-cap03-q18"
titulo: "E[S²]=σ² e Cov(Xi-Xbar, Xbar)=0 para amostra aleatória simples"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
resposta_final: "Cov(Xi-Xbar, Xbar)=0 e E[S²]=σ²"
tags: ["variancia", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 18"
---

# Exercício 18

Seja $X_1, X_2, \ldots, X_n$ uma amostra aleatória simples (v.a.'s i.i.d.) com $E[X_i] = \mu$ e $\text{Var}(X_i) = \sigma^2$. Defina:

$$\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i, \qquad S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2.$$

Mostre: **(a)** $\text{Cov}(X_i - \bar{X},\; \bar{X}) = 0$. **(b)** $E[S^2] = \sigma^2$.

---

## Passo 1: Covariâncias úteis

**Resumo:** Como as $X_i$ são i.i.d., $\text{Cov}(X_i, X_j) = 0$ para $i \neq j$ e $\text{Cov}(X_i, X_i) = \sigma^2$.

Calcula-se $\text{Cov}(X_i, \bar{X})$:

$$\text{Cov}(X_i, \bar{X}) = \text{Cov}\!\left(X_i, \frac{1}{n}\sum_{j=1}^n X_j\right) = \frac{1}{n}\sum_{j=1}^n \text{Cov}(X_i, X_j) = \frac{1}{n}\text{Var}(X_i) = \frac{\sigma^2}{n}.$$

Também: $\text{Var}(\bar{X}) = \frac{\sigma^2}{n}$.

---

## Passo 2: Parte (a) — $\text{Cov}(X_i - \bar{X}, \bar{X}) = 0$

**Resumo:** Usa-se bilinearidade para separar a covariância.

$$\text{Cov}(X_i - \bar{X},\; \bar{X}) = \text{Cov}(X_i, \bar{X}) - \text{Cov}(\bar{X}, \bar{X}) = \frac{\sigma^2}{n} - \text{Var}(\bar{X}) = \frac{\sigma^2}{n} - \frac{\sigma^2}{n} = 0. \quad \square$$

---

## Passo 3: Parte (b) — $E[S^2] = \sigma^2$

**Resumo:** Expande-se $(X_i - \bar{X})^2$ e calcula-se a esperança usando o truque da decomposição.

$$\sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n (X_i - \mu - (\bar{X} - \mu))^2$$

$$= \sum_{i=1}^n (X_i - \mu)^2 - 2(\bar{X}-\mu)\sum_{i=1}^n(X_i-\mu) + n(\bar{X}-\mu)^2.$$

Note que $\sum_{i=1}^n (X_i-\mu) = n(\bar{X}-\mu)$, logo:

$$\sum_{i=1}^n (X_i - \bar{X})^2 = \sum_{i=1}^n (X_i-\mu)^2 - n(\bar{X}-\mu)^2.$$

Tomando esperanças:

$$E\!\left[\sum_{i=1}^n (X_i-\bar{X})^2\right] = \sum_{i=1}^n E[(X_i-\mu)^2] - n\,E[(\bar{X}-\mu)^2]$$

$$= n\sigma^2 - n \cdot \frac{\sigma^2}{n} = n\sigma^2 - \sigma^2 = (n-1)\sigma^2.$$

Portanto:

$$E[S^2] = \frac{1}{n-1} \cdot (n-1)\sigma^2 = \sigma^2. \quad \square$$

> **Conclusão:** $S^2$ é um estimador **não-viesado** de $\sigma^2$. O fator $1/(n-1)$ (em vez de $1/n$) é exatamente o que garante a ausência de viés, como demonstrado.
