---
id: "lista02-q03-distribuio-uniforme-3-7"
titulo: "Distribuição Uniforme (-3, 7)"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["probabilidade", "fda"]
---

## Enunciado

Se X é uniformemente distribuída em (-3,7), determine: 

 a) A função de distribuição de X. 

 b) $ P(|X-1| \le 2) $ 

 c) $ P(|X| > 3) $

## Solução

Temos $X \sim U(-3, 7)$. A FDP é $f(x) = \frac{1}{7 - (-3)} = \frac{1}{10}$ para $x \in (-3, 7)$.

## a) Função de Distribuição (FDA)

A FDA é $F(x) = P(X \le x) = \int_{-\infty}^x f(t)dt$. Dividimos em três casos:<br>1. Se $x \le -3$, $F(x) = \int_{-\infty}^x 0 dt = 0$.<br>2. Se $-3 < x < 7$, $F(x) = \int_{-3}^{x} \frac{1}{10} dt = \frac{1}{10}[t]_{-3}^x = \frac{x-(-3)}{10} = \frac{x+3}{10}$.<br>3. Se $x \ge 7$, $F(x)=1$ pois já acumulou toda a probabilidade.

## b) $ P(|X-1| \le 2) $

Simplificando: $-2 \le X-1 \le 2 \implies -1 \le X \le 3$.<br>$P(-1 \le X \le 3) = \int_{-1}^3 \frac{1}{10} dx = \frac{3 - (-1)}{10} = 0.4$

## c) $ P(|X| > 3) $

Simplificando: $X > 3$ ou $X < -3$. Como o domínio é $(-3,7)$, calculamos $P(3 < X < 7)$.<br>$P(3 < X < 7) = \int_3^7 \frac{1}{10} dx = \frac{7-3}{10} = 0.4$
