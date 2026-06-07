---
id: "lista02-q05-aproximao-normal-da-binomial"
titulo: "Aproximação Normal da Binomial"
topicos: ["distribuicao-normal"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["tlc", "padronizacao-z"]
---

## Enunciado

Em 40 lançamentos de moeda honesta, calcule P(X=20) usando a aproximação Normal e compare com o resultado Binomial exato.

## Solução

Seja X o número de caras, $X \sim B(n=40, p=0.5)$.

## 1. Cálculo Exato (Binomial)

$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$<br>$P(X=20) = \binom{40}{20} (0.5)^{20} (0.5)^{20} \approx 0.1254$

## 2. Aproximação Normal

**Condições:** $np = 40(0.5)=20 \ge 5$ e $n(1-p)=20 \ge 5$. A aproximação é válida.<br>**Parâmetros:** Média $\mu = np = 20$. Variância $\sigma^2 = np(1-p) = 10 \implies \sigma \approx 3.162$.<br>**Correção de Continuidade:** Para $P(X=k)$, aproximamos por $P(k-0.5 < X_{norm} < k+0.5)$.<br>$P(19.5 < X < 20.5) = P(\frac{19.5-20}{3.162} < Z < \frac{20.5-20}{3.162}) = P(-0.16 < Z < 0.16)$<br>$= \Phi(0.16) - \Phi(-0.16) = 2\Phi(0.16) - 1 \approx 2(0.5636) - 1 = 0.1272$<br>O valor é muito próximo do exato.
