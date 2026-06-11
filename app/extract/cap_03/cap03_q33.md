---
id: "dantas-cap03-q33"
titulo: "Seringueiras e Tesouro Pirata"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
tags: ["esperanca", "probabilidade"]
referencia: "Dantas, Cap. 3, Q. 33"
---

## Enunciado

Uma ilha tem uma floresta com $N$ seringueiras. Um pirata escondeu seu tesouro dentro de $M$ dessas árvores. Um indivíduo derruba as árvores uma a uma, selecionadas ao acaso, verificando se há ouro.

**(a)** Seja $X$ o número de árvores encontradas com ouro entre $n$ derrubadas. Usando funções indicadoras, encontre $E(X)$.

**(b)** Seja $Y$ o número de árvores derrubadas até encontrar $r$ árvores com ouro ($r \leq M$). Encontre $E(Y)$.

## Passo 1: Definir indicadores para o item (a)

Para $i = 1, 2, \ldots, n$, defina o indicador:

$$I_i = \begin{cases} 1 & \text{se a } i\text{-ésima árvore derrubada contém ouro} \\ 0 & \text{caso contrário} \end{cases}$$

Então $X = I_1 + I_2 + \cdots + I_n$.

**Resumo:** $X$ é soma de indicadores de cada derrubada conter ouro.

## Passo 2: Calcular $E(I_i)$

Por simetria, cada árvore tem a mesma probabilidade de conter ouro:

$$E(I_i) = P[\text{árvore } i \text{ contém ouro}] = \frac{M}{N}.$$

**Resumo:** Cada indicador tem esperança $M/N$ por simetria.

## Passo 3: Esperança de $X$

$$E(X) = \sum_{i=1}^{n} E(I_i) = n \cdot \frac{M}{N} = \frac{nM}{N}.$$

**Resumo:** $E(X) = nM/N$ pela linearidade da esperança.

## Passo 4: Item (b) — $E(Y)$ usando indicadores

Defina $J_j = 1$ se a $j$-ésima árvore derrubada (dentre todas) contém ouro, $J_j = 0$ caso contrário. Então $Y = $ posição da $r$-ésima árvore com ouro.

Pelo argumento de simetria, a posição esperada da $r$-ésima "sucesso" em amostragem sem reposição de $M$ sucessos em $N$ itens é:

$$E(Y) = r \cdot \frac{N+1}{M+1}.$$

**Resumo:** Por simetria de amostragem sem reposição, $E(Y) = r(N+1)/(M+1)$.
