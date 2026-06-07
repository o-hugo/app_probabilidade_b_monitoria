---
id: "dantas-cap02-q26"
titulo: "FDA do Maximo em Amostragem sem Reposicao"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["fda"]
referencia: "Dantas, Cap. 2, Q. 26"
---

## Enunciado
Cinco bolas são selecionadas aleatoriamente sem reposição de uma urna contendo N bolas numeradas de 1 até N, $N > 5$. Seja X a variável aleatória que denota o maior valor selecionado, determine a função de distribuição de X.

## Solução

A função de distribuição de probabilidade acumulada (f.d.a) de $X$ é denotada por $F_X(k) = P(X \le k)$.
A variável $X$ representa o **maior** valor numérico obtido entre as 5 bolas sorteadas.
A condição de o maior valor ser menor ou igual a $k$ (ou seja, $X \le k$) é equivalente a dizer que **todas as 5 bolas sorteadas devem ter valores menores ou iguais a $k$**.

As bolas na urna possuem números de $1$ a $N$. O total de bolas com número menor ou igual a $k$ é exatamente $k$.
A quantidade de modos distintos de selecionar 5 bolas dentro do subconjunto das primeiras $k$ bolas é dada pela combinação $\binom{k}{5}$. (Isso só é possível se $k \ge 5$).
A quantidade de modos de selecionar qualquer grupo de 5 bolas dentre as $N$ bolas disponíveis na urna inteira é o total do espaço amostral, $\binom{N}{5}$.

Portanto, a probabilidade é dada por casos favoráveis sobre o total de casos possíveis:
$$ F_X(k) = P(X \le k) = \frac{\binom{k}{5}}{\binom{N}{5}} $$

**Definição Formal da Função de Distribuição:**
Para números reais $x$:
- Se $x < 5$: $F_X(x) = 0$ (é impossível escolher 5 bolas distintas e a maior ter valor inferior a 5).
- Se $5 \le x \le N$: $F_X(x) = \frac{\binom{\lfloor x \rfloor}{5}}{\binom{N}{5}}$, onde $\lfloor x \rfloor$ denota o maior inteiro menor ou igual a $x$.
- Se $x \ge N$: $F_X(x) = 1$.
