---
id: "dantas-cap07-q34"
titulo: "TLC — Soma de 20 Voltagens Uniformes (0,10)"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 34"
---

## Enunciado

$V_i\sim U(0,10)$ i.i.d., $n=20$. $V=\sum_{i=1}^{20}V_i$. Determine $P(V>105)$.

## Solução

$E(V_i)=5$, $\text{Var}(V_i)=100/12=25/3$.

$E(V)=100$, $\text{Var}(V)=20\cdot 25/3=500/3\approx 166{,}67$, $\sigma_V\approx 12{,}91$.

Pelo TLC: $V\approx N(100;500/3)$.

$$P(V>105)=P\!\left(Z>\frac{105-100}{\sqrt{500/3}}\right)=P\!\left(Z>\frac{5}{12{,}91}\right)=P(Z>0{,}387).$$

$$P(Z>0{,}387)=1-\Phi(0{,}387)\approx 1-0{,}6508=0{,}3492.$$

A probabilidade é aproximadamente **34,9%**.
