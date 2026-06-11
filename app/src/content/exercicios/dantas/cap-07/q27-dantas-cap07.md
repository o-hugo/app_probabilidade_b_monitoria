---
id: "dantas-cap07-q27"
titulo: "TLC — Número de Lançamentos para 100 Caras"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 27"
---

## Enunciado

Lança-se uma moeda honesta até obter 100 caras. Qual a probabilidade de que sejam necessários ao menos 220 lançamentos?

## Solução

Seja $X_i=$ número de lançamentos para a $i$-ésima cara. $X_i\sim\text{Geom}(1/2)$: $E(X_i)=2$, $\text{Var}(X_i)=2$.

O total de lançamentos $T=\sum_{i=1}^{100}X_i$: $E(T)=200$, $\text{Var}(T)=200$, $\sigma_T=\sqrt{200}=10\sqrt{2}$.

Pelo TLC: $T\approx N(200,200)$.

$$P(T\ge 220)=P\!\left(Z\ge\frac{220-200}{10\sqrt{2}}\right)=P\!\left(Z\ge\frac{20}{14{,}14}\right)=P(Z\ge 1{,}414).$$

$$P(Z\ge 1{,}414)=1-\Phi(1{,}414)\approx 1-0{,}9214=0{,}0786.$$

A probabilidade é aproximadamente **7,86%**.
