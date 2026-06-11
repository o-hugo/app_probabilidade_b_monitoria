---
id: "dantas-cap07-q23"
titulo: "TLC — Média Amostral de Lâmpadas Exponenciais"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 23"
---

## Enunciado

Duração de lâmpada $\sim\text{Exp}(1/3)$. Amostra de $n=36$. Qual a probabilidade de que a média amostral seja inferior a 2 horas?

## Solução

$X_i\sim\text{Exp}(1/3)$: $E(X_i)=3$, $\text{Var}(X_i)=9$.

$\bar{X}_{36}$: $E(\bar{X})=3$, $\text{Var}(\bar{X})=9/36=1/4$, $\sigma_{\bar{X}}=1/2$.

Pelo TLC: $\bar{X}_{36}\approx N(3;1/4)$.

$$P(\bar{X}<2)=P\!\left(Z<\frac{2-3}{1/2}\right)=P(Z<-2)=1-\Phi(2)\approx 0{,}0228.$$

A probabilidade é aproximadamente **2,28%**.
