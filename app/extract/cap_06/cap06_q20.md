---
id: "dantas-cap06-q20"
titulo: "Gama Independentes: U=X+Y, V=X/(X+Y)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["metodo-jacobiano"]
referencia: "Dantas, Cap. 6, Q. 20"
---

## Enunciado

$X\sim\text{Gama}(\alpha,\lambda)$ e $Y\sim\text{Gama}(\beta,\lambda)$ independentes. Calcule a densidade conjunta de $U=X+Y$ e $V=X/(X+Y)$. $U$ e $V$ são independentes?

## Passo 1: Inversão e Jacobiano

$X=UV$, $Y=U(1-V)$. Jacobiano: $|J|=u$.

## Passo 2: Densidade conjunta

$$f_{U,V}(u,v)=f_X(uv)f_Y(u(1-v))\cdot u$$
$$=\frac{(uv)^{\alpha-1}e^{-\lambda uv}}{\Gamma(\alpha)}\lambda^\alpha\cdot\frac{(u(1-v))^{\beta-1}e^{-\lambda u(1-v)}}{\Gamma(\beta)}\lambda^\beta\cdot u$$
$$=\frac{\lambda^{\alpha+\beta}}{\Gamma(\alpha)\Gamma(\beta)}u^{\alpha+\beta-1}e^{-\lambda u}\cdot v^{\alpha-1}(1-v)^{\beta-1}.$$

## Passo 3: Independência e identificação

A densidade fatora:

$$f_{U,V}(u,v)=\underbrace{\frac{\lambda^{\alpha+\beta}}{\Gamma(\alpha+\beta)}u^{\alpha+\beta-1}e^{-\lambda u}}_{f_U(u)}\cdot\underbrace{\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}v^{\alpha-1}(1-v)^{\beta-1}}_{f_V(v)}.$$

- $U\sim\text{Gama}(\alpha+\beta,\lambda)$.
- $V\sim\text{Beta}(\alpha,\beta)$.
- $U$ e $V$ são **independentes**. $\blacksquare$
