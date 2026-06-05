---
id: "questoes-q27-livro-exemplo-251-loteria"
titulo: "Exemplo 2.5.1 (Loteria)"
topicos: ["modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado

Uma loteria vende 100 bilhetes. O preço de cada bilhete é R$ 1,20 e o bilhete sorteado paga um prêmio de R$ 100,00. Você compra um bilhete. Qual é a esperança de seu ganho?

## Solução

## Passo 1: Definir a Variável Aleatória 'Ganho'

Seja X a variável aleatória que representa o ganho líquido. Temos dois cenários possíveis:

1. **Você Perde:** Seu bilhete não é sorteado. Seu ganho é o valor do prêmio (R$ 0) menos o custo do bilhete (R$ 1,20). $X = 0 - 1.20 = -1.20$.

2. **Você Ganha:** Seu bilhete é sorteado. Seu ganho é o valor do prêmio (R$ 100) menos o custo do bilhete (R$ 1,20). $X = 100 - 1.20 = 98.80$.

Resumo: Identificamos todos os resultados possíveis para o ganho líquido.



## Passo 2: Determinar as Probabilidades

Há 100 bilhetes no total.

A probabilidade de ganhar é de 1 em 100: $P(X=98.80) = 1/100 = 0.01$.

A probabilidade de perder é de 99 em 100: $P(X=-1.20) = 99/100 = 0.99$.

Resumo: Calculamos as probabilidades para cada um dos possíveis ganhos.



## Passo 3: Calcular a Esperança Matemática

A esperança de uma variável discreta é a soma de cada valor multiplicado por sua probabilidade: $E(X) = \sum x_i P(X=x_i)$.

$$E(X) = (98.80) \cdot (0.01) + (-1.20) \cdot (0.99)$$

$$E(X) = 0.988 - 1.188 = -0.20$$

A esperança de seu ganho é de -R$ 0,20. Isso significa que, em média, você espera perder 20 centavos cada vez que joga.

Resumo: Aplicamos a fórmula da esperança para encontrar o valor esperado do ganho, que representa o resultado médio a longo prazo.
