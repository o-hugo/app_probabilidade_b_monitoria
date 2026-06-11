---
id: "dantas-cap07-q13"
titulo: "Geométrica Escalada → Exponencial em Distribuição"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Cap. 7, Q. 13"
---

## Enunciado

$X_n\sim\text{Geom}(\lambda/n)$, $0<\lambda<n$. $Y_n=X_n/n$. Prove que $Y_n\xrightarrow{d}Z$ onde $Z\sim\text{Exp}(\lambda)$.

## Solução

Para a geométrica com parâmetro $p=\lambda/n$ (número de tentativas até o 1º sucesso):

$$P(X_n>k)=(1-\lambda/n)^k, \quad k=0,1,2,\ldots$$

Para $y>0$, $P(Y_n>y)=P(X_n>ny)=P(X_n>\lfloor ny\rfloor)=(1-\lambda/n)^{\lfloor ny\rfloor}$.

$$\lim_{n\to\infty}(1-\lambda/n)^{\lfloor ny\rfloor}=\lim_{n\to\infty}\left[(1-\lambda/n)^n\right]^{\lfloor ny\rfloor/n}=e^{-\lambda y}.$$

Portanto $P(Y_n\le y)\to 1-e^{-\lambda y}$, que é a FDA de $\text{Exp}(\lambda)$. $\blacksquare$
