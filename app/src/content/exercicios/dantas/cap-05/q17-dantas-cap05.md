---
id: "dantas-cap05-q17"
titulo: "Tempo Ótimo de Inspeção com Custos Assimétricos"
topicos: ["03-modelos-continuos"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["esperanca"]
referencia: "Dantas, Cap. 5, Q. 17"
---

## Enunciado

Máquina com tempo de falha $X \sim \text{Exp}(1/10)$. Se inspeciona antes da falha (em $t < X$): custo $B$. Se após a falha ($t > X$): custo $C$ por hora de inatividade $(t - X)$. Determine o tempo $t^*$ que minimiza o custo esperado.

## Passo 1: Custo esperado como função de $t$

$$E[\text{custo}(t)] = B \cdot P(X > t) + C \cdot E[t - X \mid X < t] \cdot P(X < t).$$

$$E[t - X \mid X < t] = t - E[X \mid X < t].$$

Para $X \sim \text{Exp}(1/10)$:

$$E[X \mid X < t] = \frac{\int_0^t x \cdot \frac{1}{10}e^{-x/10}dx}{1 - e^{-t/10}} = 10 - \frac{t + 10}{e^{t/10} - 1} \cdot \frac{1}{1}...$$

Mais diretamente:

$$E[(t-X)\mathbf{1}_{X<t}] = \int_0^t (t-x)\frac{1}{10}e^{-x/10}dx = t(1-e^{-t/10}) - 10(1-e^{-t/10}) + te^{-t/10}$$
$$= (t-10)(1-e^{-t/10}) + te^{-t/10} - te^{-t/10}$$

Calculando diretamente por partes:
$$\int_0^t(t-x)\frac{1}{10}e^{-x/10}dx = t(1-e^{-t/10}) - \left[10 - (t+10)e^{-t/10}\right] = -10 + 10e^{-t/10} + te^{-t/10}.$$

Portanto:

$$E[\text{custo}(t)] = Be^{-t/10} + C\!\left[-10 + (t+10)e^{-t/10}\right].$$

## Passo 2: Minimizar

$$\frac{d}{dt}E[\text{custo}] = -\frac{B}{10}e^{-t/10} + C\!\left[1 - \frac{t+10}{10}e^{-t/10}\right] = 0.$$

$$C = e^{-t/10}\!\left[\frac{B}{10} + \frac{C(t+10)}{10}\right] \implies e^{t/10} = \frac{B + C(t+10)}{10C}.$$

Esta equação transcendental em $t^*$ não tem solução fechada em geral. Para $B/C$ pequeno (custo de inspeção prematura pequeno), $t^*$ tende a ser pequeno.

**Resumo:** $t^*$ satisfaz $e^{t^*/10} = [B + C(t^*+10)]/(10C)$, resolvida numericamente.
