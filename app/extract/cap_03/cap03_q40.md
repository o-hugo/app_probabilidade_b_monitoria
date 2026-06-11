---
id: "dantas-cap03-q40"
titulo: "Exame de Sangue em Grupo (Pool Testing)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "probabilidade"]
referencia: "Dantas, Cap. 3, Q. 40"
---

## Enunciado

$N$ pessoas são submetidas a exame de sangue. Cada pessoa tem probabilidade $p$ de teste positivo, independentemente. No plano (ii), misturam-se amostras de $k$ pessoas:
- Se o teste é **negativo**: 1 teste basta para as $k$ pessoas.
- Se o teste é **positivo**: testa-se cada uma separadamente; total de $k+1$ testes.

**(a)** Qual a probabilidade de que a amostra misturada seja positiva?

**(b)** Qual o valor esperado do número de testes para as $k$ pessoas?

## Passo 1: Item (a) — Probabilidade de positivo na amostra misturada

O teste da amostra misturada é negativo somente se **todas** as $k$ pessoas forem negativas. A probabilidade de negativo individual é $1-p$, e as pessoas são independentes:

$$P[\text{amostra positiva}] = 1 - (1-p)^k.$$

**Resumo:** $P[\text{positivo}] = 1-(1-p)^k$ pelo complementar e independência.

## Passo 2: Item (b) — $E[\text{número de testes}]$

Seja $T$ o número de testes para as $k$ pessoas. Então:

$$T = \begin{cases} 1 & \text{com probabilidade } (1-p)^k \\ k+1 & \text{com probabilidade } 1-(1-p)^k \end{cases}$$

$$E[T] = 1 \cdot (1-p)^k + (k+1)\bigl[1-(1-p)^k\bigr]$$

$$= (1-p)^k + (k+1) - (k+1)(1-p)^k$$

$$= (k+1) - k(1-p)^k.$$

**Resumo:** $E[T] = (k+1) - k(1-p)^k$ testes esperados por grupo de $k$ pessoas.
