---
id: "dantas-cap07-q20"
titulo: "Condição Suficiente para Convergência em Probabilidade"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 7, Q. 20"
---

## Enunciado

$E(X_n^2)<\infty$ para todo $n$. Se $\lim_n E(X_n)=\alpha$ e $\lim_n\text{Var}(X_n)=0$, então $X_n\xrightarrow{P}\alpha$.

## Solução

Para $\varepsilon>0$, pela desigualdade de Tchebyschev:

$$P(|X_n-\alpha|>\varepsilon)\le P(|X_n-E(X_n)|+|E(X_n)-\alpha|>\varepsilon).$$

Para $n$ suficientemente grande, $|E(X_n)-\alpha|<\varepsilon/2$, portanto:

$$P(|X_n-\alpha|>\varepsilon)\le P\!\left(|X_n-E(X_n)|>\frac{\varepsilon}{2}\right)\le\frac{\text{Var}(X_n)}{(\varepsilon/2)^2}=\frac{4\,\text{Var}(X_n)}{\varepsilon^2}\xrightarrow{n\to\infty}0. \quad\blacksquare$$
