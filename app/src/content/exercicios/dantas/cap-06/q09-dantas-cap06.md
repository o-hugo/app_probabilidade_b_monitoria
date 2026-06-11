---
id: "dantas-cap06-q09"
titulo: "Soma e Razão de Duas Exponenciais Independentes"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano", "fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 9"
---

## Enunciado

$X,Y\sim\text{Exp}(\lambda)$ independentes. Calcule a fdp de:
(a) $Z=X+Y$; (b) $W=X/(X+Y)$.

## Passo 1: Item (a) — $Z=X+Y$

Convolução de duas exponenciais com mesmo parâmetro:

$$f_Z(z)=\int_0^z \lambda e^{-\lambda x}\cdot\lambda e^{-\lambda(z-x)}dx = \lambda^2 e^{-\lambda z}\cdot z = \lambda^2 z e^{-\lambda z}, \quad z>0.$$

Reconhecemos: $Z\sim\text{Gama}(2,\lambda)$.

## Passo 2: Item (b) — $W=X/(X+Y)$

Mudança: $U=X+Y$, $W=X/(X+Y)$, logo $X=WU$, $Y=U(1-W)$. Jacobiano $|J|=u$.

$$f_{U,W}(u,w) = f_X(wu)f_Y(u(1-w))\cdot u = \lambda e^{-\lambda wu}\cdot\lambda e^{-\lambda u(1-w)}\cdot u = \lambda^2 u e^{-\lambda u}.$$

A densidade fatora em $u$ e $w$, portanto $U$ e $W$ são **independentes**:

$$f_W(w)=1,\quad 0<w<1, \implies W\sim U(0,1).$$

$$f_U(u)=\lambda^2 u e^{-\lambda u},\quad u>0 \implies U\sim\text{Gama}(2,\lambda).$$
