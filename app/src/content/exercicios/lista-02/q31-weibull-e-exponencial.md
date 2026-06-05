---
id: "lista02-q31-weibull-e-exponencial"
titulo: "Weibull e Exponencial"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Mostre que se $X \sim Weibull(\alpha, \beta)$ então $Y=(\frac{X}{\alpha})^{\beta} \sim Exp(1)$, e vice-versa.

## Solução

FDP de Weibull: $f_X(x) = \frac{\beta}{\alpha}(\frac{x}{\alpha})^{\beta-1}e^{-(\frac{x}{\alpha})^eta}$.<br>Usamos o método da transformação. Seja $y = g(x) = (x/\alpha)^eta$. A inversa é $x = g^{-1}(y) = \alpha y^{1/\beta}$.<br>A derivada da inversa é $\frac{dx}{dy} = \frac{\alpha}{\beta} y^{\frac{1}{\beta}-1}$.<br>$f_Y(y) = f_X(g^{-1}(y)) |\frac{dx}{dy}|$.<br>$f_Y(y) = \frac{\beta}{\alpha}(\frac{\alpha y^{1/\beta}}{\alpha})^{\beta-1}e^{-y} \cdot |\frac{\alpha}{\beta} y^{\frac{1}{\beta}-1}|$<br>$ = \frac{\beta}{\alpha}(y^{\frac{\beta-1}{\beta}}) e^{-y} \frac{\alpha}{\beta} y^{\frac{1-\beta}{\beta}} = y^{\frac{\beta-1}{\beta} + \frac{1-\beta}{\beta}} e^{-y} = y^0 e^{-y} = e^{-y}$.<br>Esta é a FDP de uma $Exp(1)$.
