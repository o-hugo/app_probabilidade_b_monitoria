---
id: "dantas-cap03-q28"
titulo: "Prisioneiro e três portas: esperança do tempo de saída"
topicos: ["06-distribuicoes-bivariadas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
resposta_final: "E(T) = 3 dias"
tags: ["esperanca", "condicional"]
referencia: "Dantas, Cap. 3, Q. 28"
---

## Enunciado

Um prisioneiro está em uma cela com 3 portas, escolhidas ao acaso (independentemente) em cada tentativa:

- **Porta 1:** túnel que retorna à cela em 2 dias.
- **Porta 2:** túnel que retorna à cela em 4 dias.
- **Porta 3:** saída em 1 dia.

Qual é o número esperado de dias até o prisioneiro sair?

## Passo 1: Configuração do problema com esperanças iteradas

**Resumo:** Define $T$ como o tempo total de saída e condiciona na primeira porta escolhida.

Seja $T$ o tempo total até a saída. Condicione na porta $D$ escolhida na primeira tentativa, com $P(D=i) = 1/3$ para $i = 1, 2, 3$.

Pela lei da esperança total:

$$E(T) = E(T \mid D=1) \cdot \frac{1}{3} + E(T \mid D=2) \cdot \frac{1}{3} + E(T \mid D=3) \cdot \frac{1}{3}.$$

## Passo 2: Cálculo das esperanças condicionais

**Resumo:** Portas 1 e 2 retornam à mesma situação inicial após 2 e 4 dias; porta 3 finaliza em 1 dia.

- $D=3$ (saída): $E(T \mid D=3) = 1$.
- $D=1$ (retorno em 2 dias): após 2 dias, o prisioneiro está na mesma situação de partida, logo $E(T \mid D=1) = 2 + E(T)$.
- $D=2$ (retorno em 4 dias): $E(T \mid D=2) = 4 + E(T)$.

## Passo 3: Resolução da equação

**Resumo:** Substitui na equação da esperança total e resolve para $E(T)$.

$$E(T) = \frac{1}{3}(2 + E(T)) + \frac{1}{3}(4 + E(T)) + \frac{1}{3}(1).$$

$$E(T) = \frac{2 + E(T) + 4 + E(T) + 1}{3} = \frac{7 + 2E(T)}{3}.$$

$$3E(T) = 7 + 2E(T) \implies E(T) = 7.$$

$$\boxed{E(T) = 7 \text{ dias}}$$

**Interpretação:** O prisioneiro leva em média 7 dias para sair, pois com probabilidade $2/3$ perde dias retornando antes de finalmente escolher a porta 3.
