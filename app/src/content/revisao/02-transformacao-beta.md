---
id: "revisao-transformacao-beta"
titulo: "2. Transformação da Distribuição Beta"
topicos: ["funcao-de-variavel-aleatoria", "beta"]
ordem: 2
---

## Transformação da Distribuição Beta

Se $X \sim \text{Beta}(\alpha,\beta)$, obter a FDP de $Y = \frac{\beta X}{\alpha(1-X)}$.

1. **Inversa:** $X = \frac{\alpha Y}{\beta + \alpha Y}$.
2. **Derivada:** $\frac{dX}{dY} = \frac{\alpha\beta}{(\beta+\alpha Y)^2}$ (sempre positiva).
3. **FDP de Y:** $f_Y(y) = f_X(g^{-1}(y)) \cdot \frac{dX}{dY}$. 

Substituímos $x$ e $1-x = \frac{\beta}{\beta+\alpha Y}$ na FDP da Beta:

$f_Y(y) = \frac{1}{B(\alpha, \beta)} \left(\frac{\alpha Y}{\beta+\alpha Y}\right)^{\alpha-1} \left(\frac{\beta}{\beta+\alpha Y}\right)^{\beta-1} \cdot \frac{\alpha\beta}{(\beta+\alpha Y)^2} = \frac{\alpha^\alpha \beta^\beta}{B(\alpha,\beta)} \frac{y^{\alpha-1}}{(\beta+\alpha y)^{\alpha+\beta}}$.
