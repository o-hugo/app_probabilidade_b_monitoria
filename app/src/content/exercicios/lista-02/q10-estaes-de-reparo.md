---
id: "lista02-q10-estaes-de-reparo"
titulo: "Estações de Reparo"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["esperanca"]
---

## Enunciado

Ônibus quebra em $X \sim U(0, 100)$. Estações atuais em {0, 50, 100}. Sugestão: {25, 50, 75}. Qual é melhor?

## Solução

O critério é minimizar a distância esperada $E[D]$ à estação mais próxima.

## Configuração Atual: {0, 50, 100}

A distância $D_{atual}(X)$ é $\min(|X-0|, |X-50|, |X-100|)$.<br>$E[D] = \int_0^{100} D(x)f(x)dx = \frac{1}{100} \left[ \int_0^{25} x dx + \int_{25}^{50} (50-x) dx + \int_{50}^{75} (x-50) dx + \int_{75}^{100} (100-x) dx \right]$<br>$= \frac{1}{100} [\frac{25^2}{2} + 312.5 + 312.5 + \frac{25^2}{2}] = \frac{1250}{100} = 12.5 \text{ km}$

## Configuração Sugerida: {25, 50, 75}

A distância $D_{sug}(X)$ é $\min(|X-25|, |X-50|, |X-75|)$.<br>$E[D] = \frac{1}{100} \left[ \int_0^{37.5} |x-25| dx + \int_{37.5}^{62.5} |x-50| dx + ... \right]$<br>Por simetria, podemos calcular a distância esperada para um segmento de 25km (e.g., [0,25]) até sua estação mais próxima (25) e multiplicar por 4.<br>$E[D] = 4 \times \int_0^{25} (25-x) \frac{dx}{100} = \frac{4}{100} [25x - \frac{x^2}{2}]_0^{25} = \frac{4}{100} (312.5) = 12.5 \text{ km}$<br>**Conclusão:** As duas configurações têm a mesma eficiência em termos de distância esperada.
