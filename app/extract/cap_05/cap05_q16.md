---
id: "dantas-cap05-q16"
titulo: "Confiabilidade de Máquina com 5 Componentes Exponenciais"
topicos: ["03-modelos-continuos"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "confiabilidade", "esperanca"]
referencia: "Dantas, Cap. 5, Q. 16"
---

## Enunciado

Máquina funciona se pelo menos 3 de 5 componentes funcionarem. Cada componente tem tempo de vida $\sim \text{Exp}(1/5)$ horas, independentemente. (a) $P(\text{máquina funciona por mais de 5 horas})$. (b) Número médio de componentes funcionando 10 horas após ligar.

## Passo 1: Item (a)

Seja $I_i = 1$ se componente $i$ funciona por mais de 5 horas. $P(I_i = 1) = e^{-5/5} = e^{-1}$.

Número de componentes funcionando após 5h: $S \sim \text{Bin}(5, e^{-1})$.

A máquina funciona se $S \ge 3$:

$$P(S \ge 3) = \sum_{k=3}^{5}\binom{5}{k}(e^{-1})^k(1-e^{-1})^{5-k}.$$

Com $p = e^{-1} \approx 0{,}368$ e $1-p \approx 0{,}632$:

$$\approx \binom{5}{3}(0{,}368)^3(0{,}632)^2 + \binom{5}{4}(0{,}368)^4(0{,}632) + \binom{5}{5}(0{,}368)^5$$
$$\approx 10(0{,}0498)(0{,}399) + 5(0{,}0183)(0{,}632) + 0{,}00674$$
$$\approx 0{,}1988 + 0{,}0579 + 0{,}0067 \approx 0{,}163.$$

**Resumo:** $P(\text{funciona} > 5\text{h}) \approx 0{,}163$.

## Passo 2: Item (b)

$P(\text{componente } i \text{ funciona após 10h}) = e^{-10/5} = e^{-2} \approx 0{,}135$.

$E[\text{número funcionando após 10h}] = 5 \cdot e^{-2} \approx 5 \times 0{,}135 = 0{,}677$.

Suposição: os componentes são independentes e operam desde o início.

**Resumo:** Em média 0,677 componentes ainda funcionam após 10 horas.
