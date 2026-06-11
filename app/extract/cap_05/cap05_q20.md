---
id: "dantas-cap05-q20"
titulo: "Taxa de Falha da Distribuição Uniforme"
topicos: ["03-modelos-continuos"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
resposta_final: "h(x) = 1/(a-x) para 0 < x < a"
tags: ["taxa-de-falha"]
referencia: "Dantas, Cap. 5, Q. 20"
---

## Enunciado

Calcule a função taxa de falha de $X \sim U(0,a)$, $a>0$.

## Solução

$f(x) = 1/a$ e $R(x) = P(X > x) = (a-x)/a$ para $0 < x < a$.

$$h(x) = \frac{f(x)}{R(x)} = \frac{1/a}{(a-x)/a} = \frac{1}{a-x}, \quad 0 < x < a.$$

A taxa de falha é **crescente** em $x$ (tende a $\infty$ quando $x \to a^-$), refletindo que quanto mais próximo do limite $a$, maior a probabilidade instantânea de falha — um objeto que "inevitavelmente" falha antes de $a$.
