---
id: "dantas-cap07-q30"
titulo: "TLC — Sistema de 100 Componentes, Falha com p=1/10"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade", "confiabilidade"]
referencia: "Dantas, Cap. 7, Q. 30"
---

## Enunciado

100 componentes independentes, $P(\text{falha})=1/10$. O sistema funciona se ao menos 85 componentes funcionam. Calcule a probabilidade de que o sistema funcione.

## Solução

$F=$ número de falhas $\sim\text{Bin}(100;0{,}1)$. Sistema funciona se $F\le 15$.

$E(F)=10$, $\text{Var}(F)=9$, $\sigma=3$.

Pelo TLC: $F\approx N(10;9)$.

$$P(F\le 15)=P\!\left(Z\le\frac{15-10}{3}\right)=P(Z\le 1{,}667)=\Phi(1{,}67)\approx 0{,}9525.$$

A probabilidade de o sistema funcionar é aproximadamente **95,25%**.
