---
id: "q15-dantas-cap01"
titulo: "Questão 15"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Prove que:
(a) Se $P(A^c) = \alpha$ e $P(B^c) = \beta$, então $P(A \cap B) \ge 1 - \alpha - \beta$;
(b) Se $P(A \mid B) \ge P(A)$, então $P(B \mid A) \ge P(B)$.

*(Nota: O enunciado do item (a) no livro usa a notação para a Desigualdade de Bonferroni.)*

## Solução

- **Prova da alternativa (a) - Desigualdade de Bonferroni**
Sabemos que a probabilidade do complementar é:
$$P(A \cap B) = 1 - P((A \cap B)^c)$$
Pelas Leis de De Morgan, o complementar da interseção é a união dos complementares:
$$P(A \cap B) = 1 - P(A^c \cup B^c)$$
A probabilidade da união de dois eventos nunca excede a soma das probabilidades de cada evento separadamente:
$$P(A^c \cup B^c) \le P(A^c) + P(B^c)$$
Substituindo os valores dados no problema:
$$P(A^c \cup B^c) \le \alpha + \beta$$
Voltando para a equação original, se a parte subtraída é menor ou igual a $\alpha + \beta$, a subtração final resultará num valor maior ou igual:
$$P(A \cap B) \ge 1 - (\alpha + \beta) \implies P(A \cap B) \ge 1 - \alpha - \beta$$
*A identidade está provada.*

- **Prova da alternativa (b)**
Por definição, a probabilidade condicional é dada por:
$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$
De acordo com o enunciado, $P(A \mid B) \ge P(A)$. Substituindo:
$$\frac{P(A \cap B)}{P(B)} \ge P(A)$$
Multiplicando ambos os lados por $P(B)$ (que assumimos ser $>0$ para que a probabilidade condicional exista):
$$P(A \cap B) \ge P(A)P(B)$$
Dividindo ambos os lados por $P(A)$ (assumindo $P(A) > 0$):
$$\frac{P(A \cap B)}{P(A)} \ge P(B)$$
O lado esquerdo da inequação nada mais é do que a definição de $P(B \mid A)$:
$$P(B \mid A) \ge P(B)$$
*A identidade está provada.*
