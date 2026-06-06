---
id: "lista02-q12-chuva-anual"
titulo: "Chuva Anual"
topicos: ["distribuicao-normal"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

Chuva anual é $N(40, 4^2)$. Qual a probabilidade de levar mais de 10 anos para se registrar uma chuva anual > 50?

## Solução

**Passo 1:** Probabilidade de sucesso em 1 ano. Sucesso = Chuva > 50.<br>$p = P(X > 50) = P(Z > \frac{50 - 40}{4}) = P(Z > 2.5) = 1 - \Phi(2.5) = 1 - 0.9938 = 0.0062$.

**Passo 2:** Probabilidade de mais de 10 anos até o 1º sucesso. Isso significa 10 falhas consecutivas. O número de anos $Y$ até o sucesso segue uma Geométrica.<br>$P(Y > 10) = (1-p)^{10} = (0.9938)^{10} \approx 0.9397$.
