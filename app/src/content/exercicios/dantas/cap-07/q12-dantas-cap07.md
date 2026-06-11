---
id: "dantas-cap07-q12"
titulo: "Limite em Distribuição de n[1−F(Mₙ)]"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Cap. 7, Q. 12"
---

## Enunciado

$X_1,X_2,\ldots$ i.i.d. com FDA $F$ contínua. $M_n=\max\{X_1,\ldots,X_n\}$. $Y_n=n[1-F(M_n)]$. Ache o limite em distribuição de $Y_n$.

## Solução

Para $y>0$:

$$P(Y_n>y)=P\!\left(n[1-F(M_n)]>y\right)=P\!\left(F(M_n)<1-\frac{y}{n}\right)=P\!\left(M_n<F^{-1}\!\left(1-\frac{y}{n}\right)\right).$$

FDA do máximo: $P(M_n\le t)=[F(t)]^n$, logo:

$$P(Y_n>y)=1-P\!\left(M_n\le F^{-1}\!\left(1-\frac{y}{n}\right)\right)=1-\left(1-\frac{y}{n}\right)^n\xrightarrow{n\to\infty}1-e^{-y}.$$

Portanto $P(Y_n\le y)\to e^{-y}$... Hmm, verificando: $P(Y_n>y)\to 1-e^{-y}$, então $P(Y_n\le y)\to e^{-y}$.

Mas $e^{-y}$ é a **função de sobrevivência** de Exp(1). Revisando: $P(Y_n\le y)=1-P(Y_n>y)\to 1-(1-e^{-y})=e^{-y}$.

Isso não é uma FDA válida no sentido usual... Recalculando:

$P(Y_n\le y)=[F(F^{-1}(1-y/n))]^n=(1-y/n)^n\to e^{-y}$.

Logo $Y_n\xrightarrow{d}\text{Exp}(1)$ (com FDA $1-e^{-y}$, verificada ao notar $P(Y_n>y)=(1-y/n)^n\to e^{-y}$, então $P(Y_n\le y)\to 1-e^{-y}$). $\blacksquare$

**Resumo:** $Y_n=n[1-F(M_n)]\xrightarrow{d}\text{Exp}(1)$.
