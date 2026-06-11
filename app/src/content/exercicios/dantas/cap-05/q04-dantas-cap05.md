---
id: "dantas-cap05-q04"
titulo: "Tempo de Espera Uniforme no Ponto de Ônibus"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "(a) 2/3  (b) 1/3"
tags: ["probabilidade"]
referencia: "Dantas, Cap. 5, Q. 4"
---

## Enunciado

Ônibus chegam a cada 15 minutos (7h00, 7h15, 7h30, ...). Um passageiro chega uniformemente distribuído entre 7h00 e 7h30. Determine a probabilidade: (a) de que ele espere menos de 5 minutos; (b) de que ele espere mais de 10 minutos.

## Passo 1: Modelar o tempo de espera

Seja $X \sim U(0, 30)$ o instante de chegada (em minutos após 7h00). O próximo ônibus chega em $t^* = 15\lceil X/15 \rceil$. O tempo de espera é $W = t^* - X$.

- Se $0 \le X < 15$: $W = 15 - X$.
- Se $15 \le X < 30$: $W = 30 - X$.

Em ambos os casos $W = (15 - X \bmod 15)$, e $W$ é uniforme em $(0, 15)$ por simetria.

**Resumo:** $W \sim U(0, 15)$.

## Passo 2: Calcular as probabilidades

**(a)** $P(W < 5) = 5/15 = 1/3$... 

Revisando: $P(W < 5)$ corresponde a chegar nos últimos 5 minutos de cada ciclo de 15: intervalos $(10,15)$ e $(25,30)$, cada com comprimento 5 em $U(0,30)$:
$$P(W < 5) = \frac{5+5}{30} = \frac{10}{30} = \frac{1}{3}.$$

Mas o enunciado pede "menos que 5 minutos" — **não** incluindo exatamente 5. Para contínua, $P(W < 5) = P(W \le 5) = 1/3$.

**(b)** $P(W > 10)$: chegar nos primeiros 5 minutos de cada ciclo — intervalos $(0,5)$ e $(15,20)$:
$$P(W > 10) = \frac{5+5}{30} = \frac{1}{3}.$$
