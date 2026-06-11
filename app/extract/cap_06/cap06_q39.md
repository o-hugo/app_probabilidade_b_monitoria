---
id: "dantas-cap06-q39"
titulo: "Conjugado Beta-Bernoulli (Priori Beta, Posteriori Beta)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 39"
---

## Enunciado

$Y\sim\text{Beta}(\alpha,\beta)$. Dado $Y=y$, $X_1,\ldots,X_n$ i.i.d. $\text{Bernoulli}(y)$. Verifique que $Y|X_1=x_1,\ldots,X_n=x_n\sim\text{Beta}\!\left(\alpha+\sum x_i,\ \beta+n-\sum x_i\right)$.

## Passo 1: Verossimilhança

Seja $s=\sum_{i=1}^n x_i$:

$$L(y)=y^s(1-y)^{n-s}.$$

## Passo 2: Priori

$$f_Y(y)=\frac{1}{B(\alpha,\beta)}y^{\alpha-1}(1-y)^{\beta-1}, \quad 0<y<1.$$

## Passo 3: Posteriori

$$f_{Y|\mathbf{X}}(y|\mathbf{x})\propto y^s(1-y)^{n-s}\cdot y^{\alpha-1}(1-y)^{\beta-1}=y^{(\alpha+s)-1}(1-y)^{(\beta+n-s)-1}.$$

Reconhecemos o núcleo de $\text{Beta}(\alpha+s,\ \beta+n-s)$ com $s=\sum x_i$. $\blacksquare$

**Resumo:** A distribuição Beta é priori conjugada para o parâmetro de uma Bernoulli.
