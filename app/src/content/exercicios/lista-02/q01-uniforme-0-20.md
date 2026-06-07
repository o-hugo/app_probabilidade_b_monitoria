---
id: "lista02-q01-uniforme-0-20"
titulo: "Distribuicao Uniforme (0, 20)"
topicos: ["modelos-continuos"]
dificuldade: "baixa"
origem: "lista-02"
metodo: "integral-direta"
solucao_verificada: true
tags: ["probabilidade"]
---

## Enunciado

Se X e uniformemente distribuida no intervalo (0, 20), calcule a probabilidade de:

a) $X < 3$

b) $X > 12$

c) $4 < X < 11$

d) $|X - 3| < 4$

## Passo 1: Identificar a distribuicao e a FDP

Para $X \sim U(a, b)$, a Funcao de Densidade de Probabilidade (FDP) e constante:

$$f(x) = \frac{1}{b - a} \quad \text{para } a < x < b$$

Aqui, $a = 0$ e $b = 20$, portanto:

$$f(x) = \frac{1}{20} \quad \text{para } 0 < x < 20$$

A probabilidade $P(c < X < d)$ e a integral $\int_c^d f(x)\,dx$, que para a uniforme se reduz a formula da area de um retangulo:

$$P(c < X < d) = (d - c) \times \frac{1}{b - a} = \frac{d - c}{b - a}$$

## Passo 2: Calcular cada item

### a) $P(X < 3)$

Equivale a $P(0 < X < 3)$:

$$P(X < 3) = \int_0^3 \frac{1}{20}\,dx = \frac{3 - 0}{20} = \frac{3}{20} = 0.15$$

### b) $P(X > 12)$

Equivale a $P(12 < X < 20)$:

$$P(X > 12) = \int_{12}^{20} \frac{1}{20}\,dx = \frac{20 - 12}{20} = \frac{8}{20} = 0.40$$

### c) $P(4 < X < 11)$

$$P(4 < X < 11) = \int_4^{11} \frac{1}{20}\,dx = \frac{11 - 4}{20} = \frac{7}{20} = 0.35$$

### d) $P(|X - 3| < 4)$

**Resolver a inequacao:** $|X - 3| < 4$ implica $-4 < X - 3 < 4$.

**Isolar X:** Somando 3, obtemos $-1 < X < 7$.

**Considerar o dominio de X:** A intersecao de $(-1, 7)$ com $(0, 20)$ e $(0, 7)$.

$$P(0 < X < 7) = \int_0^7 \frac{1}{20}\,dx = \frac{7 - 0}{20} = \frac{7}{20} = 0.35$$
