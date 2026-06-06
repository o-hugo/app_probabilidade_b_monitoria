---
id: "q02-dantas-cap02"
titulo: "Questão 2"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Seja $X$ uma variável aleatória discreta com distribuição de probabilidade dada por $P[X=x] = c2^{-x}$ para $x \in \mathbb{N} = \{0, 1, 2, \dots\}$ (conjunto dos números naturais incluindo-se o zero) e zero no complementar. Determine:
(a) O valor da constante $c$;
(b) $P(X \leq 2)$;
(c) $P(X > 5)$;
(d) $P(X \text{ ser ímpar})$.

## Solução

- **(a) O valor da constante $c$:**
Para que $P[X=x]$ seja uma distribuição de probabilidade válida, a soma de todas as probabilidades deve ser igual a 1.
$$ \sum_{x=0}^{\infty} P(X=x) = 1 $$
$$ \sum_{x=0}^{\infty} c\left(\frac{1}{2}\right)^x = 1 $$
A soma representa uma série geométrica infinita, cujo primeiro termo é $a_0 = c \left(\frac{1}{2}\right)^0 = c$ e a razão é $q = \frac{1}{2}$.
$$ \frac{c}{1 - 1/2} = 1 \implies \frac{c}{1/2} = 1 \implies 2c = 1 \implies c = \frac{1}{2} $$

- **(b) $P(X \leq 2)$:**
$$ P(X \le 2) = P(0) + P(1) + P(2) $$
$$ P(X \le 2) = \frac{1}{2}\left(\frac{1}{2}\right)^0 + \frac{1}{2}\left(\frac{1}{2}\right)^1 + \frac{1}{2}\left(\frac{1}{2}\right)^2 $$
$$ P(X \le 2) = \frac{1}{2} + \frac{1}{4} + \frac{1}{8} = \frac{4+2+1}{8} = \frac{7}{8} = 0,875 $$

- **(c) $P(X > 5)$:**
Podemos calcular somando a série infinita a partir de $x=6$:
$$ P(X > 5) = \sum_{x=6}^{\infty} \frac{1}{2} \left(\frac{1}{2}\right)^x = \sum_{x=6}^{\infty} \left(\frac{1}{2}\right)^{x+1} $$
A série geométrica começa com o termo de $x=6$, que é $\left(\frac{1}{2}\right)^7 = \frac{1}{128}$.
$$ S = \frac{1/128}{1 - 1/2} = \frac{1/128}{1/2} = \frac{2}{128} = \frac{1}{64} $$

- **(d) $P(X \text{ ser ímpar})$:**
Os números ímpares naturais são da forma $x = 2k + 1$, com $k \in \{0, 1, 2, \dots\}$.
$$ P(X \text{ ímpar}) = \sum_{k=0}^{\infty} P(X = 2k + 1) = \sum_{k=0}^{\infty} \frac{1}{2} \left(\frac{1}{2}\right)^{2k+1} $$
$$ P(X \text{ ímpar}) = \sum_{k=0}^{\infty} \frac{1}{2} \cdot \frac{1}{2} \left(\frac{1}{4}\right)^k = \sum_{k=0}^{\infty} \frac{1}{4} \left(\frac{1}{4}\right)^k $$
Esta é outra série geométrica, com primeiro termo $a_0 = \frac{1}{4}$ e razão $q = \frac{1}{4}$.
$$ P(\text{Ímpar}) = \frac{1/4}{1 - 1/4} = \frac{1/4}{3/4} = \frac{1}{3} \approx 0,3333 $$
