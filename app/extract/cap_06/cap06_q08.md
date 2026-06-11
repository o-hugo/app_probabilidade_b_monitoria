---
id: "dantas-cap06-q08"
titulo: "Soma e Razão: Uniforme + Exponencial"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano", "metodo-fda"]
referencia: "Dantas, Cap. 6, Q. 8"
---

## Enunciado

$X\sim U(0,1)$ e $Y\sim\text{Exp}(1)$, independentes. Determine a distribuição de:
(a) $Z=X+Y$; (b) $W=X/Y$.

## Passo 1: Item (a) — $Z=X+Y$

Convolução: $f_Z(z)=\int f_X(z-y)f_Y(y)\,dy$ com $f_X(u)=\mathbf{1}_{[0,1]}(u)$, $f_Y(y)=e^{-y}\mathbf{1}_{y\ge 0}$.

Precisamos $z-y\in[0,1]$ e $y\ge 0$, i.e., $y\in[\max(0,z-1),z]$.

- Para $0<z\le 1$: $\int_0^z e^{-y}dy = 1-e^{-z}$.
- Para $1<z$: $\int_{z-1}^{z}e^{-y}dy = e^{-(z-1)}-e^{-z}=e^{-z}(e-1)$.

$$f_Z(z) = \begin{cases} 1-e^{-z}, & 0<z\le 1,\\ e^{-z}(e-1), & z>1.\end{cases}$$

## Passo 2: Item (b) — $W=X/Y$

Pelo método jacobiano: $X=WY$, $Y=Y$; Jacobiano $|J|=y$.

$$f_{W,Y}(w,y)=f_X(wy)f_Y(y)\cdot y = \mathbf{1}_{[0,1]}(wy)\cdot e^{-y}\cdot y.$$

Condição $wy\in[0,1]$: $y\in[0,1/w]$ (para $w>0$).

$$f_W(w)=\int_0^{1/w}ye^{-y}dy.$$

Integrando por partes: $\int_0^{1/w}ye^{-y}dy=1-e^{-1/w}\!\left(1+\frac{1}{w}\right)$, para $w>0$.
