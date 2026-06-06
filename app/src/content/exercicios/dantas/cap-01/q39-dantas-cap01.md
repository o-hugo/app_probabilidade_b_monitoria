---
id: "q39-dantas-cap01"
titulo: "Questão 39"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Seleciona-se ao acaso uma amostra casual de tamanho r de uma população de tamanho n, sem reposição. Qual é a probabilidade de que um elemento fixado seja incluído na amostra? Se a amostragem for com reposição, qual é a probabilidade de que um elemento fixado seja incluído pelo menos uma vez na amostra?

## Solução

Seja $x$ um elemento específico (fixado) da população de tamanho $n$.

- **Amostragem sem reposição:**
O número total de amostras de tamanho $r$ que podem ser formadas é $\binom{n}{r}$.
Queremos contar as amostras que incluem o elemento $x$. Se garantirmos que $x$ está na amostra, ainda precisaremos escolher mais $r-1$ elementos dentre os $n-1$ restantes da população. O número de maneiras de fazer isso é $\binom{n-1}{r-1}$.
A probabilidade procurada é:
$$ P(x \text{ na amostra sem reposição}) = \frac{\binom{n-1}{r-1}}{\binom{n}{r}} $$
$$ P = \frac{\frac{(n-1)!}{(r-1)!(n-r)!}}{\frac{n!}{r!(n-r)!}} = \frac{(n-1)! \times r! \times (n-r)!}{(r-1)!(n-r)! \times n!} $$
$$ P = \frac{r}{n} $$

- **Amostragem com reposição:**
O número total de resultados ordenados para $r$ seleções (cada seleção tem $n$ possibilidades) é $n^r$.
Para encontrar a probabilidade de o elemento $x$ aparecer *pelo menos uma vez*, é mais fácil calcular pelo evento complementar: "Qual é a probabilidade do elemento $x$ NÃO aparecer nenhuma vez na amostra?".
Se $x$ não aparece, significa que em cada uma das $r$ retiradas, os elementos sorteados vieram do conjunto de $n-1$ elementos (população menos o elemento $x$).
A quantidade de resultados nos quais $x$ nunca aparece é $(n-1)^r$.
Logo, a probabilidade de $x$ não aparecer é $\left(\frac{n-1}{n}\right)^r$.
A probabilidade de ele aparecer pelo menos uma vez é o complementar:
$$ P(x \text{ na amostra com reposição}) = 1 - \left(\frac{n-1}{n}\right)^r $$
