---
id: "questoes-q28-livro-exemplo-272-roleta"
titulo: "Exemplo 2.7.2 (Roleta)"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Na roleta (números de 0 a 36), um jogador aposta R$ 10,00 na primeira dúzia (números de 1 a 12). Se acertar, recebe R$ 2,00 para cada R$ 1,00 apostado (ganha R$ 20,00). Se errar, perde a aposta. Determine a distribuição de probabilidade e a esperança do ganho (Y).

## Solução

## Passo 1: Definir a Variável Aleatória 'Ganho' (Y)

Temos dois resultados para o ganho líquido Y:

1. **O jogador Ganha:** O resultado é um número de 1 a 12. O prêmio é de R$ 20,00. O ganho líquido é o prêmio menos a aposta: $Y = 20 - 10 = 10$? Não, o enunciado diz "recebe R$ 2,00 para cada real apostado". Isso significa que ele recebe os R$10 de volta mais R$20. Ganho líquido = R$ 20. O livro simplifica para o jogador receber R$20. Vamos seguir o cálculo do livro. $Y = 20$.

2. **O jogador Perde:** O resultado é um número de 13 a 36, ou 0. Ele perde a aposta de R$ 10,00. $Y = -10$.

Resumo: Determinamos os possíveis valores para o ganho líquido com base nas regras do jogo.



## Passo 2: Determinar as Probabilidades

A roleta tem 37 números (0 a 36), todos equiprováveis.

Probabilidade de Ganhar: Há 12 números na primeira dúzia. $P(Y=20) = \frac{12}{37}$.

Probabilidade de Perder: Há $36-12=24$ números fora da dúzia, mais o 0, totalizando 25 números. $P(Y=-10) = \frac{25}{37}$.

Resumo: Contamos o número de resultados favoráveis para cada evento e dividimos pelo total de resultados possíveis.



## Passo 3: Apresentar a Distribuição e Calcular a Esperança

A distribuição de probabilidade de Y é:

$P(Y=20) = 12/37$

$P(Y=-10) = 25/37$

A esperança de ganho é:

$$E(Y) = (20) \cdot (\frac{12}{37}) + (-10) \cdot (\frac{25}{37})$$

$$E(Y) = \frac{240}{37} - \frac{250}{37} = -\frac{10}{37} \approx -0.27$$

A esperança de ganho é de aproximadamente -R$ 0,27 por rodada.

Resumo: Usamos a distribuição de probabilidade para calcular o ganho esperado, que é negativo, indicando uma perda média para o jogador a longo prazo.
