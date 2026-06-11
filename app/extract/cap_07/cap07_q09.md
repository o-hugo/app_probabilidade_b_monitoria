---
id: "dantas-cap07-q09"
titulo: "Máximo e Mínimo de Uniformes — Convergência em Probabilidade"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 7, Q. 9"
---

## Enunciado

$X_1,X_2,\ldots$ i.i.d. $U(0,1)$. $Y_n=\max\{X_1,\ldots,X_n\}$, $Z_n=\min\{X_1,\ldots,X_n\}$. Prove: (a) $Y_n\xrightarrow{P}1$; (b) $Z_n\xrightarrow{P}0$.

## Solução

**(a) $Y_n\xrightarrow{P}1$:** Para $\varepsilon>0$:

$$P(|Y_n-1|>\varepsilon)=P(Y_n<1-\varepsilon)=P(X_1<1-\varepsilon,\ldots,X_n<1-\varepsilon)=(1-\varepsilon)^n\xrightarrow{n\to\infty}0. \quad\blacksquare$$

**(b) $Z_n\xrightarrow{P}0$:** Para $\varepsilon>0$:

$$P(|Z_n-0|>\varepsilon)=P(Z_n>\varepsilon)=P(X_1>\varepsilon,\ldots,X_n>\varepsilon)=(1-\varepsilon)^n\xrightarrow{n\to\infty}0. \quad\blacksquare$$
