---
id: "q23-dantas-cap01"
titulo: "Questão 23"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Uma cidade tem 30.000 habitantes e três jornais: A, B e C. Uma pesquisa de opinião revela que 12.000 lêem A, 8.000 lêem B; 7.000 lêem A e B; 6.000 lêem C; 4.500 lêem A e C; 1.000 lêem B e C e 500 lêem A, B e C. Selecionamos ao acaso um habitante dessa cidade. Qual a probabilidade de que ele leia: 
(a) pelo menos um jornal? 
(b) somente um jornal?

## Solução

Sendo $n(\Omega) = 30.000$, podemos resolver encontrando o número de elementos de cada conjunto pelo Princípio da Inclusão-Exclusão ou construindo um Diagrama de Venn.

Dados:
$n(A) = 12000$, $n(B) = 8000$, $n(C) = 6000$
$n(A \cap B) = 7000$, $n(A \cap C) = 4500$, $n(B \cap C) = 1000$
$n(A \cap B \cap C) = 500$

- **(a) Pelo menos um jornal**
Isso equivale à união dos três conjuntos: $n(A \cup B \cup C)$.
$$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C)$$
$$n(A \cup B \cup C) = 12000 + 8000 + 6000 - 7000 - 4500 - 1000 + 500$$
$$n(A \cup B \cup C) = 26000 - 12500 + 500 = 14000$$
A probabilidade é:
$$P(\text{pelo menos um}) = \frac{14000}{30000} = \frac{14}{30} = \frac{7}{15} \approx 0,4667$$

- **(b) Somente um jornal**
Calculamos os habitantes que leem apenas um dos jornais removendo as interseções:
Somente $A = n(A) - n(A \cap B) - n(A \cap C) + n(A \cap B \cap C)$
Somente $A = 12000 - 7000 - 4500 + 500 = 1000$

Somente $B = n(B) - n(A \cap B) - n(B \cap C) + n(A \cap B \cap C)$
Somente $B = 8000 - 7000 - 1000 + 500 = 500$

Somente $C = n(C) - n(A \cap C) - n(B \cap C) + n(A \cap B \cap C)$
Somente $C = 6000 - 4500 - 1000 + 500 = 1000$

Total de leitores de exatamente um jornal = $1000 + 500 + 1000 = 2500$.
A probabilidade é:
$$P(\text{somente um}) = \frac{2500}{30000} = \frac{25}{300} = \frac{1}{12} \approx 0,0833$$
