---
id: "dantas-cap07-q18"
titulo: "Distribuição Discreta Uniforme → Uniforme Contínua"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Cap. 7, Q. 18"
---

## Enunciado

$P\{X_n=k/n\}=\dfrac{1}{n+1}$ para $k=0,1,\ldots,n$. Ache o limite em distribuição de $X_n$.

## Solução

Para $x\in[0,1]$, a FDA de $X_n$:

$$F_n(x)=P(X_n\le x)=\frac{\lfloor nx\rfloor+1}{n+1}.$$

Tomando o limite:

$$\lim_{n\to\infty}F_n(x)=\lim_{n\to\infty}\frac{\lfloor nx\rfloor+1}{n+1}=x, \quad x\in[0,1].$$

(pois $\lfloor nx\rfloor/n\to x$).

Portanto $X_n\xrightarrow{d}U(0,1)$.
