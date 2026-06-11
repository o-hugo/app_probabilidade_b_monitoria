---
id: "dantas-cap05-q09"
titulo: "Razão dos Segmentos — Ponto Aleatório em Segmento"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "2/5"
tags: ["probabilidade"]
referencia: "Dantas, Cap. 5, Q. 9"
---

## Enunciado

Um ponto é escolhido ao acaso num segmento de comprimento $L$. Determine a probabilidade de que a razão entre o menor e o maior segmento obtidos seja menor que $1/4$.

## Solução

Seja $X \sim U(0, L)$ a posição do ponto. Os dois segmentos têm comprimentos $X$ e $L - X$. O menor é $\min(X, L-X)$ e o maior é $\max(X, L-X)$.

A razão $\frac{\min(X, L-X)}{\max(X, L-X)} < \frac{1}{4}$ equivale a $\min < \frac{1}{5}L$ (pois se menor$/$(maior) $< 1/4$ e menor $+$ maior $= L$, então menor $< L/5$).

De fato: menor$/$(maior) $< 1/4 \Rightarrow$ menor $< L - $ menor$)/4 \Rightarrow 5\cdot$menor $< L \Rightarrow$ menor $< L/5$.

Isso ocorre quando $X < L/5$ ou $X > 4L/5$:

$$P = \frac{L/5 + (L - 4L/5)}{L} = \frac{L/5 + L/5}{L} = \frac{2}{5}.$$
