---
id: "dantas-cap01-q34"
titulo: "Bayes: Peca Defeituosa por Maquina"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional"]
referencia: "Dantas, Cap. 1, Q. 34"
---

## Enunciado
Três máquinas A, B e C produzem 50%, 30% e 20%, respectivamente, do total de peças de uma fábrica. As porcentagens de produção defeituosa destas máquinas são 3%, 4% e 5%. Se uma peça é selecionada aleatoriamente, ache a probabilidade de ela ser defeituosa. Se a peça selecionada é defeituosa, encontre a probabilidade de ter sido produzida pela máquina C.

## Solução

Este é um problema clássico que usa a Lei da Probabilidade Total e o Teorema de Bayes.
As probabilidades a priori de uma peça vir de cada máquina são:
$P(A) = 0,50$
$P(B) = 0,30$
$P(C) = 0,20$

As probabilidades condicionais de uma peça ser defeituosa ($D$), dado que veio de determinada máquina, são:
$P(D \mid A) = 0,03$
$P(D \mid B) = 0,04$
$P(D \mid C) = 0,05$

- **1. Probabilidade de a peça selecionada ser defeituosa ($P(D)$):**
Usamos a Lei da Probabilidade Total:
$$ P(D) = P(A)P(D \mid A) + P(B)P(D \mid B) + P(C)P(D \mid C) $$
$$ P(D) = (0,50 \times 0,03) + (0,30 \times 0,04) + (0,20 \times 0,05) $$
$$ P(D) = 0,015 + 0,012 + 0,010 = 0,037 $$
A probabilidade de a peça ser defeituosa é **0,037** ou **3,7%**.

- **2. Probabilidade de ter sido produzida pela máquina C, sabendo que é defeituosa:**
Usamos o Teorema de Bayes para encontrar $P(C \mid D)$:
$$ P(C \mid D) = \frac{P(C)P(D \mid C)}{P(D)} $$
$$ P(C \mid D) = \frac{0,010}{0,037} = \frac{10}{37} \approx 0,2703 $$
A probabilidade de ter vindo da máquina C é de aproximadamente **27,03%**.
