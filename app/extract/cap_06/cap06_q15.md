---
id: "dantas-cap06-q15"
titulo: "Área de Chapa Retangular S = A×B"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "probabilidade", "metodo-fda"]
referencia: "Dantas, Cap. 6, Q. 15"
---

## Enunciado

$A$ e $B$ independentes com:
$$f_A(x)=\begin{cases}x-1,&1\le x\le 2\\3-x,&2<x\le 3\\0,&\text{c.c.}\end{cases}, \qquad f_B(y)=\tfrac{1}{2},\ 2\le y\le 4.$$
Determine: (a) a fdp de $S=AB$; (b) $E(S)$; (c) $P(S>10)$.

## Passo 1: Item (b) — $E(S)=E(A)E(B)$

$$E(A)=\int_1^2(x-1)x\,dx+\int_2^3(3-x)x\,dx=\int_1^2(x^2-x)dx+\int_2^3(3x-x^2)dx.$$

$$=\left[\frac{x^3}{3}-\frac{x^2}{2}\right]_1^2+\left[\frac{3x^2}{2}-\frac{x^3}{3}\right]_2^3=\frac{5}{6}+\frac{7}{6}=2.$$

$$E(B)=\int_2^4 y\cdot\frac{1}{2}dy=3.$$

$$E(S)=E(A)E(B)=6.$$

## Passo 2: Item (a) — fdp de $S$

Para $s$ fixo, $S=AB\le s$ iff $A\le s/B$. Condicionando em $B=b$ ($b\in[2,4]$):

$$F_S(s)=\int_2^4 F_A(s/b)\cdot\frac{1}{2}db.$$

Diferenciando: $f_S(s)=\frac{1}{2}\int_2^4\frac{1}{b}f_A(s/b)db$.

## Passo 3: Item (c) — $P(S>10)$

$$P(S>10)=1-F_S(10)=1-\frac{1}{2}\int_2^4 F_A(10/b)db.$$

(Avaliação numérica: $10/b\in[2{,}5,5]$ para $b\in[2,4]$; $f_A$ tem suporte $[1,3]$.)
