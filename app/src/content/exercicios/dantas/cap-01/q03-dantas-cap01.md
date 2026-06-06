---
id: "q03-dantas-cap01"
titulo: "Questão 3"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

> [!NOTE]
> A numeração desta questão (3) foi inferida pela sua sequência no livro original.

## Enunciado
Suponha que o espaço amostral é o intervalo [0,1] dos reais.
Considere os eventos $A = \{x : 1/4 \le x \le 5/8\}$ e $B = \{x : 1/2 \le x \le 7/8\}$. Determine os eventos:
(a) $A^c$;
(b) $A \cap B^c$;
(c) $(A \cup B)^c$;
(d) $A^c \cup B$.

## Solução

O espaço amostral é $\Omega = [0, 1]$.
Os eventos são os intervalos $A = [1/4, 5/8]$ e $B = [1/2, 7/8]$.

- **(a) $A^c$**: Complementar de $A$ em $[0, 1]$.
$A^c = [0, 1/4) \cup (5/8, 1]$.

- **(b) $A \cap B^c$**: Interseção de $A$ com o complementar de $B$ ($B^c = [0, 1/2) \cup (7/8, 1]$).
$A \cap B^c = [1/4, 5/8] \cap ([0, 1/2) \cup (7/8, 1]) = [1/4, 1/2)$.

- **(c) $(A \cup B)^c$**: Complementar da união $A \cup B$.
$A \cup B = [1/4, 7/8]$. Logo, $(A \cup B)^c = [0, 1/4) \cup (7/8, 1]$.

- **(d) $A^c \cup B$**: União do complementar de $A$ com $B$.
$A^c \cup B = [0, 1/4) \cup (5/8, 1] \cup [1/2, 7/8] = [0, 1/4) \cup [1/2, 1]$.
