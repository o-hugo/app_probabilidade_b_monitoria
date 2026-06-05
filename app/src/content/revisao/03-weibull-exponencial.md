---
id: "revisao-weibull-exponencial"
titulo: "3. Relação Weibull-Exponencial"
topicos: ["modelos-continuos", "weibull", "exponencial"]
ordem: 3
---

## Relação Weibull-Exponencial

Se $X \sim \text{Weibull}(\alpha,\beta)$ e $Y=(X/\alpha)^\beta$, mostrar que Y é $Exp(1)$.

Usamos o método da FDA: $F_Y(y) = P(Y \le y) = P\left((\frac{X}{\alpha})^\beta \le y\right)$.

Isolando X: $P\left(\frac{X}{\alpha} \le y^{1/\beta}\right) = P(X \le \alpha y^{1/\beta})$. Isso é a FDA de X, $F_X$, avaliada em $\alpha y^{1/\beta}$.

A FDA da Weibull é $F_X(x) = 1-e^{-(x/\alpha)^\beta}$. Substituindo:

$F_Y(y) = 1 - \exp\left\{-\left(\frac{\alpha y^{1/\beta}}{\alpha}\right)^\beta\right\} = 1 - \exp\left\{-(y^{1/\beta})^\beta\right\} = 1 - e^{-y}$.

Esta é a FDA da distribuição Exponencial com $\lambda=1$.
