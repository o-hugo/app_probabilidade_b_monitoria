---
id: "dantas-cap06-q38"
titulo: "Conjugado Gama-Exponencial (Priori Gama, Posteriori Gama)"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["condicional", "fdp-valida"]
referencia: "Dantas, Cap. 6, Q. 38"
---

## Enunciado

$W\sim\text{Gama}(\alpha,\beta)$. Dado $W=w$, $X_1,\ldots,X_n$ i.i.d. $\text{Exp}(w)$. Mostre que $W|X_1=x_1,\ldots,X_n=x_n\sim\text{Gama}\!\left(\alpha+n,\ \beta+\sum x_i\right)$.

## Passo 1: Verossimilhança

$$L(w)=\prod_{i=1}^n we^{-wx_i}=w^n e^{-w\sum x_i}.$$

## Passo 2: Priori

$$f_W(w)=\frac{\beta^\alpha}{\Gamma(\alpha)}w^{\alpha-1}e^{-\beta w}, \quad w>0.$$

## Passo 3: Posteriori

Por Bayes, $f_{W|\mathbf{X}}(w|\mathbf{x})\propto L(w)\cdot f_W(w)$:

$$f_{W|\mathbf{X}}(w|\mathbf{x})\propto w^n e^{-w\sum x_i}\cdot w^{\alpha-1}e^{-\beta w}=w^{(\alpha+n)-1}e^{-(\beta+\sum x_i)w}.$$

Reconhecemos o núcleo de $\text{Gama}(\alpha+n,\ \beta+\sum_{i=1}^n x_i)$. $\blacksquare$

**Resumo:** A distribuição Gama é priori conjugada para o parâmetro de uma Exponencial.
