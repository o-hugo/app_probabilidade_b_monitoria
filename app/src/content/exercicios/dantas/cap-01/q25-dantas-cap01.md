---
id: "q25-dantas-cap01"
titulo: "Questão 25"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Um restaurante popular apresenta dois tipos de refeições: salada completa e um prato à base de carne. 20% dos fregueses do sexo masculino preferem salada, e 30% das mulheres preferem carne. 75% dos fregueses são homens. Considere os seguintes eventos:

H: o freguês é homem, M: o freguês é mulher,
A: o freguês prefere salada, B: o freguês prefere carne.

Calcule:
(a) $P(H)$, $P(A \mid H)$ e $P(B \mid H)$;
(b) $P(A \cup H)$ e $P(A \cap H)$;
(c) $P(M \mid A)$.

## Solução

Temos as seguintes informações diretas do problema:
$P(H) = 0,75$ e $P(M) = 1 - 0,75 = 0,25$.
Dentre os homens, 20% preferem salada: $P(A \mid H) = 0,20$.
Dentre as mulheres, 30% preferem carne: $P(B \mid M) = 0,30$.
Como só há 2 opções de prato (Salada e Carne), deduzimos que:
$P(B \mid H) = 1 - 0,20 = 0,80$ e $P(A \mid M) = 1 - 0,30 = 0,70$.

- **(a) $P(H)$, $P(A \mid H)$ e $P(B \mid H)$:**
$$ P(H) = 0,75 $$
$$ P(A \mid H) = 0,20 $$
$$ P(B \mid H) = 0,80 $$

- **(b) $P(A \cap H)$ e $P(A \cup H)$:**
(Note que na alternativa b foram cobrados a união e a interseção, e na original do livro havia um símbolo misto. Vamos calcular os dois.)
Primeiro calculamos a interseção:
$$ P(A \cap H) = P(A \mid H)P(H) = 0,20 \times 0,75 = 0,15 $$
Para a união, precisaremos de $P(A)$. Usamos a Lei da Probabilidade Total:
$$ P(A) = P(A \cap H) + P(A \cap M) = P(A \mid H)P(H) + P(A \mid M)P(M) $$
$$ P(A) = (0,20 \times 0,75) + (0,70 \times 0,25) = 0,15 + 0,175 = 0,325 $$
Com isso, calculamos a união:
$$ P(A \cup H) = P(A) + P(H) - P(A \cap H) $$
$$ P(A \cup H) = 0,325 + 0,75 - 0,15 = 0,925 $$

- **(c) $P(M \mid A)$:**
Usamos o Teorema de Bayes:
$$ P(M \mid A) = \frac{P(A \mid M)P(M)}{P(A)} $$
$$ P(M \mid A) = \frac{0,70 \times 0,25}{0,325} = \frac{0,175}{0,325} = \frac{175}{325} = \frac{7}{13} \approx 0,5385 $$
