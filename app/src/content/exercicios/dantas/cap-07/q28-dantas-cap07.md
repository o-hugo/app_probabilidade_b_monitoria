---
id: "dantas-cap07-q28"
titulo: "TLC — Proporção de Favoráveis em Amostra de 100"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "probabilidade"]
referencia: "Dantas, Cap. 7, Q. 28"
---

## Enunciado

65% da população é favorável a uma proposta. Amostra de $n=100$. Determine:

(a) $P(S_{100}\ge 50)$. (b) $P(S_{100}\le 75)$.

## Solução

$S_{100}\sim\text{Bin}(100;0{,}65)$: $E=65$, $\text{Var}=100\cdot 0{,}65\cdot 0{,}35=22{,}75$, $\sigma\approx 4{,}77$.

Pelo TLC: $S_{100}\approx N(65;22{,}75)$.

**(a) $P(S_{100}\ge 50)$:**

$$P\!\left(Z\ge\frac{50-65}{4{,}77}\right)=P(Z\ge -3{,}14)=\Phi(3{,}14)\approx 0{,}9992.$$

**(b) $P(S_{100}\le 75)$:**

$$P\!\left(Z\le\frac{75-65}{4{,}77}\right)=P(Z\le 2{,}10)=\Phi(2{,}10)\approx 0{,}9821.$$
