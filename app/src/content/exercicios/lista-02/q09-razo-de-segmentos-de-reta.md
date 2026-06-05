---
id: "lista02-q09-razo-de-segmentos-de-reta"
titulo: "Razão de Segmentos de Reta"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Ponto X é escolhido ao acaso em $(0, L)$. P(razão entre menor/maior segmento < 1/4)?

## Solução

Se o ponto é $X \sim U(0,L)$, os segmentos são $X$ e $L-X$. Queremos $P(\frac{\min(X, L-X)}{\max(X, L-X)} < 1/4)$.<br>**Caso 1: $X < L/2$** (X é o menor). A razão é $\frac{X}{L-X} < \frac{1}{4} \implies 4X < L-X \implies 5X < L \implies X < L/5$.<br>**Caso 2: $X > L/2$** (L-X é o menor). A razão é $\frac{L-X}{X} < \frac{1}{4} \implies 4L - 4X < X \implies 4L < 5X \implies X > 4L/5$.<br>O evento ocorre se $X \in (0, L/5) \cup (4L/5, L)$.<br>$ P = \frac{(L/5 - 0) + (L - 4L/5)}{L} = \frac{2L/5}{L} = \frac{2}{5} = 0.4 $
