---
id: "q05-dantas-cap01"
titulo: "Questão 5"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Sejam A, B e C três eventos de um espaço amostral. Determine expressões em função de A, B e C para os eventos:
(a) somente A ocorre;
(b) todos os três eventos ocorrem;
(c) pelo menos dois eventos ocorrem;
(d) exatamente dois eventos ocorrem;
(e) não mais do que dois eventos ocorrem;
(f) A e B ocorrem, mas C não ocorre;
(g) pelo menos um dos eventos ocorre;
(h) exatamente um dos eventos ocorre;
(i) nenhum dos eventos ocorre.

## Solução

As expressões baseadas nas operações de teoria dos conjuntos são:

- **(a) Somente $A$ ocorre:** $A \cap B^c \cap C^c$
- **(b) Todos os três eventos ocorrem:** $A \cap B \cap C$
- **(c) Pelo menos dois eventos ocorrem:** $(A \cap B) \cup (A \cap C) \cup (B \cap C)$
- **(d) Exatamente dois eventos ocorrem:** $(A \cap B \cap C^c) \cup (A \cap B^c \cap C) \cup (A^c \cap B \cap C)$
- **(e) Não mais do que dois eventos ocorrem:** Equivale a dizer que não ocorrem os três juntos, logo $(A \cap B \cap C)^c$ ou $A^c \cup B^c \cup C^c$
- **(f) A e B ocorrem, mas C não ocorre:** $A \cap B \cap C^c$
- **(g) Pelo menos um dos eventos ocorre:** A união dos três eventos, $A \cup B \cup C$
- **(h) Exatamente um dos eventos ocorre:** A união das regiões onde só um ocorre, $(A \cap B^c \cap C^c) \cup (A^c \cap B \cap C^c) \cup (A^c \cap B^c \cap C)$
- **(i) Nenhum dos eventos ocorre:** O complementar da união dos três eventos, $A^c \cap B^c \cap C^c$ ou $(A \cup B \cup C)^c$
