---
id: "dantas-cap03-q39"
titulo: "Urna de Pólya como Martingal"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
resposta_final: "E[Y_20] = b/(b+p)"
tags: ["esperanca", "condicional", "probabilidade"]
referencia: "Dantas, Cap. 3, Q. 39"
---

## Enunciado

Uma urna contém inicialmente $b$ bolas brancas e $p$ bolas pretas. A cada etapa: retira-se uma bola ao acaso, observa-se a cor, repõe-se + $R$ bolas da mesma cor. $X_n = 1$ se a $n$-ésima bola é branca, $X_n = 0$ caso contrário. Seja $Y_n$ a proporção de bolas brancas na urna após a $n$-ésima etapa.

Mostre que $\{Y_n\}$ é martingal em relação a $\{X_n\}$. Determine $E[Y_{20}]$.

## Passo 1: Fórmula de $Y_n$

Após $n$ etapas, a urna tem $b + p + nR$ bolas no total. Se $W_n$ é o número de bolas brancas após $n$ etapas, então $Y_n = W_n / (b + p + nR)$.

A cada etapa: se a bola retirada é branca (prob $Y_{n-1}$), acrescentam-se $R$ brancas; caso contrário, nada muda para as brancas.

**Resumo:** $W_n = W_{n-1} + R \cdot X_n$, portanto $Y_n = W_n/(b+p+nR)$.

## Passo 2: Verificar a propriedade de martingal

$$E[Y_n \mid X_1, \ldots, X_{n-1}] = E\!\left[\frac{W_{n-1} + R X_n}{b+p+nR} \,\Big|\, X_1,\ldots,X_{n-1}\right]$$

$$= \frac{W_{n-1} + R\,E[X_n \mid X_1,\ldots,X_{n-1}]}{b+p+nR}.$$

Dado $X_1,\ldots,X_{n-1}$, temos $W_{n-1}$ determinado e $E[X_n \mid X_1,\ldots,X_{n-1}] = Y_{n-1} = W_{n-1}/(b+p+(n-1)R)$. Portanto:

$$= \frac{W_{n-1} + R \cdot \frac{W_{n-1}}{b+p+(n-1)R}}{b+p+nR} = \frac{W_{n-1}\bigl(1 + \frac{R}{b+p+(n-1)R}\bigr)}{b+p+nR}$$

$$= \frac{W_{n-1} \cdot \frac{b+p+nR}{b+p+(n-1)R}}{b+p+nR} = \frac{W_{n-1}}{b+p+(n-1)R} = Y_{n-1}.$$

Logo $\{Y_n\}$ é martingal. $\blacksquare$

**Resumo:** $E[Y_n \mid X_1,\ldots,X_{n-1}] = Y_{n-1}$, confirmando a propriedade de martingal.

## Passo 3: Calcular $E[Y_{20}]$

Pela propriedade dos martingais (Ex. 38): $E[Y_{20}] = E[Y_{19}] = \cdots = E[Y_0]$.

O estado inicial (antes de qualquer retirada, $n=0$) tem proporção de brancas $Y_0 = b/(b+p)$.

$$\boxed{E[Y_{20}] = \frac{b}{b+p}.}$$

**Resumo:** A esperança da proporção é invariante ao longo do processo — conserva o valor inicial $b/(b+p)$.
