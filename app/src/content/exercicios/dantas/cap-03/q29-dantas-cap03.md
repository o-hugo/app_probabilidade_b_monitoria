---
id: "dantas-cap03-q29"
titulo: "Quantia total esperada gasta na loja (esperança de soma aleatória)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "E(S) = R$ 2500"
tags: ["esperanca"]
referencia: "Dantas, Cap. 3, Q. 29"
---

## Enunciado

O número $N$ de pessoas que entram em uma loja tem média $E(N) = 50$. A quantia gasta por cada pessoa é uma variável aleatória independente $C_i$ com média $E(C_i) = 50$ reais. A quantia gasta por cada consumidor é independente do número de pessoas. Qual a quantia esperada total gasta no dia?

## Solução

Seja $S = C_1 + C_2 + \cdots + C_N$ a quantia total gasta, onde $N$ é aleatório.

Pela **lei da esperança total** (fórmula de Wald):

$$E(S) = E\!\left[\sum_{i=1}^N C_i\right] = E\!\left[E\!\left(\sum_{i=1}^N C_i \;\Big|\; N\right)\right].$$

Dado $N = n$, a soma $\sum_{i=1}^n C_i$ tem esperança $n \cdot E(C_i) = 50n$ (pois os $C_i$ são i.i.d. com média 50 e independentes de $N$). Portanto:

$$E(S \mid N = n) = 50n \implies E(S \mid N) = 50N.$$

Tomando esperança:

$$E(S) = E[50N] = 50 \cdot E(N) = 50 \times 50 = 2500.$$

$$\boxed{E(S) = \text{R\$ } 2500}$$

**Observação (Fórmula de Wald):** Em geral, se $C_1, C_2, \ldots$ são i.i.d. com média $\mu$ e $N$ é v.a. inteira não-negativa independente dos $C_i$, então $E\!\left[\sum_{i=1}^N C_i\right] = \mu \cdot E(N)$.
