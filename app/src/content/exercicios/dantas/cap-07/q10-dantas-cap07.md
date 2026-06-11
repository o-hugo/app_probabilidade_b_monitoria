---
id: "dantas-cap07-q10"
titulo: "nY_n → Exp(1) em Distribuição"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Cap. 7, Q. 10"
---

## Enunciado

$X_1,X_2,\ldots$ i.i.d. $U(0,1)$. $Y_n=\min\{X_1,\ldots,X_n\}$. Mostre que $nY_n\xrightarrow{d}Y$ onde $Y\sim\text{Exp}(1)$.

## Solução

Para $y>0$, a FDA de $nY_n$:

$$P(nY_n>y)=P\!\left(Y_n>\frac{y}{n}\right)=P\!\left(X_1>\frac{y}{n},\ldots,X_n>\frac{y}{n}\right)=\left(1-\frac{y}{n}\right)^n.$$

Tomando o limite:

$$\lim_{n\to\infty}\left(1-\frac{y}{n}\right)^n=e^{-y}.$$

Portanto $P(nY_n\le y)\to 1-e^{-y}$, que é a FDA de $\text{Exp}(1)$. $\blacksquare$
