---
id: "q41-dantas-cap02"
titulo: "Questão 41"
topicos: ["03-modelos-continuos"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Um florista faz estoque de uma flor de curta duração que lhe custa R$ 0,50 e que ele vende a R$ 1,50 no primeiro dia em que a flor está na loja. Toda flor que não é vendida nesse primeiro dia é jogada fora. Seja X a variável aleatória que denota o número de flores vendidas por este florista em um dia. Sabendo-se que a função de probabilidade de X é dada por:

| X | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| P(X = x) | 1/10 | 4/10 | 3/10 | 2/10 |

determine quantas flores deveria o florista ter em estoque a fim de maximizar o lucro esperado.

## Solução

Este problema é uma aplicação numérica direta do "Problema do Jornaleiro" derivado e equacionado de forma genérica na Questão 40.
Conforme demonstrado anteriormente, o nível ótimo de estoque $k^*$ é o menor inteiro que satisfaz a seguinte relação sobre a Função de Distribuição Acumulada da demanda:
$$ F(k^*) = P(X \le k^*) \ge \frac{B}{B+L} $$

Temos os seguintes parâmetros econômicos baseados no enunciado:
- Preço de venda = 1,50
- Custo unitário = 0,50
- O lucro limpo ganho por uma unidade bem-sucedida é $B = 1,50 - 0,50 = 1,00$.
- O prejuízo de uma unidade não vendida e descartada (encalhe) é o dinheiro rasgado no custo: $L = 0,50$.

Avaliando o limiar crítico da probabilidade acumulada (índice de nível de serviço):
$$ \frac{B}{B+L} = \frac{1,00}{1,00 + 0,50} = \frac{1}{1,5} = \frac{2}{3} \approx 0,6667 \ (66,67\%) $$

Agora, avaliaremos empiricamente a Função de Distribuição Acumulada de $X$, somando sucessivamente a tabela:
- Para $k=0$: $F(0) = P(X=0) = \frac{1}{10} = 0,10$. (Ainda é menor que $0,666$).
- Para $k=1$: $F(1) = P(X=0) + P(X=1) = \frac{1}{10} + \frac{4}{10} = \frac{5}{10} = 0,50$. (Ainda é menor que $0,666$).
- Para $k=2$: $F(2) = F(1) + P(X=2) = 0,50 + \frac{3}{10} = 0,80$.

Como em $k=2$ a probabilidade acumulada $0,80$ ultrapassou pela primeira vez a marca crítica $0,6667$, concluímos pela fórmula marginal que a terceira unidade (de 2 para 3) não valeria o risco, mas ir do 1 para o 2 ainda era lucrativo.

Logo, o florista deveria ter exatamente **2 flores** em estoque.
