---
id: "dantas-cap07-q31"
titulo: "TLC — Tempo Total de 30 Dispositivos Exponenciais"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 31"
---

## Enunciado

30 dispositivos em série, cada um $\sim\text{Exp}(\beta=1/10)$. $T=$ tempo total. $P(T>350)$?

## Solução

$T=\sum_{i=1}^{30}X_i$, $X_i\sim\text{Exp}(1/10)$ i.i.d.: $E(X_i)=10$, $\text{Var}(X_i)=100$.

$E(T)=300$, $\text{Var}(T)=3000$, $\sigma_T=\sqrt{3000}=10\sqrt{30}\approx 54{,}77$.

Pelo TLC: $T\approx N(300;3000)$.

$$P(T>350)=P\!\left(Z>\frac{350-300}{54{,}77}\right)=P(Z>0{,}913)=1-\Phi(0{,}913)\approx 1-0{,}8194=0{,}1806.$$

A probabilidade é aproximadamente **18,06%**.
