---
id: "dantas-cap01-q12"
titulo: "Eventos Independentes Dois a Dois com Intersecao Vazia"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 1, Q. 12"
---

## Enunciado
Sejam A, B e C três eventos independentes dois a dois tal que $A \cap B \cap C = \emptyset$. Dado que $P(A) = P(B) = P(C) = x$, determine o maior valor possível de $x$.

## Solução

Temos três eventos $A$, $B$ e $C$. Eles são independentes dois a dois, o que significa que:
$$P(A \cap B) = P(A)P(B) = x \cdot x = x^2$$
$$P(A \cap C) = P(A)P(C) = x \cdot x = x^2$$
$$P(B \cap C) = P(B)P(C) = x \cdot x = x^2$$

Também sabemos que a interseção dos três é vazia, logo:
$$P(A \cap B \cap C) = 0$$

Para encontrar o maior valor de $x$, precisamos garantir que nenhuma probabilidade das diversas interseções ou de suas componentes exceda as restrições lógicas. Em particular, a probabilidade de uma dada região do Diagrama de Venn não pode ser negativa.

Vamos analisar a região de $A$ que ocorre exclusivamente sem $B$ e sem $C$, ou seja, $P(A \cap B^c \cap C^c)$.
Podemos decompor o evento $A$ como a união de partes mutuamente exclusivas:
$$A = (A \cap B \cap C) \cup (A \cap B \cap C^c) \cup (A \cap B^c \cap C) \cup (A \cap B^c \cap C^c)$$

Tomando as probabilidades:
$$P(A) = P(A \cap B \cap C) + P(A \cap B \cap C^c) + P(A \cap B^c \cap C) + P(A \cap B^c \cap C^c)$$

Sabemos que $P(A \cap B) = P(A \cap B \cap C) + P(A \cap B \cap C^c)$. Como $P(A \cap B \cap C) = 0$, temos:
$$P(A \cap B \cap C^c) = P(A \cap B) = x^2$$
De modo análogo:
$$P(A \cap B^c \cap C) = P(A \cap C) = x^2$$

Substituindo tudo na equação de $P(A)$:
$$x = 0 + x^2 + x^2 + P(A \cap B^c \cap C^c)$$
$$P(A \cap B^c \cap C^c) = x - 2x^2$$

Como toda probabilidade deve ser não-negativa ($P \ge 0$), temos:
$$x - 2x^2 \ge 0$$
$$x(1 - 2x) \ge 0$$

Como $x$ representa uma probabilidade, $x \ge 0$. Logo, a inequação se satisfaz para:
$$1 - 2x \ge 0 \implies 2x \le 1 \implies x \le \frac{1}{2}$$

Assim, o maior valor possível de $x$ é $\frac{1}{2}$.
