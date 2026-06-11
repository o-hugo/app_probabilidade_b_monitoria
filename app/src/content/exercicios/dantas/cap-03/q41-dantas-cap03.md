---
id: "dantas-cap03-q41"
titulo: "Tábua de Vida e Taxa de Mortalidade"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "alta"
origem: "livro"
solucao_verificada: false
tags: ["probabilidade", "taxa-de-falha", "confiabilidade"]
referencia: "Dantas, Cap. 3, Q. 41"
---

## Enunciado

Seja $_tP_x$ a probabilidade de uma pessoa com $x$ anos sobreviver $t$ anos. Mostre que:

$$_{t+u}P_x = ({_tP_x})({_uP_{x+t}}).$$

Para $t$ inteiro $n$: $_nP_x = P_x \cdot P_{x+1} \cdots P_{x+n-1}$.

Com $\ell_0$ constante positiva, defina $\ell_x = \ell_0 \cdot {_xP_0}$ e $d_x = \ell_x - \ell_{x+1}$. Mostre:

$$_tP_x = \frac{\ell_{x+t}}{\ell_x} \qquad \text{e} \qquad q_x = \frac{d_x}{\ell_x}.$$

Interprete $q_x$ (taxa de mortalidade à idade $x$).

## Passo 1: Mostrar $_{t+u}P_x = (_tP_x)(_uP_{x+t})$

Sobreviver $t+u$ anos a partir de $x$ equivale a:
1. Sobreviver $t$ anos (prob $_tP_x$), e então
2. Sobreviver mais $u$ anos a partir da idade $x+t$ (prob $_uP_{x+t}$).

Por independência dos eventos futuros dado que sobreviveu até $x+t$:

$$_{t+u}P_x = {_tP_x} \cdot {_uP_{x+t}}. \qquad \blacksquare$$

**Resumo:** A lei dos produtos encadeados segue da Markov/independência condicional.

## Passo 2: Caso inteiro $n$

Aplicando repetidamente com $t=1$:

$$_nP_x = P_x \cdot {_{n-1}P_{x+1}} = P_x \cdot P_{x+1} \cdot {_{n-2}P_{x+2}} = \cdots = P_x P_{x+1} \cdots P_{x+n-1}.$$

**Resumo:** Para $t$ inteiro, decompõe em sobrevivência ano a ano.

## Passo 3: Fórmula para $_tP_x$

Por definição $\ell_x = \ell_0 \cdot {_xP_0}$ e $\ell_{x+t} = \ell_0 \cdot {_{x+t}P_0}$. Do resultado do Passo 1:

$$_{x+t}P_0 = {_xP_0} \cdot {_tP_x} \implies {_tP_x} = \frac{_{x+t}P_0}{_xP_0} = \frac{\ell_{x+t}}{\ell_x}. \qquad \blacksquare$$

**Resumo:** $_tP_x = \ell_{x+t}/\ell_x$ pois $\ell$ é proporcional à probabilidade de sobrevivência desde o nascimento.

## Passo 4: Taxa de mortalidade $q_x$

$q_x$ é a probabilidade de morrer entre $x$ e $x+1$: $q_x = 1 - P_x = 1 - {_1P_x} = 1 - \ell_{x+1}/\ell_x = (\ell_x - \ell_{x+1})/\ell_x = d_x/\ell_x$. $\blacksquare$

**Interpretação:** $q_x = d_x/\ell_x$ é a proporção de indivíduos de idade $x$ que morrem antes de atingir a idade $x+1$, segundo a tábua de vida.

**Resumo:** $q_x = d_x/\ell_x$ é a probabilidade de morte no intervalo $[x, x+1)$.
