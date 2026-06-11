---
id: "dantas-cap05-q08"
titulo: "Lucro Esperado com Garantia — Componente Exponencial"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "probabilidade"]
referencia: "Dantas, Cap. 5, Q. 8"
---

## Enunciado

Tempo de vida $X \sim \text{Exp}(1)$ (em milhares de horas). Custo de fabricação: R\$2,00; preço de venda: R\$5,00. Garantia total se $X \le 0{,}9$. Qual o lucro esperado por item?

## Passo 1: Eventos e lucros

- $X > 0{,}9$ (não há devolução): lucro $= 5 - 2 = 3$ reais.
- $X \le 0{,}9$ (devolução total): lucro $= -2$ reais (devolve 5 e pagou 2 para fabricar).

**Resumo:** Lucro é 3 com prob $P(X>0{,}9)$ e $-2$ com prob $P(X \le 0{,}9)$.

## Passo 2: Probabilidades

$$P(X \le 0{,}9) = 1 - e^{-0{,}9} \approx 0{,}5934.$$
$$P(X > 0{,}9) = e^{-0{,}9} \approx 0{,}4066.$$

## Passo 3: Lucro esperado

$$E[\text{lucro}] = 3 \cdot e^{-0{,}9} + (-2)(1 - e^{-0{,}9}) = 3e^{-0{,}9} - 2 + 2e^{-0{,}9} = 5e^{-0{,}9} - 2 \approx 5(0{,}4066) - 2 = 0{,}033 \text{ reais}.$$

**Resumo:** O lucro esperado é aproximadamente R\$0,03 por item — margens muito apertadas pela garantia.
