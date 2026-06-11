---
id: "dantas-cap06-q16"
titulo: "Distribuição de Maxwell"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-fda", "fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 16"
---

## Enunciado

$X_1,X_2,X_3\sim N(0,\sigma^2)$ independentes. $Y=(X_1^2+X_2^2+X_3^2)^{1/2}$. Determine a densidade de $Y$ (distribuição de Maxwell).

## Passo 1: Soma dos quadrados

$V=X_1^2+X_2^2+X_3^2$. Cada $X_i^2/\sigma^2\sim\chi^2(1)$, logo $V/\sigma^2\sim\chi^2(3)$, ou seja $V\sim\text{Gama}(3/2,\,1/(2\sigma^2))$.

$$f_V(v)=\frac{1}{2^{3/2}\sigma^3\Gamma(3/2)}v^{1/2}e^{-v/(2\sigma^2)}, \quad v>0.$$

## Passo 2: Transformação $Y=\sqrt{V}$

$V=Y^2$, $|dV/dY|=2y$.

$$f_Y(y)=f_V(y^2)\cdot 2y = \frac{2y}{\sqrt{2\pi}\,\sigma^3}\cdot y e^{-y^2/(2\sigma^2)}\cdot\sqrt{2}=\sqrt{\frac{2}{\pi}}\cdot\frac{y^2}{\sigma^3}e^{-y^2/(2\sigma^2)}, \quad y>0.$$

Usando $\Gamma(3/2)=\sqrt{\pi}/2$:

$$\boxed{f_Y(y)=\sqrt{\frac{2}{\pi}}\,\frac{y^2}{\sigma^3}\,e^{-y^2/(2\sigma^2)}, \quad y>0.}$$

Esta é a **distribuição de Maxwell** com parâmetro $\sigma$.
