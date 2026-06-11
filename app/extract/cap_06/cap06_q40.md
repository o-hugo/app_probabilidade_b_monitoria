---
id: "dantas-cap06-q40"
titulo: "Esperança e Variância com Densidade Condicional Exponencial"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "esperanca", "variancia"]
referencia: "Dantas, Cap. 6, Q. 40"
---

## Enunciado

$X$ com $f(x)=2x$, $0\le x\le 1$. Dado $X=x$, $Y|X=x\sim\text{Exp}(\lambda x)$. Calcule $E(Y)$ e $\text{Var}(Y)$.

## Passo 1: $E(Y)$ via esperança iterada

$E(Y|X=x)=\frac{1}{\lambda x}$:

$$E(Y)=E\!\left[\frac{1}{\lambda X}\right]=\frac{1}{\lambda}\int_0^1\frac{1}{x}\cdot 2x\,dx=\frac{2}{\lambda}.$$

## Passo 2: $\text{Var}(Y)$ via lei da variância total

$$\text{Var}(Y)=E[\text{Var}(Y|X)]+\text{Var}(E[Y|X]).$$

$\text{Var}(Y|X=x)=\frac{1}{(\lambda x)^2}$:

$$E[\text{Var}(Y|X)]=E\!\left[\frac{1}{\lambda^2 X^2}\right]=\frac{1}{\lambda^2}\int_0^1\frac{1}{x^2}\cdot 2x\,dx=\frac{2}{\lambda^2}\int_0^1\frac{1}{x}dx.$$

A integral $\int_0^1 1/x\,dx$ diverge — a variância não existe em sentido clássico. Caso o enunciado tenha $\lambda x$ como taxa para $Y>0$ e a integral for interpretada como finita, revisar se $f(x)=2x$ implica suporte $(0,1]$ sem problema em $x=0$.

**Resumo (resultado formal):** $E(Y)=2/\lambda$; $\text{Var}(Y)$ diverge por $\int_0^1 x^{-1}\cdot 2x\,dx=2$, logo $E[\text{Var}(Y|X)]=2/\lambda^2$.

$\text{Var}(E[Y|X])=\text{Var}(1/(\lambda X))=\frac{1}{\lambda^2}\text{Var}(1/X)$.

$$E(1/X^2)=\int_0^1 2\,dx=2,\quad E(1/X)=2 \implies \text{Var}(1/X)=2-4<0\ \text{(erro)}.$$

Revisão: $E(1/X)=\int_0^1 \frac{1}{x}\cdot 2x\,dx=2$ e $E(1/X^2)=\int_0^1\frac{1}{x^2}\cdot 2x\,dx=\int_0^1\frac{2}{x}dx$ diverge. Portanto $\text{Var}(Y)=\infty$.
