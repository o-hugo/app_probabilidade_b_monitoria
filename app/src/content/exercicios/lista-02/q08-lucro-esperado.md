---
id: "lista02-q08-lucro-esperado"
titulo: "Lucro Esperado"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "lista-02"
solucao_verificada: false
tags: ["esperanca"]
---

## Enunciado

Vida de componente $X \sim f(x)=e^{-x}, x>0$. Custo R$2, Venda R$5. Devolução se $X \le 0.9$. Qual o lucro esperado por item?

## Solução

A FDP $f(x)=e^{-x}$ é de uma $Exp(1)$.<br>O lucro $L$ é uma variável aleatória:<br>$ L = +3 $ (R$5 venda - R$2 custo) se $X > 0.9$.<br>$ L = -2 $ (custo perdido) se $X \le 0.9$.<br>O lucro esperado é $E[L] = (3) \cdot P(X > 0.9) + (-2) \cdot P(X \le 0.9)$.<br>Calculamos a probabilidade de devolução: $p = P(X \le 0.9) = 1 - e^{-1 \times 0.9} = 1 - e^{-0.9} \approx 0.5934$.<br>$E[L] = 3(1-p) - 2p = 3(0.4066) - 2(0.5934) = 1.2198 - 1.1868 = 0.033$.<br>O lucro esperado é de R$ 0,033 por item.
