---
id: "q13-dantas-cap01"
titulo: "Questão 13"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Sejam A e B eventos de um mesmo espaço amostral. Se A e B são independentes, prove que A e $B^c$; $A^c$ e B; $A^c$ e $B^c$ também são independentes.
*(Nota: O texto original continha uma repetição "A^c e B; A^c e B", que foi corrigida no enunciado lógico de todas as permutações.)*

## Solução

Se $A$ e $B$ são independentes, sabemos por definição que:
$$P(A \cap B) = P(A)P(B)$$

**1. Provando que $A$ e $B^c$ são independentes:**
Temos que o conjunto $A$ pode ser dividido em duas partes disjuntas: a que está em $B$ e a que está em $B^c$.
$$A = (A \cap B) \cup (A \cap B^c)$$
$$P(A) = P(A \cap B) + P(A \cap B^c)$$
Isolando $P(A \cap B^c)$:
$$P(A \cap B^c) = P(A) - P(A \cap B)$$
Substituindo a independência de A e B:
$$P(A \cap B^c) = P(A) - P(A)P(B) = P(A)(1 - P(B))$$
Como $P(B^c) = 1 - P(B)$, temos:
$$P(A \cap B^c) = P(A)P(B^c)$$
Isso prova que $A$ e $B^c$ são independentes.

**2. Provando que $A^c$ e $B$ são independentes:**
A demonstração é idêntica à anterior, mas considerando $B = (A \cap B) \cup (A^c \cap B)$:
$$P(A^c \cap B) = P(B) - P(A \cap B) = P(B) - P(A)P(B) = P(B)(1 - P(A)) = P(A^c)P(B)$$
O que prova a independência.

**3. Provando que $A^c$ e $B^c$ são independentes:**
Queremos encontrar $P(A^c \cap B^c)$. Pelas Leis de De Morgan, sabemos que $A^c \cap B^c = (A \cup B)^c$.
$$P(A^c \cap B^c) = 1 - P(A \cup B)$$
Usando a regra da adição:
$$P(A^c \cap B^c) = 1 - (P(A) + P(B) - P(A \cap B))$$
Substituindo $P(A \cap B) = P(A)P(B)$:
$$P(A^c \cap B^c) = 1 - P(A) - P(B) + P(A)P(B)$$
Podemos fatorar esta expressão agrupando os termos:
$$P(A^c \cap B^c) = (1 - P(A)) - P(B)(1 - P(A)) = (1 - P(A))(1 - P(B))$$
Substituindo pelas probabilidades dos complementares:
$$P(A^c \cap B^c) = P(A^c)P(B^c)$$
Fica demonstrado que $A^c$ e $B^c$ são independentes.
