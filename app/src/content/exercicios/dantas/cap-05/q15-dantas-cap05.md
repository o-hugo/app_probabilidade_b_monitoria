---
id: "dantas-cap05-q15"
titulo: "Estratégia de Marketing — Lucro Esperado com Garantia Normal"
topicos: ["04-distribuicao-normal"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "padronizacao-z"]
referencia: "Dantas, Cap. 5, Q. 15"
---

## Enunciado

Tempo para defeito grave: tipo A $\sim N(\mu=9, \sigma^2=4)$ meses, tipo B $\sim N(\mu=12, \sigma^2=9)$ meses. Garantia de 6 meses. Lucro sem devolução: A=R\$1.000, B=R\$2.000. Prejuízo com devolução: A=R\$3.000, B=R\$8.000. Qual tipo incentivar?

## Passo 1: Probabilidade de devolução (defeito em 6 meses)

**Tipo A:** $P(X_A \le 6) = P\!\left(Z \le \frac{6-9}{2}\right) = P(Z \le -1{,}5) = 1 - \Phi(1{,}5) \approx 0{,}0668$.

**Tipo B:** $P(X_B \le 6) = P\!\left(Z \le \frac{6-12}{3}\right) = P(Z \le -2) = 1 - \Phi(2) \approx 0{,}0228$.

**Resumo:** Tipo B tem menor risco de devolução.

## Passo 2: Lucro esperado por unidade

**Tipo A:**
$$E[L_A] = 1000(1 - 0{,}0668) + (-3000)(0{,}0668) = 933{,}2 - 200{,}4 = 732{,}8 \text{ reais}.$$

**Tipo B:**
$$E[L_B] = 2000(1 - 0{,}0228) + (-8000)(0{,}0228) = 1954{,}4 - 182{,}4 = 1772 \text{ reais}.$$

## Passo 3: Decisão

$E[L_B] \approx \text{R\$}1.772 > E[L_A] \approx \text{R\$}733$. **Incentivaria as vendas do tipo B** — apesar do prejuízo maior em caso de devolução, a probabilidade de defeito no prazo de garantia é muito menor, resultando em lucro esperado 2,4 vezes maior.
