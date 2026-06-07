---
id: "dantas-cap02-q01"
titulo: "Distribuicao de Probabilidade Discreta Empirica"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "baixa"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "esperanca", "variancia"]
referencia: "Dantas, Cap. 2, Q. 1"
---

## Enunciado
Considere uma variável aleatória discreta $T$ cuja distribuição de probabilidade é apresentada a seguir:

| Valores de $T$ | 2    | 3    | 4    | 5    | 6    | 7    |
|----------------|------|------|------|------|------|------|
| Probabilidades | 1/10 | 1/10 | 4/10 | 2/10 | 1/10 | 1/10 |

Determine:
(a) $P(T \ge 6)$ ;
(b) $P(|T-4| > 2)$;
(c) $P(T \text{ ser um número primo})$.

## Solução

A soma das probabilidades da tabela é: $\frac{1+1+4+2+1+1}{10} = \frac{10}{10} = 1$. A distribuição está correta.

- **(a) $P(T \ge 6)$:**
Consiste nos valores $T = 6$ e $T = 7$.
$$ P(T \ge 6) = P(T=6) + P(T=7) = \frac{1}{10} + \frac{1}{10} = \frac{2}{10} = \frac{1}{5} = 0,2 $$

- **(b) $P(|T-4| > 2)$:**
Vamos resolver a inequação modular:
$$ |T-4| > 2 \iff T - 4 > 2 \quad \text{ou} \quad T - 4 < -2 $$
$$ T > 6 \quad \text{ou} \quad T < 2 $$
Dentre os valores possíveis para $T$ (de 2 a 7), não existe valor menor que 2. O único valor que é estritamente maior que 6 é $T=7$.
$$ P(|T-4| > 2) = P(T=7) = \frac{1}{10} = 0,1 $$

- **(c) $P(T \text{ ser um número primo})$:**
Os números primos no espaço amostral $\{2, 3, 4, 5, 6, 7\}$ são $2, 3, 5$ e $7$.
$$ P(\text{Primo}) = P(T=2) + P(T=3) + P(T=5) + P(T=7) $$
$$ P(\text{Primo}) = \frac{1}{10} + \frac{1}{10} + \frac{2}{10} + \frac{1}{10} = \frac{5}{10} = \frac{1}{2} = 0,5 $$
