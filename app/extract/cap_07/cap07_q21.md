---
id: "dantas-cap07-q21"
titulo: "Bernoulli com p=1/n — Limite em Probabilidade"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 7, Q. 21"
---

## Enunciado

$X_n$ independentes com $P(X_n=1)=1/n$ e $P(X_n=0)=1-1/n$. Ache o limite em probabilidade de $X_n$.

## Solução

$E(X_n)=1/n\to 0$ e $\text{Var}(X_n)=\frac{1}{n}(1-\frac{1}{n})\to 0$.

Pelo exercício Q20, $X_n\xrightarrow{P}0$.

Verificação direta: $P(|X_n-0|>\varepsilon)\le P(X_n=1)=1/n\to 0$ para qualquer $\varepsilon\in(0,1)$.
