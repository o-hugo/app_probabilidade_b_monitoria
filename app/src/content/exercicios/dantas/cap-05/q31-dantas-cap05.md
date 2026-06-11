---
id: "dantas-cap05-q31"
titulo: "Transformação Weibull → Exponencial"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["metodo-fda", "confiabilidade"]
referencia: "Dantas, Cap. 5, Q. 31"
---

## Enunciado

Mostre que se $X \sim \text{Weibull}(\alpha, \beta)$ com $f(x) = \frac{\beta}{\alpha}(x/\alpha)^{\beta-1}e^{-(x/\alpha)^\beta}$, $x>0$, então $Y = (X/\alpha)^\beta \sim \text{Exp}(1)$, e vice-versa.

## Solução

**Weibull → Exponencial:** Seja $Y = (X/\alpha)^\beta$. Como a função é monótona crescente:

$$F_Y(y) = P(Y \le y) = P\!\left(\frac{X}{\alpha} \le y^{1/\beta}\right) = F_X(\alpha y^{1/\beta}) = 1 - e^{-(\alpha y^{1/\beta}/\alpha)^\beta} = 1 - e^{-y}, \quad y>0.$$

Logo $Y \sim \text{Exp}(1)$. $\blacksquare$

**Exponencial → Weibull:** Se $Y \sim \text{Exp}(1)$, defina $X = \alpha Y^{1/\beta}$. Então:

$$F_X(x) = P(X \le x) = P\!\left(Y \le (x/\alpha)^\beta\right) = 1 - e^{-(x/\alpha)^\beta},$$

que é a FDA Weibull$(\alpha,\beta)$. $\blacksquare$
