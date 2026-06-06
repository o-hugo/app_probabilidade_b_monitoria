---
id: "q33-dantas-cap01"
titulo: "Questão 33"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Um dispositivo eletrônico é formado por três partes. Cada parte tem probabilidade de 0,9 de funcionar bem e 0,1 de falhar. O funcionamento de cada parte não depende das demais. O dispositivo falha se duas ou mais falham. Calcule a probabilidade de falha do dispositivo.

## Solução

Seja $X$ a variável aleatória que representa o número de partes que falharam no dispositivo.
Como o funcionamento de cada parte é independente, $X$ segue uma distribuição binomial: $X \sim \text{Binomial}(n=3, p=0,1)$, onde $p$ é a probabilidade de falha de uma única peça.

O dispositivo falhará como um todo se duas ou mais partes falharem ($X \ge 2$).
$$ P(X \ge 2) = P(X = 2) + P(X = 3) $$

Usando a fórmula da probabilidade binomial $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$:

1. **Probabilidade de exatamente 2 peças falharem:**
$$ P(X = 2) = \binom{3}{2} (0,1)^2 (0,9)^{3-2} $$
$$ P(X = 2) = 3 \times 0,01 \times 0,9 = 0,027 $$

2. **Probabilidade de exatamente 3 peças falharem:**
$$ P(X = 3) = \binom{3}{3} (0,1)^3 (0,9)^{3-3} $$
$$ P(X = 3) = 1 \times 0,001 \times 1 = 0,001 $$

Somando ambas:
$$ P(\text{Falha do dispositivo}) = 0,027 + 0,001 = 0,028 $$

Portanto, a probabilidade do dispositivo falhar é de **2,8%** (0,028).
