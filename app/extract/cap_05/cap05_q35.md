---
id: "dantas-cap05-q35"
titulo: "Distribuição do Alcance Balístico R = A·sen(θ)"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["metodo-fda", "fdp-valida"]
referencia: "Dantas, Cap. 5, Q. 35"
---

## Enunciado

$\theta \sim U(-\pi/2, \pi/2)$. $R = A\sin\theta$, $A$ constante fixada. Determine a distribuição de $R$.

## Passo 1: Suporte de R

$-A \le R = A\sin\theta \le A$ (pois $|\sin\theta| \le 1$).

**Resumo:** $R \in (-A, A)$.

## Passo 2: FDA de R

Para $-A < r < A$:

$$F_R(r) = P(R \le r) = P(A\sin\theta \le r) = P\!\left(\sin\theta \le \frac{r}{A}\right) = P\!\left(\theta \le \arcsin\frac{r}{A}\right).$$

Como $\theta \sim U(-\pi/2, \pi/2)$ com densidade $1/\pi$:

$$F_R(r) = \frac{\arcsin(r/A) + \pi/2}{\pi}.$$

## Passo 3: Densidade de R

$$f_R(r) = \frac{d}{dr}F_R(r) = \frac{1}{\pi} \cdot \frac{1/A}{\sqrt{1-(r/A)^2}} = \frac{1}{\pi\sqrt{A^2 - r^2}}, \quad -A < r < A.$$

Esta é a distribuição **arco-seno** (caso particular da distribuição beta com $\alpha=\beta=1/2$).
