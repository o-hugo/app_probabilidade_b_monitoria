---
id: "q37-dantas-cap01"
titulo: "Questão 37"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
A probabilidade de que um aluno saiba a resposta de uma questão de um exame de múltipla escolha é p. Há m respostas possíveis para cada questão, das quais apenas uma é correta. Se o aluno não sabe a resposta para uma dada questão, ele escolhe ao acaso uma das m respostas possíveis. 
(a) Qual é a probabilidade de o aluno responder corretamente uma questão? 
(b) Se o aluno respondeu corretamente a questão, qual é a probabilidade de que ele tenha "chutado" a resposta?

## Solução

Sejam os eventos:
- $S$: o aluno Sabe a resposta. A probabilidade é $P(S) = p$.
- $S^c$: o aluno não sabe e "Chuta". A probabilidade é $P(S^c) = 1 - p$.
- $R$: o aluno Responde corretamente.

Sabemos as probabilidades condicionais:
- $P(R \mid S) = 1$ (se ele sabe, acerta com 100% de certeza).
- $P(R \mid S^c) = \frac{1}{m}$ (se ele chuta, tem 1 chance em $m$).

- **(a) Probabilidade de o aluno responder corretamente ($P(R)$):**
Usamos a Lei da Probabilidade Total:
$$ P(R) = P(S)P(R \mid S) + P(S^c)P(R \mid S^c) $$
$$ P(R) = p(1) + (1 - p)\left(\frac{1}{m}\right) = p + \frac{1-p}{m} = \frac{mp + 1 - p}{m} $$

- **(b) Probabilidade de ele ter "chutado", dado que acertou ($P(S^c \mid R)$):**
Usamos o Teorema de Bayes:
$$ P(S^c \mid R) = \frac{P(S^c)P(R \mid S^c)}{P(R)} $$
$$ P(S^c \mid R) = \frac{(1-p) \frac{1}{m}}{\frac{mp + 1 - p}{m}} $$
Multiplicando o numerador e denominador por $m$:
$$ P(S^c \mid R) = \frac{1-p}{mp + 1 - p} $$
