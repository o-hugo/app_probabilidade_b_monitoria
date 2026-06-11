---
id: "dantas-cap06-q41"
titulo: "Mistura Poisson-Exponencial → Distribuição Geométrica"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "falta-de-memoria"]
referencia: "Dantas, Cap. 6, Q. 41"
---

## Enunciado

Dado $Y=y$, $X|Y=y\sim\text{Poisson}(y)$. $Y\sim\text{Exp}(1)$. Determine a distribuição de $X$.

## Solução

$$P(X=k)=\int_0^\infty P(X=k|Y=y)f_Y(y)\,dy=\int_0^\infty\frac{e^{-y}y^k}{k!}\cdot e^{-y}\,dy=\frac{1}{k!}\int_0^\infty y^k e^{-2y}dy.$$

Pela integral gama: $\int_0^\infty y^k e^{-2y}dy=\frac{k!}{2^{k+1}}$.

$$P(X=k)=\frac{1}{k!}\cdot\frac{k!}{2^{k+1}}=\frac{1}{2^{k+1}}=\frac{1}{2}\left(\frac{1}{2}\right)^k, \quad k=0,1,2,\ldots$$

**Reconhecemos:** $X\sim\text{Geom}(1/2)$ (com $P(X=k)=(1-p)^k p$, $p=1/2$).

**Resumo:** A mistura Poisson-Exponencial produz a distribuição Geométrica com $p=1/2$.
