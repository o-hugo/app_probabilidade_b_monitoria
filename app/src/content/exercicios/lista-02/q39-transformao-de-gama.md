---
id: "lista02-q39-transformao-de-gama"
titulo: "Transformação de Gama"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Se $X \sim Gama(\alpha, \beta)$ e $Z=2\beta X$, qual a FDP de Z? E se $\alpha=1/2$?

## Solução

Transformação: $X = Z/(2\beta)$, $\frac{dX}{dZ} = 1/(2\beta)$. FDP de X: $f_X(x)=\frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$.<br>$f_Z(z) = f_X(\frac{z}{2\beta}) |\frac{dx}{dz}| = \frac{\beta^\alpha}{\Gamma(\alpha)} (\frac{z}{2\beta})^{\alpha-1} e^{-\beta (z/2\beta)} \frac{1}{2\beta}$.<br>$= \frac{1}{2^\alpha \Gamma(\alpha)} z^{\alpha-1}e^{-z/2} $. Esta é a FDP da Qui-quadrado com $k=2\alpha$ graus de liberdade.<br>Se $\alpha = 1/2$, Z tem distribuição $\chi^2(1)$.
