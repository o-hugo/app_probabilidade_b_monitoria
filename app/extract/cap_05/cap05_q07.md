---
id: "dantas-cap05-q07"
titulo: "Aprovação de Dieta — Aproximação Normal para Binomial"
topicos: ["04-distribuicao-normal"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "tlc", "padronizacao-z"]
referencia: "Dantas, Cap. 5, Q. 7"
---

## Enunciado

100 pessoas são submetidas a uma dieta. O nutricionista endossa a dieta se pelo menos 65 pessoas apresentarem nível de colesterol menor. Se a dieta não tem efeito, cada pessoa melhora com probabilidade 1/2. Qual a probabilidade de o nutricionista endossar a dieta ineficaz?

## Passo 1: Modelo

$X \sim \text{Bin}(100, 1/2)$, $\mu = 50$, $\sigma = \sqrt{25} = 5$. Queremos $P(X \ge 65)$.

**Resumo:** $X \sim \text{Bin}(100, 0{,}5)$.

## Passo 2: Aproximação normal

$$P(X \ge 65) \approx P\!\left(Z \ge \frac{64{,}5 - 50}{5}\right) = P(Z \ge 2{,}9) = 1 - \Phi(2{,}9) \approx 1 - 0{,}9981 = 0{,}0019.$$

**Resumo:** Há apenas 0,19% de chance de endossar uma dieta sem efeito — o critério é bastante rigoroso.
