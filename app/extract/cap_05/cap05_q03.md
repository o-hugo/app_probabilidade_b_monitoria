---
id: "dantas-cap05-q03"
titulo: "FDA e Probabilidades da Uniforme em (-3,7)"
topicos: ["03-modelos-continuos"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["fda", "probabilidade"]
referencia: "Dantas, Cap. 5, Q. 3"
---

## Enunciado

$X \sim U(-3, 7)$. Determine: (a) a função de distribuição de $X$; (b) $P\{|X-1| \le 2\}$; (c) $P\{|X| > 3\}$.

## Solução

**(a)** $f(x) = 1/10$ para $-3 < x < 7$. A FDA é:

$$F(x) = \begin{cases} 0 & x \le -3 \\ \dfrac{x+3}{10} & -3 < x < 7 \\ 1 & x \ge 7 \end{cases}$$

**(b)** $|X-1| \le 2 \Leftrightarrow -1 \le X \le 3$:
$$P = \frac{3-(-1)}{10} = \frac{4}{10} = 0{,}4.$$

**(c)** $|X| > 3 \Leftrightarrow X < -3$ ou $X > 3$. Como $X \ge -3$ sempre: $P = P\{X > 3\} = (7-3)/10 = 4/10 = 0{,}4$.
