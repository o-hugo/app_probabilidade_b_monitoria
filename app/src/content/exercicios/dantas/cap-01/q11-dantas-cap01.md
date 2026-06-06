---
id: "q11-dantas-cap01"
titulo: "Questão 11"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Sejam A e B dois eventos de um mesmo espaço de probabilidades. Sabendo-se que $P(A)=0,7$ e $P(B)=0,6$, determine o valor máximo e mínimo de $P(A \cap B)$.

## Solução

A probabilidade da interseção $P(A \cap B)$ está sujeita a duas restrições principais decorrentes das propriedades da probabilidade.

1. **Valor máximo:**
   A interseção $A \cap B$ está contida tanto em $A$ quanto em $B$. Logo, $P(A \cap B) \le P(A)$ e $P(A \cap B) \le P(B)$.
   $$P(A \cap B) \le \min(P(A), P(B)) = \min(0,7, 0,6) = 0,6$$
   Portanto, o valor máximo possível para $P(A \cap B)$ é **0,6** (que ocorre quando $B \subset A$).

2. **Valor mínimo:**
   Sabemos pela lei da adição que:
   $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
   Rearranjando para a interseção:
   $$P(A \cap B) = P(A) + P(B) - P(A \cup B)$$
   Sabemos também que a probabilidade da união não pode ultrapassar 1: $P(A \cup B) \le 1$.
   Portanto:
   $$P(A \cap B) \ge P(A) + P(B) - 1$$
   $$P(A \cap B) \ge 0,7 + 0,6 - 1 = 1,3 - 1 = 0,3$$
   Portanto, o valor mínimo possível para $P(A \cap B)$ é **0,3**.
