---
id: "dantas-cap07-q14"
titulo: "Convergência em Distribuição ≠ Convergência em Probabilidade"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 7, Q. 14"
---

## Enunciado

Na situação do Q13, verifique que $Y_n\not\xrightarrow{P}Z$.

## Solução

Para convergência em probabilidade, precisaríamos que $P(|Y_n-Z|>\varepsilon)\to 0$ para todo $\varepsilon>0$. Mas $Y_n$ e $Z$ são variáveis **independentes** (definidas em espaços distintos — $Y_n$ é função de $X_n$ enquanto $Z$ é a variável limite), então faz sentido avaliar a convergência em distribuição apenas.

De forma mais precisa: $Y_n=X_n/n$ onde $X_n\sim\text{Geom}(\lambda/n)$ é discreta. $Z\sim\text{Exp}(\lambda)$ é contínua. Mesmo no mesmo espaço de probabilidade, $Y_n$ assume apenas valores em $\{1/n, 2/n, \ldots\}$, enquanto $Z$ é contínua.

$$P(|Y_n-Z|>\varepsilon)\ge P(Y_n=k/n, Z\in((k-\varepsilon)/n,(k+\varepsilon)/n)\text{ para algum }k)\not\to 0.$$

Em geral, convergência em distribuição para uma constante implica convergência em probabilidade, mas convergência em distribuição para uma v.a. não-degenerada **não** implica convergência em probabilidade. $\blacksquare$
