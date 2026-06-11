---
id: "dantas-cap07-q15"
titulo: "Convergência em Probabilidade Implica em Distribuição"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 7, Q. 15"
---

## Enunciado

Mostre que $X_n\xrightarrow{P}X\Rightarrow X_n\xrightarrow{d}X$.

## Solução

Seja $F_n$ a FDA de $X_n$, $F$ a FDA de $X$. Fixe $x$ ponto de continuidade de $F$ e $\varepsilon>0$.

$$F_n(x)=P(X_n\le x)=P(X_n\le x,X\le x+\varepsilon)+P(X_n\le x,X>x+\varepsilon).$$

$$\le P(X\le x+\varepsilon)+P(|X_n-X|>\varepsilon)=F(x+\varepsilon)+P(|X_n-X|>\varepsilon).$$

Analogamente, $F(x-\varepsilon)\le F_n(x)+P(|X_n-X|>\varepsilon)$.

Como $X_n\xrightarrow{P}X$: $P(|X_n-X|>\varepsilon)\to 0$.

Portanto $F(x-\varepsilon)\le\liminf_n F_n(x)\le\limsup_n F_n(x)\le F(x+\varepsilon)$.

Tomando $\varepsilon\to 0$ e usando continuidade de $F$ em $x$: $F_n(x)\to F(x)$. $\blacksquare$
