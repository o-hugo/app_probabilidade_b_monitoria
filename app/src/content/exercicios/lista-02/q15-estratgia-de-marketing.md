---
id: "lista02-q15-estratgia-de-marketing"
titulo: "Estratégia de Marketing"
topicos: ["distribuicao-normal"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Analisar lucro/prejuízo de carros tipo A e B, com tempos de defeito normais. Qual incentivar?

## Solução

## Carro Tipo A

$T_A \sim N(\mu=9, \sigma^2=4)$. Restituição se $T_A < 6$. Lucro: +1000, Prejuízo: -3000.<br>Prob. de restituição: $p_A = P(T_A < 6) = P(Z < \frac{6-9}{2}) = P(Z < -1.5) \approx 0.0668$.<br>$E[Lucro_A] = 1000(1-p_A) + (-3000)(p_A) = 1000(0.9332) - 3000(0.0668) = 732.80$

## Carro Tipo B

$T_B \sim N(\mu=12, \sigma^2=9)$. Restituição se $T_B < 6$. Lucro: +2000, Prejuízo: -8000.<br>Prob. de restituição: $p_B = P(T_B < 6) = P(Z < \frac{6-12}{3}) = P(Z < -2) \approx 0.0228$.<br>$E[Lucro_B] = 2000(1-p_B) + (-8000)(p_B) = 2000(0.9772) - 8000(0.0228) = 1772.00$<br>**Conclusão:** Incentivar as vendas do tipo B, pois o lucro esperado é significativamente maior.
