---
id: "dantas-cap06-q12"
titulo: "Soma de Normais Independentes"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "fgm"]
referencia: "Dantas, Cap. 6, Q. 12"
---

## Enunciado

Mostre que se $X_i\sim N(\mu_i,\sigma_i^2)$, $i=1,\ldots,n$, independentes, então $\sum_{i=1}^n X_i\sim N\!\left(\sum\mu_i,\sum\sigma_i^2\right)$.

## Solução

Via função geradora de momentos. Primeiro, a FGM de cada $X_i\sim N(\mu_i,\sigma_i^2)$:

$$M_{X_i}(t)=\frac{1}{\sigma_i\sqrt{2\pi}}\int_{-\infty}^{\infty}\exp\!\left\{tx-\frac{(x-\mu_i)^2}{2\sigma_i^2}\right\}dx.$$

Completando o quadrado no expoente:

$$tx-\frac{(x-\mu_i)^2}{2\sigma_i^2}=-\frac{(x-\mu_i-\sigma_i^2 t)^2}{2\sigma_i^2}+\mu_i t+\frac{\sigma_i^2 t^2}{2}.$$

O fator $e^{\mu_i t+\sigma_i^2 t^2/2}$ sai da integral, e o que sobra é a integral da densidade de uma $N(\mu_i+\sigma_i^2 t,\sigma_i^2)$, que vale 1. Logo:

$$M_{X_i}(t)=\exp\!\left\{\mu_i t+\frac{\sigma_i^2 t^2}{2}\right\}.$$

Pela independência, a FGM da soma é o produto das FGMs:

$$M_{\sum X_i}(t)=\prod_{i=1}^n M_{X_i}(t)=\exp\!\left\{\left(\sum\mu_i\right)t+\frac{\left(\sum\sigma_i^2\right)t^2}{2}\right\}.$$

Esta é a FGM de $N\!\left(\sum\mu_i,\sum\sigma_i^2\right)$. Pela unicidade da FGM, $\sum X_i\sim N\!\left(\sum\mu_i,\sum\sigma_i^2\right)$. $\blacksquare$
