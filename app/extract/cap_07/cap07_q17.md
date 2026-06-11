---
id: "dantas-cap07-q17"
titulo: "Gama(n,β)/n → Limite em Distribuição"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Cap. 7, Q. 17"
---

## Enunciado

$X_n\sim\text{Gama}(n,\beta)$, $\beta>0$. Calcule o limite em distribuição de $Z_n=X_n/n$.

## Solução

$X_n\sim\text{Gama}(n,\beta)$ tem $E(X_n)=n/\beta$ e $\text{Var}(X_n)=n/\beta^2$.

$Z_n=X_n/n$: $E(Z_n)=1/\beta$ e $\text{Var}(Z_n)=1/(n\beta^2)\to 0$.

Pelo exercício Q20 (ou pela LGN para somas de Exp$(\beta)$ i.i.d.): como $X_n\overset{d}{=}\sum_{i=1}^n Y_i$ com $Y_i\sim\text{Exp}(\beta)$ i.i.d., temos

$$Z_n=\frac{1}{n}\sum_{i=1}^n Y_i\xrightarrow{P}E(Y_1)=\frac{1}{\beta}.$$

Convergência em probabilidade para a constante $1/\beta$ implica convergência em distribuição:

$$Z_n\xrightarrow{d}\frac{1}{\beta} \quad\text{(distribuição degenerada em }1/\beta\text{)}.$$
