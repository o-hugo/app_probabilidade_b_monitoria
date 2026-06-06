---
id: "q10-dantas-cap01"
titulo: "Questão 10"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Prove que se A e B são dois eventos de um espaço amostral S e P é uma probabilidade definida nos eventos de S, então:  
$P((A\cap B^c)\cup (B\cap A^c))=P(A)+P(B)-2P(A\cap B).$

## Solução

A expressão $(A\cap B^c)\cup (B\cap A^c)$ é conhecida como a *diferença simétrica* entre $A$ e $B$, muitas vezes denotada como $A \Delta B$. Ela representa os elementos que pertencem exatamente a um dos eventos (mas não a ambos simultaneamente).

Temos os eventos $(A\cap B^c)$ e $(B\cap A^c)$. Como um elemento não pode pertencer a $A$ e a $A^c$ ao mesmo tempo (o mesmo vale para $B$ e $B^c$), esses dois conjuntos são **mutuamente exclusivos** (ou disjuntos), ou seja:
$$(A \cap B^c) \cap (B \cap A^c) = \emptyset$$

Como são disjuntos, a probabilidade da união é a soma das probabilidades:
$$P((A \cap B^c) \cup (B \cap A^c)) = P(A \cap B^c) + P(B \cap A^c)$$

Sabemos que um conjunto $A$ pode ser particionado em duas partes: a que intercepta $B$ e a que não intercepta $B$. Ou seja:
$$A = (A \cap B) \cup (A \cap B^c)$$
Como as partes da união são disjuntas, temos:
$$P(A) = P(A \cap B) + P(A \cap B^c) \implies P(A \cap B^c) = P(A) - P(A \cap B)$$

Fazendo o mesmo raciocínio para $B$:
$$B = (B \cap A) \cup (B \cap A^c)$$
$$P(B) = P(B \cap A) + P(B \cap A^c) \implies P(B \cap A^c) = P(B) - P(A \cap B)$$

Substituindo essas expressões na equação da diferença simétrica:
$$P((A \cap B^c) \cup (B \cap A^c)) = [P(A) - P(A \cap B)] + [P(B) - P(A \cap B)]$$
$$P((A \cap B^c) \cup (B \cap A^c)) = P(A) + P(B) - 2P(A \cap B)$$

A identidade está provada.
