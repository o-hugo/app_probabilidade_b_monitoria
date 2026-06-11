---
id: "dantas-cap03-q37"
titulo: "Processo de Ramificação de Galton-Watson"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "variancia", "condicional"]
referencia: "Dantas, Cap. 3, Q. 37"
---

## Enunciado

Considere uma população onde cada indivíduo, independentemente dos demais, produz $J$ filhos com probabilidade $P_J$, $J = 0, 1, 2, \ldots$ Seja $X_n$ o número de indivíduos na $n$-ésima geração, com $X_0 = 1$. Sejam $\mu = \sum_{J=0}^{\infty} J P_J$ e $\sigma^2 = \sum_{J=0}^{\infty}(J - \mu)^2 P_J$.

**(a)** Mostre que $E[X_n] = \mu\, E[X_{n-1}]$.

**(b)** Conclua que $E[X_n] = \mu^n$.

**(c)** Mostre que $\text{Var}(X_n) = \sigma^2 \mu^{n-1} + \mu^2 \text{Var}(X_{n-1})$.

**(d)** Conclua que $\text{Var}(X_n) = \sigma^2 \mu^{n-1} \frac{\mu^n - 1}{\mu - 1}$ para $\mu \neq 1$, e $\text{Var}(X_n) = n\sigma^2$ para $\mu = 1$.

## Passo 1: Item (a) — $E[X_n]$ via condicionamento

Condicione em $X_{n-1} = k$. Dado $X_{n-1} = k$, $X_n$ é a soma de $k$ variáveis i.i.d. com média $\mu$:

$$E[X_n \mid X_{n-1} = k] = k\mu.$$

Portanto $E[X_n \mid X_{n-1}] = \mu X_{n-1}$. Pela lei das esperanças iteradas:

$$E[X_n] = E[E(X_n \mid X_{n-1})] = \mu\, E[X_{n-1}].$$

**Resumo:** $E[X_n] = \mu E[X_{n-1}]$ por condicionamento e linearidade.

## Passo 2: Item (b) — $E[X_n] = \mu^n$

Da recorrência em (a), com $E[X_0] = 1$:

$$E[X_n] = \mu E[X_{n-1}] = \mu^2 E[X_{n-2}] = \cdots = \mu^n E[X_0] = \mu^n.$$

**Resumo:** Iterando a recorrência: $E[X_n] = \mu^n$.

## Passo 3: Item (c) — $\text{Var}(X_n)$

Pela lei da variância total: $\text{Var}(X_n) = E[\text{Var}(X_n \mid X_{n-1})] + \text{Var}[E(X_n \mid X_{n-1})]$.

Dado $X_{n-1} = k$: $\text{Var}(X_n \mid X_{n-1} = k) = k\sigma^2$ (soma de $k$ i.i.d. com variância $\sigma^2$).

Logo $\text{Var}(X_n \mid X_{n-1}) = \sigma^2 X_{n-1}$, então $E[\text{Var}(X_n \mid X_{n-1})] = \sigma^2 E[X_{n-1}] = \sigma^2 \mu^{n-1}$.

Também: $\text{Var}[E(X_n \mid X_{n-1})] = \text{Var}[\mu X_{n-1}] = \mu^2 \text{Var}(X_{n-1})$.

Portanto:

$$\text{Var}(X_n) = \sigma^2 \mu^{n-1} + \mu^2 \text{Var}(X_{n-1}).$$

**Resumo:** Lei da variância total dá a recorrência para $\text{Var}(X_n)$.

## Passo 4: Item (d) — Fórmula fechada

Com $\text{Var}(X_0) = 0$ e a recorrência $V_n = \sigma^2 \mu^{n-1} + \mu^2 V_{n-1}$:

**Caso $\mu \neq 1$:** A recorrência tem solução particular $V_n^* = C\mu^n$. Substituindo: $C\mu^n = \sigma^2 \mu^{n-1} + \mu^2 C\mu^{n-1}$, portanto $C = \sigma^2/(\mu - \mu^2)\cdot\mu = \sigma^2/({\mu(1-\mu)})$... Mais diretamente, iterando:

$$V_n = \sigma^2 \sum_{k=0}^{n-1} \mu^{n-1+k} \cdot \mu^{-(k)} = \sigma^2 \mu^{n-1} \sum_{k=0}^{n-1} \mu^k = \sigma^2 \mu^{n-1} \frac{\mu^n - 1}{\mu - 1}.$$

**Caso $\mu = 1$:** $V_n = \sigma^2 + V_{n-1}$, iterando com $V_0 = 0$ dá $V_n = n\sigma^2$.

**Resumo:** $\text{Var}(X_n) = \sigma^2 \mu^{n-1}\frac{\mu^n-1}{\mu-1}$ ($\mu \neq 1$); $\text{Var}(X_n) = n\sigma^2$ ($\mu = 1$).
