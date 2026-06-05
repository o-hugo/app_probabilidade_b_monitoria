---
id: "lista02-q34-fdp-de-x"
titulo: "FDP de |X|"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Se $X \sim U(-1, 1)$, determine a FDP de $Y=|X|$.

## Solução

O intervalo de Y é $[0, 1)$. Para $y \in [0,1)$, usamos o método da FDA:<br>$F_Y(y) = P(Y \le y) = P(|X| \le y) = P(-y \le X \le y)$.<br>Como $X \sim U(-1,1)$, a FDP é $f(x)=1/2$.<br>$P(-y \le X \le y) = \int_{-y}^y \frac{1}{2} dx = \frac{1}{2}[x]_{-y}^y = \frac{1}{2}(y - (-y)) = y$.<br>A FDA de Y é $F_Y(y) = y$, então a FDP é $f_Y(y) = F_Y'(y) = 1$. Logo, $Y \sim U(0,1)$.
