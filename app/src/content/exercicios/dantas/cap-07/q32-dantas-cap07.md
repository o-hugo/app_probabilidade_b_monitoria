---
id: "dantas-cap07-q32"
titulo: "TLC — Aproximação para Soma de Normais ao Quadrado"
topicos: ["07-convergencia-e-tlc"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["tlc", "padronizacao-z", "esperanca", "variancia"]
referencia: "Dantas, Cap. 7, Q. 32"
---

## Enunciado

$X_1,X_2,\ldots$ i.i.d. $N(0,\sigma^2)$.

(a) Calcule $E(X_1^2)$ e $\text{Var}(X_1^2)$.
(b) Aproxime $P(X_1^2+\cdots+X_n^2\le x)$ em termos de $\Phi$.

## Solução

**(a)** $X_1^2/\sigma^2\sim\chi^2(1)$, logo:

$$E(X_1^2)=\sigma^2, \qquad E(X_1^4)=3\sigma^4.$$

$$\text{Var}(X_1^2)=E(X_1^4)-[E(X_1^2)]^2=3\sigma^4-\sigma^4=2\sigma^4.$$

**(b)** Seja $S_n=\sum_{i=1}^n X_i^2$. Pelo TLC:

$$E(S_n)=n\sigma^2, \quad \text{Var}(S_n)=2n\sigma^4, \quad \sigma_{S_n}=\sigma^2\sqrt{2n}.$$

$$P(S_n\le x)\approx\Phi\!\left(\frac{x-n\sigma^2}{\sigma^2\sqrt{2n}}\right).$$
