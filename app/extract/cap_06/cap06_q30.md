---
id: "dantas-cap06-q30"
titulo: "Estatísticas de Ordem — Uniforme (0,1): Amplitude e Correlação"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "metodo-fda"]
referencia: "Dantas, Cap. 6, Q. 30"
---

## Enunciado

Condições do Q29. (a) Determine $E[F(X_{(1)})]$ e $E[F(X_{(n)})]$.

Para $f(x)=1$, $F(x)=x$, $0\le x\le 1$:
(b) Densidade de $A=X_{(n)}-X_{(1)}$.
(c) $E(X_{(1)})$, $E(X_{(n)})$ e correlação entre $X_{(1)}$ e $X_{(n)}$.

## Passo 1: Item (a)

A densidade marginal de $X_{(k)}$ é $f_{(k)}(x)=\frac{n!}{(k-1)!(n-k)!}[F(x)]^{k-1}[1-F(x)]^{n-k}f(x)$.

Por substituição $u=F(x)$ (uniforme em $(0,1)$ se $F$ contínua):

$$E[F(X_{(1)})]=\frac{1}{n+1}, \qquad E[F(X_{(n)})]=\frac{n}{n+1}.$$

## Passo 2: Item (b) — Densidade de $A$ com $U(0,1)$

Da Q29 com $f=1$, $F(x)=x$: $f_{X_{(1)},X_{(n)}}(x,y)=n(n-1)(y-x)^{n-2}$, $0<x<y<1$.

$$f_A(a)=\int_0^{1-a}n(n-1)a^{n-2}dx=n(n-1)a^{n-2}(1-a), \quad 0<a<1.$$

Reconhecemos: $A\sim\text{Beta}(n-1,2)$.

## Passo 3: Item (c)

$X_{(k)}\sim\text{Beta}(k,n-k+1)$ para $U(0,1)$:

$$E(X_{(1)})=\frac{1}{n+1}, \qquad E(X_{(n)})=\frac{n}{n+1}.$$

Para a correlação, $\text{Cov}(X_{(1)},X_{(n)})=E[X_{(1)}X_{(n)}]-E[X_{(1)}]E[X_{(n)}]$.

$$E[X_{(1)}X_{(n)}]=n(n-1)\int_0^1\int_0^y xy(y-x)^{n-2}dx\,dy=\frac{n+1}{(n+1)^2(n+2)}\cdot\ldots=\frac{1}{(n+1)(n+2)}.$$

$$\text{Var}(X_{(1)})=\text{Var}(X_{(n)})=\frac{n}{(n+1)^2(n+2)}.$$

$$\text{Corr}(X_{(1)},X_{(n)})=\frac{1/[(n+1)(n+2)]-n/(n+1)^2}{n/[(n+1)^2(n+2)]}=\frac{1}{n}.$$
