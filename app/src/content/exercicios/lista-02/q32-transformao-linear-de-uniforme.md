---
id: "lista02-q32-transformao-linear-de-uniforme"
titulo: "Transformação Linear de Uniforme"
topicos: ["funcao-de-variavel-aleatoria", "modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["metodo-fda"]
---

## Enunciado

Se $X \sim U(a, b)$, determine $\alpha, \beta$ tais que $Y=\alpha X+\beta$ seja $U(0, 1)$.

## Solução

Queremos mapear o intervalo $[a, b]$ para $[0, 1]$.<br>Quando $X=a$, queremos $Y=0 \implies \alpha a + \beta = 0$.<br>Quando $X=b$, queremos $Y=1 \implies \alpha b + \beta = 1$.<br>Subtraindo a primeira equação da segunda: $\alpha(b-a) = 1 \implies \alpha = \frac{1}{b-a}$.<br>Substituindo $\alpha$ na primeira: $\frac{a}{b-a} + \beta = 0 \implies \beta = -\frac{a}{b-a}$.<br>A transformação é $Y = \frac{1}{b-a}X - \frac{a}{b-a} = \frac{X-a}{b-a}$.
