---
id: "dantas-cap03-q31"
titulo: "E[X₁ | X₁+...+Xₙ = x] para variáveis i.i.d."
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "E[X₁ | X₁+...+Xₙ = x] = x/n"
tags: ["condicional", "esperanca"]
referencia: "Dantas, Cap. 3, Q. 31"
---

## Enunciado

Sejam $X_1, X_2, \ldots, X_n$ variáveis aleatórias independentes e identicamente distribuídas (i.i.d.). Determine $E[X_1 \mid X_1 + X_2 + \cdots + X_n = x]$.

## Passo 1: Argumento de simetria

**Resumo:** Como as $X_i$ são i.i.d., todas têm o mesmo papel; por simetria, $E[X_i | S_n=x]$ é o mesmo para todo $i$.

Seja $S_n = X_1 + X_2 + \cdots + X_n$. Por simetria (as variáveis são i.i.d., portanto intercambiáveis), a esperança condicional $E[X_i \mid S_n = x]$ é a mesma para todo $i = 1, \ldots, n$:

$$E[X_1 \mid S_n = x] = E[X_2 \mid S_n = x] = \cdots = E[X_n \mid S_n = x].$$

## Passo 2: Uso da linearidade

**Resumo:** Soma as esperanças condicionais e usa que $E[S_n | S_n=x] = x$.

Pela linearidade da esperança condicional:

$$E[S_n \mid S_n = x] = E[X_1 \mid S_n = x] + E[X_2 \mid S_n = x] + \cdots + E[X_n \mid S_n = x].$$

O lado esquerdo é trivialmente $x$ (dado que $S_n = x$). Usando a simetria:

$$x = n \cdot E[X_1 \mid S_n = x].$$

## Passo 3: Resultado

**Resumo:** Divide por $n$ para obter o resultado final.

$$\boxed{E[X_1 \mid X_1 + X_2 + \cdots + X_n = x] = \frac{x}{n}.}$$

**Interpretação:** Condicionado na soma total $x$, cada parcela "recebe" em média $x/n$, distribuindo igualmente o total entre as $n$ variáveis.
