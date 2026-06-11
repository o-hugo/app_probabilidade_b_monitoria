---
id: "dantas-cap06-q07"
titulo: "Problema do Encontro — Uniforme em [0,1]"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 6, Q. 7"
---

## Enunciado

Paulo e Pedro decidem se encontrar em um local. Cada um chega independentemente em um tempo uniformemente distribuído entre meio-dia e uma hora da tarde. Qual a probabilidade de que o primeiro a chegar espere mais de 10 minutos?

## Solução

Sejam $X$ e $Y$ os tempos de chegada (em minutos após o meio-dia), $X,Y\sim U(0,60)$ independentes. O primeiro espera mais de 10 minutos se $|X-Y|>10$.

$$P(|X-Y|>10) = 1 - P(|X-Y|\le 10).$$

A região $|x-y|\le 10$ no quadrado $[0,60]^2$ é a faixa diagonal; sua área é $60^2 - 2\cdot\frac{50^2}{2} = 3600 - 2500 = 1100$.

$$P(|X-Y|\le 10)=\frac{1100}{3600}=\frac{11}{36}.$$

$$P(|X-Y|>10)=1-\frac{11}{36}=\frac{25}{36}.$$

**Resumo:** A probabilidade de espera superior a 10 minutos é $\dfrac{25}{36}\approx 0{,}694$.
