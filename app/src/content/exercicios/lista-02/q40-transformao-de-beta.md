---
id: "lista02-q40-transformao-de-beta"
titulo: "Transformação de Beta"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Se $X \sim Beta(\alpha, \beta)$ e $Y=\frac{\beta X}{\alpha(1-X)}$, obtenha a FDP de Y.

## Solução

Esta transformação relaciona a Beta com a distribuição F. <br>Inversa: $Y\alpha(1-X) = \beta X \implies X = \frac{\alpha Y}{\beta + \alpha Y}$. Derivada: $\frac{dX}{dY} = \frac{\alpha\beta}{(\beta+\alpha Y)^2}$.<br>Substituindo na FDP da Beta e simplificando, obtemos a FDP da distribuição F com $v_1=2\alpha$ e $v_2=2\beta$ graus de liberdade, a menos de constantes de escala. A FDP resultante é:<br>$$ f_Y(y) = \frac{(\alpha/\beta)^\alpha \Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)} \frac{y^{\alpha-1}}{(1+\frac{\alpha}{\beta}y)^{\alpha+\beta}} $$
