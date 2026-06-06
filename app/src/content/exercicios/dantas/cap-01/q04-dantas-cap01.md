---
id: "q04-dantas-cap01"
titulo: "Questão 4"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Quais das seguintes relações são verdadeiras:
(a) $(A \cup B) \cap (A \cup C) = A \cup (A \cap C)$
(b) $A \cup B = (A \cap B^c) \cup B$
(c) $A^c \cap B = A \cup B$
(d) $(A \cup B)^c \cap C = A^c \cap B^c \cap C^c$

## Solução

- **(a) Falsa**. Pela distributividade da união em relação à interseção, temos que $(A \cup B) \cap (A \cup C) = A \cup (B \cap C)$, o que em geral é diferente de $A \cup (A \cap C) = A$.
- **(b) Verdadeira**. Podemos expandir o lado direito usando a distributividade: $(A \cap B^c) \cup B = (A \cup B) \cap (B^c \cup B) = (A \cup B) \cap \Omega = A \cup B$.
- **(c) Falsa**. O evento $A^c \cap B$ representa apenas a região de $B$ que não intercepta $A$, enquanto $A \cup B$ representa tudo que está em $A$ ou em $B$.
- **(d) Falsa**. Pelas leis de De Morgan, $(A \cup B)^c \cap C = (A^c \cap B^c) \cap C = A^c \cap B^c \cap C$. O lado direito da afirmação diz $A^c \cap B^c \cap C^c$, que é a interseção com o complementar de $C$, logo são conjuntos distintos (de fato, mutuamente exclusivos).
