---
id: "dantas-cap05-q36"
titulo: "Esperança e Variância da Distribuição de Pareto"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "E(X)=αβ/(α-1) para α>1; Var(X)=αβ²/[(α-1)²(α-2)] para α>2"
tags: ["esperanca", "variancia"]
referencia: "Dantas, Cap. 5, Q. 36"
---

## Enunciado

$X \sim \text{Pareto}(\alpha,\beta)$: $f(x) = \frac{\alpha}{\beta}\left(\frac{\beta}{x}\right)^{\alpha+1}$, $x > \beta$. Mostre que $E(X) = \frac{\alpha\beta}{\alpha-1}$ ($\alpha>1$) e $\text{Var}(X) = \frac{\alpha\beta^2}{(\alpha-1)^2(\alpha-2)}$ ($\alpha>2$).

## Passo 1: $E(X)$

$$E(X) = \int_\beta^\infty x \cdot \frac{\alpha\beta^\alpha}{x^{\alpha+1}}dx = \alpha\beta^\alpha \int_\beta^\infty x^{-\alpha}dx = \alpha\beta^\alpha \cdot \frac{x^{-\alpha+1}}{-\alpha+1}\Bigg|_\beta^\infty = \frac{\alpha\beta^\alpha \cdot \beta^{1-\alpha}}{\alpha-1} = \frac{\alpha\beta}{\alpha-1}.$$

Converge para $\alpha > 1$. **Resumo:** $E(X) = \alpha\beta/(\alpha-1)$.

## Passo 2: $E(X^2)$

$$E(X^2) = \alpha\beta^\alpha \int_\beta^\infty x^{-\alpha+1}dx = \frac{\alpha\beta^2}{\alpha-2}, \quad \alpha > 2.$$

## Passo 3: $\text{Var}(X)$

$$\text{Var}(X) = \frac{\alpha\beta^2}{\alpha-2} - \frac{\alpha^2\beta^2}{(\alpha-1)^2} = \alpha\beta^2\left[\frac{1}{\alpha-2} - \frac{\alpha}{(\alpha-1)^2}\right] = \frac{\alpha\beta^2}{(\alpha-1)^2(\alpha-2)}.$$
