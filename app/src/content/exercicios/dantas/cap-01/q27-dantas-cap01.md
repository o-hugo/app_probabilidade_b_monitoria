---
id: "q27-dantas-cap01"
titulo: "Questão 27"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
O jogo da loto consiste em selecionar-se cinco dezenas do conjunto de cem dezenas de 00 a 99. Qual a probabilidade de se acertar a quina (5 dezenas) se marcar-se 10 dezenas no volante?

## Solução

O espaço amostral total do jogo, que chamaremos de $\Omega$, consiste em todas as formas possíveis de escolher 5 dezenas vencedoras dentre as 100 dezenas disponíveis.
O número total de resultados possíveis é dado pela combinação:
$$ n(\Omega) = \binom{100}{5} $$

Ao preencher o volante marcando 10 dezenas, você cobrirá uma quantidade de conjuntos de 5 dezenas igual ao número de combinações de 5 que podem ser formadas a partir das 10 que você escolheu.
Assim, o número de resultados favoráveis $n(A)$ (quantidade de apostas de 5 que você está fazendo com suas 10 dezenas marcadas) é:
$$ n(A) = \binom{10}{5} $$

Calculando os valores das combinações:
$$ \binom{10}{5} = \frac{10!}{5!5!} = \frac{10 \times 9 \times 8 \times 7 \times 6}{5 \times 4 \times 3 \times 2 \times 1} = 252 $$
$$ \binom{100}{5} = \frac{100!}{5!95!} = \frac{100 \times 99 \times 98 \times 97 \times 96}{5 \times 4 \times 3 \times 2 \times 1} = 75.287.520 $$

Logo, a probabilidade procurada é:
$$ P(A) = \frac{\binom{10}{5}}{\binom{100}{5}} = \frac{252}{75.287.520} $$
Isso equivale a 1 em 298.760, ou aproximadamente $0,000334\%$.
