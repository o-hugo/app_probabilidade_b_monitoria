---
id: "dantas-cap05-q40"
titulo: "Transformação Beta → Distribuição F-Snedecor"
topicos: ["05-funcao-de-variavel-aleatoria"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["fdp-valida", "metodo-jacobiano"]
referencia: "Dantas, Cap. 5, Q. 40"
---

## Enunciado

$X \sim \text{Beta}(\alpha,\beta)$. $Y = \dfrac{\beta X}{\alpha(1-X)}$. Obtenha $f_Y(y)$.

## Passo 1: Mudança de variável

Da relação $y = \frac{\beta x}{\alpha(1-x)}$, resolvendo para $x$:

$$x = \frac{\alpha y}{\beta + \alpha y}, \qquad \frac{dx}{dy} = \frac{\alpha\beta}{(\beta + \alpha y)^2}.$$

**Resumo:** $x = \alpha y/(\beta + \alpha y)$ e Jacobiano $= \alpha\beta/(\beta+\alpha y)^2$.

## Passo 2: Densidade de Y

$$f_Y(y) = f_X(x(y))\left|\frac{dx}{dy}\right| = \frac{1}{B(\alpha,\beta)}\left(\frac{\alpha y}{\beta+\alpha y}\right)^{\alpha-1}\!\!\left(\frac{\beta}{\beta+\alpha y}\right)^{\beta-1}\!\cdot\frac{\alpha\beta}{(\beta+\alpha y)^2}.$$

Simplificando:

$$f_Y(y) = \frac{1}{B(\alpha,\beta)}\cdot\frac{\alpha^\alpha\beta^\beta\, y^{\alpha-1}}{(\beta+\alpha y)^{\alpha+\beta}}, \quad y > 0.$$

Esta é a densidade da **distribuição F-Snedecor** com $2\alpha$ e $2\beta$ graus de liberdade (após reparametrização $\nu_1 = 2\alpha$, $\nu_2 = 2\beta$).
