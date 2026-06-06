---
id: "q32-dantas-cap01"
titulo: "Questão 32"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Uma moeda é lançada até se obter a primeira cara. Determine: 
(a) a probabilidade de que isto ocorra em um lançamento de número par; 
(b) a probabilidade de que isto ocorra em um lançamentos de número ímpar.

## Solução

A probabilidade de sair "cara" (C) em um lançamento é $p = \frac{1}{2}$ e a probabilidade de sair "coroa" (K) é $q = \frac{1}{2}$.
A probabilidade de que a primeira cara ocorra exatamente no $n$-ésimo lançamento é dada pela distribuição geométrica, o que implica em $n-1$ coroas seguidas de 1 cara:
$$ P(X = n) = q^{n-1}p = \left(\frac{1}{2}\right)^{n-1} \left(\frac{1}{2}\right) = \left(\frac{1}{2}\right)^n $$

- **(a) Ocorrer em um lançamento de número par:**
Queremos a soma das probabilidades para $n \in \{2, 4, 6, 8, \dots\}$.
Podemos expressar um número par genérico como $n = 2k$, para $k = 1, 2, 3, \dots$
$$ P(\text{par}) = \sum_{k=1}^{\infty} \left(\frac{1}{2}\right)^{2k} = \sum_{k=1}^{\infty} \left(\frac{1}{4}\right)^k $$
Temos uma soma de progressão geométrica (P.G.) infinita, cujo primeiro termo é $a_1 = \frac{1}{4}$ e a razão é $q = \frac{1}{4}$.
$$ S = \frac{a_1}{1 - q} = \frac{1/4}{1 - 1/4} = \frac{1/4}{3/4} = \frac{1}{3} \approx 0,3333 $$

- **(b) Ocorrer em um lançamento de número ímpar:**
Queremos a soma das probabilidades para $n \in \{1, 3, 5, 7, \dots\}$.
Podemos expressar um número ímpar genérico como $n = 2k-1$, para $k = 1, 2, 3, \dots$
$$ P(\text{ímpar}) = \sum_{k=1}^{\infty} \left(\frac{1}{2}\right)^{2k-1} = \sum_{k=1}^{\infty} 2 \left(\frac{1}{2}\right)^{2k} = \sum_{k=1}^{\infty} 2 \left(\frac{1}{4}\right)^k = 2 \times P(\text{par}) $$
$$ P(\text{ímpar}) = 2 \times \frac{1}{3} = \frac{2}{3} \approx 0,6667 $$
(Podemos confirmar também notando que P(par) + P(ímpar) = $\frac{1}{3} + \frac{2}{3} = 1$).
