---
id: "dantas-cap07-q07"
titulo: "Tchebyschev Aplicado a Gama(m+1,1)"
topicos: ["07-desigualdades-concentracao"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 7, Q. 7"
---

## Enunciado

$Y$ com $f(y)=\dfrac{1}{m!}y^m e^{-y}$, $y\ge 0$, $m\in\mathbb{N}$. Prove que $P(0\le Y\le 2(m+1))\ge\dfrac{m}{m+1}$.

## Solução

Reconhecemos $Y\sim\text{Gama}(m+1,1)$: $E(Y)=m+1$, $\text{Var}(Y)=m+1$.

Tchebyschev com $k\sigma$: queremos $P(|Y-\mu|\le k\sigma)\ge 1-1/k^2$.

A condição $0\le Y\le 2(m+1)$ equivale a $|Y-(m+1)|\le m+1$, ou seja $k\sigma=m+1$.

$$k=\frac{m+1}{\sigma}=\frac{m+1}{\sqrt{m+1}}=\sqrt{m+1}.$$

Pela desigualdade de Tchebyschev:

$$P(|Y-(m+1)|\le m+1)\ge 1-\frac{1}{k^2}=1-\frac{1}{m+1}=\frac{m}{m+1}. \quad\blacksquare$$

Obs.: como $P(Y<0)=0$ (suporte $[0,\infty)$), a condição $Y\ge 0$ é automática.
