---
id: "lista02-q38-distribuio-de-x"
titulo: "Distribuição de X²"
topicos: ["funcao-de-variavel-aleatoria"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Seja $X \sim N(0, 1)$. Seja $Y=X^2$. a) Determine a FDP de Y. b) Calcule E(Y) e Var(Y).

## Solução

## a) FDP de Y

$F_Y(y) = P(Y \le y) = P(X^2 \le y) = P(-\sqrt{y} \le X \le \sqrt{y}) = \Phi(\sqrt{y}) - \Phi(-\sqrt{y}) = 2\Phi(\sqrt{y}) - 1$.<br>$f_Y(y) = F_Y'(y) = 2\phi(\sqrt{y}) \frac{1}{2\sqrt{y}} = 2 \frac{1}{\sqrt{2\pi}} e^{-(\sqrt{y})^2/2} \frac{1}{2\sqrt{y}} = \frac{1}{\sqrt{2\pi}} y^{-1/2} e^{-y/2} $.<br>Esta é a FDP da Qui-quadrado com 1 grau de liberdade, $\chi^2(1)$.

## b) Média e Variância

$E[Y] = E[X^2] = Var(X) + (E[X])^2 = 1 + 0^2 = 1$.<br>$Var(Y) = Var(X^2) = E[X^4] - (E[X^2])^2$. O 4º momento de uma $N(0,1)$ é 3. $Var(Y) = 3 - 1^2 = 2$.
