---
id: "q04-dantas-cap02"
titulo: "Questão 4"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Considere o lançamento de dois dados simultaneamente (admita que os dados são equilibrados). Para cada um dos itens a seguir, determine o campo de variação da variável aleatória $X$, bem como sua distribuição de probabilidades: 
(a) $X$ é o maior valor observado no lançamento dos dois dados. 
(b) $X$ é a soma dos valores observados. 
(c) $X$ é o produto dos valores observados. 
(d) $X$ é a diferença entre o maior valor observado e o menor valor observado.

## Solução

O espaço amostral tem $6 \times 6 = 36$ resultados equiprováveis: $(i,j)$ para $1 \le i,j \le 6$.

- **(a) $X = \max(D_1, D_2)$:**
Valores de $X$: $\{1, 2, 3, 4, 5, 6\}$.
Um resultado dará $X=k$ se a face maior for $k$. 
O total de pares com elementos $\le k$ é $k \times k = k^2$. 
O total de pares onde o máximo é EXATAMENTE $k$ é a diferença entre os pares $\le k$ e os pares $\le k-1$, ou seja, $k^2 - (k-1)^2 = 2k - 1$.
- $P(X=1) = \frac{1}{36}$
- $P(X=2) = \frac{3}{36}$
- $P(X=3) = \frac{5}{36}$
- $P(X=4) = \frac{7}{36}$
- $P(X=5) = \frac{9}{36}$
- $P(X=6) = \frac{11}{36}$

- **(b) $X = D_1 + D_2$:**
Valores de $X$: $\{2, 3, 4, \dots, 12\}$.
A quantidade de pares cuja soma é $k$ cresce linearmente até 7 e depois decresce.
- $P(X=2) = P(X=12) = \frac{1}{36}$
- $P(X=3) = P(X=11) = \frac{2}{36}$
- $P(X=4) = P(X=10) = \frac{3}{36}$
- $P(X=5) = P(X=9) = \frac{4}{36}$
- $P(X=6) = P(X=8) = \frac{5}{36}$
- $P(X=7) = \frac{6}{36}$

- **(c) $X = D_1 \times D_2$:**
Valores possíveis de $X$: $\{1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 30, 36\}$.
Ao construir a tabela de multiplicação $6 \times 6$ e contar as frequências:
- Probabilidade $\frac{1}{36}$: para os valores $1, 9, 16, 25, 36$. (os quadrados perfeitos com raízes de 1 a 6)
- Probabilidade $\frac{2}{36}$: para os valores $2, 3, 5, 8, 10, 15, 18, 20, 24, 30$. (gerados por fatores distintos, aparecendo 2 vezes cada na tabela)
- Probabilidade $\frac{3}{36}$: para o valor $4$. (pares $(1,4), (4,1), (2,2)$)
- Probabilidade $\frac{4}{36}$: para os valores $6$ e $12$. (pares para 6: $(1,6), (6,1), (2,3), (3,2)$. Para 12: $(2,6), (6,2), (3,4), (4,3)$)

- **(d) $X = |D_1 - D_2|$ (A diferença entre o maior e o menor):**
Valores de $X$: $\{0, 1, 2, 3, 4, 5\}$.
- $X=0$: Pares de valores iguais $(1,1), \dots, (6,6)$. São 6. $P(X=0) = \frac{6}{36}$.
- $X=1$: Pares consecutivos (5 pares) e suas permutações. Total = $2 \times 5 = 10$. $P(X=1) = \frac{10}{36}$.
- $X=2$: Diferença de 2 (4 pares) e permutações. Total = $2 \times 4 = 8$. $P(X=2) = \frac{8}{36}$.
- $X=3$: Diferença de 3 (3 pares) e permutações. Total = $2 \times 3 = 6$. $P(X=3) = \frac{6}{36}$.
- $X=4$: Diferença de 4 (2 pares) e permutações. Total = $2 \times 2 = 4$. $P(X=4) = \frac{4}{36}$.
- $X=5$: Pares $(1,6)$ e $(6,1)$. Total = 2. $P(X=5) = \frac{2}{36}$.
