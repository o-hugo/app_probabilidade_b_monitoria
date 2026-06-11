---
id: "dantas-cap05-q02"
titulo: "Probabilidades com Distribuição Normal N(3,9)"
topicos: ["04-distribuicao-normal"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "padronizacao-z"]
referencia: "Dantas, Cap. 5, Q. 2"
---

## Enunciado

Se $X$ é uma variável aleatória normal com $\mu = 3$ e $\sigma^2 = 9$ ($\sigma = 3$), determine: (a) $P\{2 < X < 5\}$; (b) $P\{X > 0\}$; (c) $P\{|X-3| > 6\}$.

## Solução

Padronizando $Z = (X-3)/3$:

**(a)**
$$P\{2 < X < 5\} = P\!\left\{\frac{-1}{3} < Z < \frac{2}{3}\right\} = \Phi(0{,}67) - \Phi(-0{,}33) \approx 0{,}7486 - 0{,}3707 = 0{,}3779.$$

**(b)**
$$P\{X > 0\} = P\{Z > -1\} = \Phi(1) \approx 0{,}8413.$$

**(c)** $|X-3| > 6 \Leftrightarrow |Z| > 2$:
$$P\{|Z| > 2\} = 2(1 - \Phi(2)) \approx 2(0{,}0228) = 0{,}0456.$$
