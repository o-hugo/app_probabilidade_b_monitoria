---
id: "dantas-cap06-q11"
titulo: "Soma de Variáveis Gama Independentes"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "fgm"]
referencia: "Dantas, Cap. 6, Q. 11"
---

## Enunciado

(a) Mostre que se $X\sim\text{Gama}(\alpha,\lambda)$ e $Y\sim\text{Gama}(\beta,\lambda)$ independentes, então $X+Y\sim\text{Gama}(\alpha+\beta,\lambda)$.

(b) Por indução, se $X_i\sim\text{Gama}(\alpha_i,\lambda)$ independentes, então $\sum X_i\sim\text{Gama}(\sum\alpha_i,\lambda)$.

(c) Se $X_1,\ldots,X_n\sim\text{Exp}(\lambda)$ independentes, qual a distribuição de $S=\sum X_i$?

## Solução

**(a) Via FGM:**

$$M_{X+Y}(t)=M_X(t)M_Y(t)=\left(\frac{\lambda}{\lambda-t}\right)^\alpha\!\!\left(\frac{\lambda}{\lambda-t}\right)^\beta=\left(\frac{\lambda}{\lambda-t}\right)^{\alpha+\beta}, \quad t<\lambda.$$

Esta é a FGM de $\text{Gama}(\alpha+\beta,\lambda)$. $\blacksquare$

**(b) Por indução:** Base: (a). Passo: se $\sum_{i=1}^k X_i\sim\text{Gama}(\sum_{i=1}^k\alpha_i,\lambda)$, então adicionando $X_{k+1}$ independente aplica-se (a). $\blacksquare$

**(c)** $\text{Exp}(\lambda)=\text{Gama}(1,\lambda)$, logo $\sum_{i=1}^n X_i\sim\text{Gama}(n,\lambda)$.
