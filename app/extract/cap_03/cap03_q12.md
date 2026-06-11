---
id: "dantas-cap03-q12"
titulo: "F^n(x) e 1-[1-F(x)]^n são f.d.a.'s (máximo e mínimo de i.i.d.'s)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "Ambas são f.d.a.'s válidas (máximo e mínimo de n v.a. i.i.d.)"
tags: ["fda", "confiabilidade"]
referencia: "Dantas, Cap. 3, Q. 12"
---

# Exercício 12

Seja $F(x)$ uma função de distribuição acumulada (f.d.a.). Mostre que:

**(a)** $G(x) = F^n(x)$ é uma f.d.a.

**(b)** $H(x) = 1 - [1-F(x)]^n$ é uma f.d.a.

**Dica:** Considere $X_1, X_2, \ldots, X_n$ variáveis aleatórias independentes e identicamente distribuídas (i.i.d.) com f.d.a. $F$. Defina $Y = \max\{X_1,\ldots,X_n\}$ e $Z = \min\{X_1,\ldots,X_n\}$.

---

## Solução

### Parte (a): $G(x) = F^n(x)$ é f.d.a.

Sejam $X_1, \ldots, X_n$ i.i.d. com f.d.a. $F$ e seja $Y = \max\{X_1, \ldots, X_n\}$.

Calculemos a f.d.a. de $Y$:

$$F_Y(x) = P(Y \leq x) = P(\max\{X_1,\ldots,X_n\} \leq x) = P(X_1 \leq x, X_2 \leq x, \ldots, X_n \leq x).$$

Pela independência:

$$F_Y(x) = \prod_{i=1}^n P(X_i \leq x) = \prod_{i=1}^n F(x) = F^n(x) = G(x).$$

Como $G(x) = F_Y(x)$ é a f.d.a. de uma v.a. bem definida ($Y$), $G$ é uma f.d.a. $\square$

**Verificação direta das propriedades:**

1. **Monotonicidade:** $F$ não-decrescente $\Rightarrow$ $F^n$ não-decrescente (produto de funções não-decrescentes em $[0,1]$).
2. **Limites:** $\lim_{x\to-\infty} G(x) = 0^n = 0$ e $\lim_{x\to+\infty} G(x) = 1^n = 1$.
3. **Continuidade à direita:** $F$ contínua à direita $\Rightarrow$ $F^n$ contínua à direita.

---

### Parte (b): $H(x) = 1 - [1-F(x)]^n$ é f.d.a.

Seja $Z = \min\{X_1, \ldots, X_n\}$ com as mesmas $X_i$ i.i.d.

$$F_Z(x) = P(Z \leq x) = 1 - P(Z > x) = 1 - P(\min\{X_1,\ldots,X_n\} > x).$$

O mínimo é maior que $x$ se e somente se todos os $X_i$ são maiores que $x$:

$$P(Z > x) = P(X_1 > x, \ldots, X_n > x) = \prod_{i=1}^n P(X_i > x) = [1-F(x)]^n.$$

Portanto:

$$F_Z(x) = 1 - [1-F(x)]^n = H(x).$$

Como $H(x) = F_Z(x)$ é a f.d.a. de uma v.a. bem definida ($Z$), $H$ é uma f.d.a. $\square$

**Verificação direta das propriedades:**

1. **Monotonicidade:** $F$ não-decrescente $\Rightarrow$ $1-F$ não-crescente $\Rightarrow$ $[1-F]^n$ não-crescente $\Rightarrow$ $H = 1-[1-F]^n$ não-decrescente.
2. **Limites:** $\lim_{x\to-\infty} H(x) = 1 - 1^n = 0$ e $\lim_{x\to+\infty} H(x) = 1 - 0^n = 1$.
3. **Continuidade à direita:** herdada de $F$.
