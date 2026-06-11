---
id: "dantas-cap03-q22"
titulo: "Propriedades da função indicadora: esperança, produto e covariância"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "Cov(I_A, I_B) = P(A∩B) - P(A)P(B)"
tags: ["esperanca", "probabilidade", "variancia"]
referencia: "Dantas, Cap. 3, Q. 22"
---

# Exercício 22

Seja $I_A$ a função indicadora do evento $A$, definida por:

$$I_A(\omega) = \begin{cases} 1 & \text{se } \omega \in A, \\ 0 & \text{se } \omega \notin A. \end{cases}$$

Mostre:

**(a)** $E(I_A) = P(A)$

**(b)** $E(I_A \cdot I_B) = P(A \cap B)$

**(c)** $\text{Cov}(I_A, I_B) = P(A \cap B) - P(A)P(B)$

---

## Solução

### Parte (a): $E(I_A) = P(A)$

$I_A$ é uma variável de Bernoulli: assume o valor $1$ com probabilidade $P(A)$ e $0$ com probabilidade $1-P(A)$.

$$E(I_A) = 1 \cdot P(I_A = 1) + 0 \cdot P(I_A = 0) = P(A). \quad \square$$

---

### Parte (b): $E(I_A \cdot I_B) = P(A \cap B)$

Observe que o produto $I_A \cdot I_B$ é ele mesmo uma função indicadora:

$$I_A(\omega) \cdot I_B(\omega) = \begin{cases} 1 & \text{se } \omega \in A \text{ e } \omega \in B, \\ 0 & \text{caso contrário.} \end{cases} = I_{A \cap B}(\omega).$$

Logo, pela parte (a):

$$E(I_A \cdot I_B) = E(I_{A \cap B}) = P(A \cap B). \quad \square$$

---

### Parte (c): $\text{Cov}(I_A, I_B) = P(A \cap B) - P(A)P(B)$

Pela definição de covariância e pelas partes (a) e (b):

$$\text{Cov}(I_A, I_B) = E(I_A I_B) - E(I_A)E(I_B) = P(A \cap B) - P(A)P(B). \quad \square$$

> **Interpretações:**
>
> - $\text{Cov}(I_A, I_B) > 0 \iff P(A \cap B) > P(A)P(B) \iff$ $A$ e $B$ são **positivamente correlacionados** (ocorrência de um torna o outro mais provável).
> - $\text{Cov}(I_A, I_B) = 0 \iff P(A \cap B) = P(A)P(B) \iff$ $A$ e $B$ são **independentes**.
> - $\text{Cov}(I_A, I_B) < 0 \iff$ $A$ e $B$ são **negativamente correlacionados**.
>
> Este resultado conecta diretamente a noção probabilística de independência de eventos com a noção estatística de não-correlação de variáveis aleatórias.
