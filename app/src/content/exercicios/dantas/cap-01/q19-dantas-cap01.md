---
id: "q19-dantas-cap01"
titulo: "Questão 19"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Um número é escolhido, ao acaso, entre os números inteiros de 1 a 20. Considere os eventos: 
$A$ : o número escolhido é múltiplo de 3; 
$B$ : o número escolhido é par. 
Descreva os eventos $A \cap B$, $A \cup B$, $A \cap B^c$ e calcule suas probabilidades.

## Solução

O espaço amostral é $\Omega = \{1, 2, \dots, 20\}$ e possui $20$ elementos equiprováveis.

O evento $A$ (múltiplos de 3) é: $A = \{3, 6, 9, 12, 15, 18\}$. (6 elementos)
O evento $B$ (pares) é: $B = \{2, 4, 6, 8, 10, 12, 14, 16, 18, 20\}$. (10 elementos)

- **$A \cap B$ (Múltiplo de 3 E Par):**
Ou seja, são os múltiplos de 6.
$A \cap B = \{6, 12, 18\}$
A quantidade de elementos é 3.
$$P(A \cap B) = \frac{3}{20} = 0,15$$

- **$A \cup B$ (Múltiplo de 3 OU Par):**
$A \cup B = \{2, 3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20\}$
A quantidade de elementos é $6 + 10 - 3 = 13$.
$$P(A \cup B) = \frac{13}{20} = 0,65$$

- **$A \cap B^c$ (Múltiplo de 3 E Ímpar):**
Consiste nos elementos de A que não estão em B.
$A \cap B^c = \{3, 9, 15\}$
A quantidade de elementos é 3.
$$P(A \cap B^c) = \frac{3}{20} = 0,15$$
