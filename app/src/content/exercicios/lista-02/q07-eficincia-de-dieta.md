---
id: "lista02-q07-eficincia-de-dieta"
titulo: "Eficiência de Dieta"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
---

## Enunciado

100 pessoas fazem dieta. Se a dieta não tem efeito, P(colesterol menor)=1/2. Qual a P(nutricionista endossar a dieta), ou seja, P(≥65 pessoas melhorarem)?

## Solução

Seja X o número de pessoas que melhoram. Se não há efeito, $X \sim B(n=100, p=0.5)$. Queremos $P(X \ge 65)$.

**Aproximação Normal:** $\mu = np = 50$, $\sigma = \sqrt{np(1-p)} = 5$. As condições são satisfeitas.<br>**Correção de Continuidade:** Para $P(X \ge k)$, aproximamos por $P(X_{norm} > k-0.5)$.<br>$P(X > 64.5) = P(Z > \frac{64.5 - 50}{5}) = P(Z > 2.9)$<br>$= 1 - \Phi(2.9) \approx 1 - 0.9981 = 0.0019$.<br>A probabilidade de endossar a dieta por acaso é muito baixa (0.19%).
