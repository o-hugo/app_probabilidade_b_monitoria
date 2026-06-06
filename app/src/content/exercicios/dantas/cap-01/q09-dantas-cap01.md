---
id: "q09-dantas-cap01"
titulo: "Questão 9"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
$A, B$ e $C$ são três eventos de um mesmo espaço amostral, tais que:
$P(B)=0,5, \quad P(C)=0,3, \quad P(B\mid C)=0,4$ e $P(A\mid (B\cap C))=0,5.$
Calcule $P(A\cap B\cap C).$

## Solução

Vamos usar a definição de probabilidade condicional para resolver passo a passo.
A probabilidade condicional é definida como $P(X \mid Y) = \frac{P(X \cap Y)}{P(Y)}$.

1. Primeiro, utilizamos $P(B \mid C)$ e $P(C)$ para encontrar $P(B \cap C)$:
   $$ P(B \mid C) = \frac{P(B \cap C)}{P(C)} $$
   $$ 0,4 = \frac{P(B \cap C)}{0,3} $$
   $$ P(B \cap C) = 0,4 \times 0,3 = 0,12 $$

2. Agora, utilizamos $P(A \mid (B \cap C))$ e $P(B \cap C)$ para encontrar a intersecção tríplice $P(A \cap B \cap C)$:
   $$ P(A \mid (B \cap C)) = \frac{P(A \cap B \cap C)}{P(B \cap C)} $$
   $$ 0,5 = \frac{P(A \cap B \cap C)}{0,12} $$
   $$ P(A \cap B \cap C) = 0,5 \times 0,12 = 0,06 $$

**Resposta:** $P(A\cap B\cap C) = 0,06$.
