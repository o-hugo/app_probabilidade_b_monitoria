---
id: "dantas-cap06-q10"
titulo: "Diferença de Uniformes — Distribuição Independente de θ"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 10"
---

## Enunciado

$X,Y$ independentes com distribuição $U[\theta-\frac{1}{2},\theta+\frac{1}{2}]$, $\theta\in\mathbb{R}$. Mostre que a distribuição de $Z=X-Y$ não depende de $\theta$.

## Solução

Escreva $X=\theta+U$ e $Y=\theta+V$ onde $U,V\sim U(-\frac{1}{2},\frac{1}{2})$ independentes.

Então $Z=X-Y=U-V$.

A distribuição de $U-V$ não depende de $\theta$ — é a distribuição triangular em $(-1,1)$:

$$f_Z(z) = \int_{-1/2}^{1/2} f_U(z+v)\,dv = \int_{\max(-1/2,z-1/2)}^{\min(1/2,z+1/2)} 1\,dv = 1-|z|, \quad |z|<1.$$

Como $f_Z$ não envolve $\theta$, a distribuição de $Z=X-Y$ é independente de $\theta$. $\blacksquare$
