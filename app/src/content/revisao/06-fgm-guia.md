---
id: "revisao-fgm-guia"
titulo: "6. Guia: Como Usar a FGM"
topicos: ["funcao-geradora-momentos"]
ordem: 6
---

## Guia: Como Usar a Função Geradora de Momentos (FGM)

A FGM é uma ferramenta poderosa para encontrar os momentos (como a média e a variância) de uma distribuição.

1. **Primeiro, você deve encontrar a FGM.** A fórmula é $M_X(t) = E[e^{tX}]$. Para uma variável contínua, isso significa calcular a integral $\int_{-\infty}^{\infty} e^{tx} f(x) dx$.
2. **Segundo, para encontrar a média ($E[X]$), derive a FGM.** Calcule a primeira derivada em relação a 't': $M'_X(t) = \frac{d}{dt} M_X(t)$.
3. **Terceiro, substitua t=0 na primeira derivada.** O resultado é a média: $E[X] = M'_X(0)$.
4. **Quarto, para encontrar o segundo momento ($E[X^2]$), derive a FGM novamente.** Calcule a segunda derivada: $M''_X(t) = \frac{d^2}{dt^2} M_X(t)$.
5. **Quinto, substitua t=0 na segunda derivada.** O resultado é o segundo momento: $E[X^2] = M''_X(0)$. A partir daí, a variância pode ser calculada com $Var(X) = E[X^2] - (E[X])^2$.

**Regra Geral:** O k-ésimo momento é $E[X^k] = \frac{d^k}{dt^k} M_X(t) \Big|_{t=0}$.
