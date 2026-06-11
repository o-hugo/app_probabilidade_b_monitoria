---
id: "dantas-cap06-q33"
titulo: "Tamanho Mínimo de Amostra para o Máximo"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 6, Q. 33"
---

## Enunciado

$X_1,\ldots,X_n\sim U(0,1)$ i.i.d. $X_{(n)}=\max_i X_i$. Determine o menor $n$ tal que $P(X_{(n)}\ge 0{,}99)\ge 0{,}95$.

## Solução

$$P(X_{(n)}\ge 0{,}99)=1-P(X_{(n)}<0{,}99)=1-(0{,}99)^n.$$

Queremos $1-(0{,}99)^n\ge 0{,}95$, ou seja $(0{,}99)^n\le 0{,}05$.

$$n\ln(0{,}99)\le\ln(0{,}05) \implies n\ge\frac{\ln(0{,}05)}{\ln(0{,}99)}=\frac{-2{,}9957}{-0{,}01005}\approx 298{,}1.$$

O menor inteiro é $n=\mathbf{299}$.
