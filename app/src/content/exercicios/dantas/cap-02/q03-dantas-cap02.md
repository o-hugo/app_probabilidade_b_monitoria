---
id: "q03-dantas-cap02"
titulo: "Questão 3"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Suponha que uma variável aleatória discreta tenha a seguinte distribuição de probabilidade: $P[X=x] = cx$ para $x \in \{0, 1, \dots, N\}$ e zero fora desse conjunto. Determine:
(a) O valor da constante $c$ quando $N=4$;
(b) O valor de $c$ para um valor qualquer de $N$;
(c) $P(X \leq a), \, a \leq N$;
(d) $P(X \text{ ser par})$.

## Solução

- **(b) O valor de $c$ para um valor qualquer de $N$:**
(Vamos resolver primeiro o caso geral, que torna a letra A trivial).
A soma de todas as probabilidades do espaço amostral deve ser 1.
$$ \sum_{x=0}^{N} P(X=x) = 1 \implies \sum_{x=0}^{N} cx = 1 $$
$$ c \sum_{x=1}^{N} x = 1 $$
A soma dos $N$ primeiros números naturais é dada pela fórmula da P.A.: $\frac{N(N+1)}{2}$.
$$ c \cdot \frac{N(N+1)}{2} = 1 \implies c = \frac{2}{N(N+1)} $$

- **(a) O valor da constante $c$ quando $N=4$:**
Substituindo $N=4$ na fórmula encontrada acima:
$$ c = \frac{2}{4(4+1)} = \frac{2}{20} = \frac{1}{10} = 0,1 $$

- **(c) $P(X \leq a)$, para $a \leq N$:**
$$ P(X \le a) = \sum_{x=0}^{a} P(X=x) = \sum_{x=1}^{a} cx = c \frac{a(a+1)}{2} $$
Substituindo $c$:
$$ P(X \le a) = \frac{2}{N(N+1)} \cdot \frac{a(a+1)}{2} = \frac{a(a+1)}{N(N+1)} $$

- **(d) $P(X \text{ ser par})$:**
Precisamos somar as probabilidades dos valores pares de $x$, ou seja, $x = 2k$.
A soma dos pares no conjunto $\{1, \dots, N\}$ varia conforme a paridade de $N$:

Se $N$ é **par**, digamos $N = 2m$:
$$ S_{\text{pares}} = 2 + 4 + \dots + 2m = 2(1 + 2 + \dots + m) = 2 \cdot \frac{m(m+1)}{2} = m(m+1) $$
Substituindo $m = \frac{N}{2}$:
$$ S_{\text{pares}} = \frac{N}{2} \left(\frac{N}{2} + 1\right) = \frac{N(N+2)}{4} $$
A probabilidade será:
$$ P(\text{Par}) = c \cdot S_{\text{pares}} = \frac{2}{N(N+1)} \cdot \frac{N(N+2)}{4} = \frac{N+2}{2(N+1)} $$

Se $N$ é **ímpar**, digamos $N = 2m + 1$:
O maior par é $2m = N-1$.
$$ S_{\text{pares}} = 2 + 4 + \dots + 2m = m(m+1) $$
Substituindo $m = \frac{N-1}{2}$:
$$ S_{\text{pares}} = \frac{N-1}{2} \left(\frac{N-1}{2} + 1\right) = \frac{N-1}{2} \cdot \frac{N+1}{2} = \frac{(N-1)(N+1)}{4} $$
A probabilidade será:
$$ P(\text{Par}) = c \cdot S_{\text{pares}} = \frac{2}{N(N+1)} \cdot \frac{(N-1)(N+1)}{4} = \frac{N-1}{2N} $$
