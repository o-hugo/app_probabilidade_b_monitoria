---
id: "dantas-cap01-q02"
titulo: "Operacoes com Eventos em Lancamento de Moeda"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade"]
referencia: "Dantas, Cap. 1, Q. 2"
---

## Enunciado
Uma moeda é lançada três vezes. Descreva o espaço amostral.
Considere os eventos $A_i$: cara no $i$-ésimo lançamento, para $i = 1, 2, 3$. Determine os seguintes eventos:
(a) $A_1^c \cap A_2$;
(b) $A_1^c \cup A_2$;
(c) $(A_1^c \cap A_2^c)^c$;
(d) $A_1 \cap (A_2 \cup A_3)$.

## Solução

Espaço amostral (onde C = Cara, K = Coroa):
$\Omega = \{(x_1, x_2, x_3) : x_i \in \{C, K\}\} = \{CCC, CCK, CKC, CKK, KCC, KCK, KKC, KKK\}$.

Eventos $A_1, A_2, A_3$:
$A_1 = \{CCC, CCK, CKC, CKK\}$
$A_2 = \{CCC, CCK, KCC, KCK\}$
$A_3 = \{CCC, CKC, KCC, KKC\}$

- **(a) $A_1^c \cap A_2$**: Ocorre coroa no 1º lançamento e cara no 2º.
$A_1^c \cap A_2 = \{KCC, KCK\}$.

- **(b) $A_1^c \cup A_2$**: Ocorre coroa no 1º ou cara no 2º.
$A_1^c \cup A_2 = \{KCC, KCK, KKC, KKK\} \cup \{CCC, CCK, KCC, KCK\} = \{CCC, CCK, KCC, KCK, KKC, KKK\}$.

- **(c) $(A_1^c \cap A_2^c)^c$**: Pelas leis de De Morgan, $(A_1^c \cap A_2^c)^c = A_1 \cup A_2$.
$A_1 \cup A_2 = \{CCC, CCK, CKC, CKK, KCC, KCK\}$.

- **(d) $A_1 \cap (A_2 \cup A_3)$**: Cara no 1º, e cara no 2º ou 3º.
$A_1 \cap (A_2 \cup A_3) = \{CCC, CCK, CKC\}$.
