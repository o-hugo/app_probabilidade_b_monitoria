---
id: "dantas-cap05-q12"
titulo: "Chuva Anual Normal — Tempo Até Registro Excepcional"
topicos: ["04-distribuicao-normal"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "padronizacao-z"]
referencia: "Dantas, Cap. 5, Q. 12"
---

## Enunciado

Chuva anual $\sim N(\mu=40, \sigma=4)$. Qual a probabilidade de que sejam necessários mais de 10 anos para registrar uma chuva anual maior que 50? Suposições?

## Passo 1: Probabilidade em um ano

$$p = P(X > 50) = P\!\left(Z > \frac{50-40}{4}\right) = P(Z > 2{,}5) = 1 - \Phi(2{,}5) \approx 0{,}0062.$$

**Resumo:** $p \approx 0{,}0062$ por ano.

## Passo 2: Tempo até o primeiro ano com chuva > 50

Suposição: anos independentes com mesma distribuição. Seja $T$ = número de anos até o primeiro com $X > 50$. $T \sim \text{Geom}(p)$ (número de tentativas até primeiro sucesso).

$$P(T > 10) = (1-p)^{10} \approx (0{,}9938)^{10} \approx 0{,}940.$$

**Resumo:** Há 94% de probabilidade de esperar mais de 10 anos para registrar chuva acima de 50. Suposição: anos independentes e identicamente distribuídos.
