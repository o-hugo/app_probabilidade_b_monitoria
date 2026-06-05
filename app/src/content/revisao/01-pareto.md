---
id: "revisao-pareto"
titulo: "1. Distribuição de Pareto"
topicos: ["modelos-continuos", "pareto"]
ordem: 1
---

## Distribuição de Pareto

Dada a FDP $f(x) = \frac{\alpha\beta^\alpha}{x^{\alpha+1}}$ para $x \ge \beta$.

**a) Esperança $E(X)$ para $\alpha>1$:**

$E(X) = \int_\beta^\infty x \cdot \frac{\alpha\beta^\alpha}{x^{\alpha+1}} dx = \alpha\beta^\alpha \int_\beta^\infty x^{-\alpha} dx = \alpha\beta^\alpha \left[ \frac{x^{1-\alpha}}{1-\alpha} \right]_\beta^\infty$.

Para convergência, $1-\alpha < 0 \implies \alpha > 1$. Com isso, $\lim_{x\to\infty} x^{1-\alpha} = 0$.

$E(X) = \alpha\beta^\alpha \left( 0 - \frac{\beta^{1-\alpha}}{1-\alpha} \right) = \frac{\alpha\beta^\alpha \beta^{1-\alpha}}{\alpha-1} = \frac{\alpha\beta}{\alpha-1}$.

**b) Variância $Var(X)$ para $\alpha>2$:**

Primeiro, $E(X^2) = \int_\beta^\infty x^2 f(x) dx = \alpha\beta^\alpha \int_\beta^\infty x^{1-\alpha} dx$. Converge se $2-\alpha<0 \implies \alpha>2$.

$E(X^2) = \alpha\beta^\alpha \left[ \frac{x^{2-\alpha}}{2-\alpha} \right]_\beta^\infty = \alpha\beta^\alpha \left( \frac{-\beta^{2-\alpha}}{2-\alpha} \right) = \frac{\alpha\beta^2}{\alpha-2}$.

$Var(X) = E(X^2) - [E(X)]^2 = \frac{\alpha\beta^2}{\alpha-2} - \left(\frac{\alpha\beta}{\alpha-1}\right)^2 = \frac{\alpha\beta^2}{(\alpha-1)^2(\alpha-2)}$.
