---
id: "q43-dantas-cap01"
titulo: "Questão 43"
topicos: []
dificuldade: "media"
origem: "livro-dantas"
solucao_verificada: false
---

## Enunciado
Suponha que r bolas distintas sejam distribuídas aleatoriamente em n urnas. Determine a probabilidade de que uma urna específica contenha exatamente k bolas, $k=0,1,\ldots,r$.

## Solução

Foque em uma única urna (digamos, a urna "alvo"). 
Para cada uma das $r$ bolas que serão distribuídas, existem $n$ urnas equiprováveis para ela cair.
A probabilidade de uma bola específica cair na urna alvo é $p = \frac{1}{n}$.
A probabilidade de ela NÃO cair na urna alvo é $1 - p = 1 - \frac{1}{n}$.

Como a distribuição de cada bola é independente das demais, o número de bolas $X$ que caiem na urna alvo segue uma distribuição Binomial:
$$ X \sim \text{Binomial}\left(r, \frac{1}{n}\right) $$

A probabilidade de que a urna alvo contenha exatamente $k$ bolas é dada pela fórmula da probabilidade da distribuição Binomial:
$$ P(X = k) = \binom{r}{k} p^k (1-p)^{r-k} $$
Substituindo $p = \frac{1}{n}$:
$$ P(X = k) = \binom{r}{k} \left(\frac{1}{n}\right)^k \left(1 - \frac{1}{n}\right)^{r-k} $$

Podemos também escrever a resposta em uma única fração expandida:
$$ P(X = k) = \binom{r}{k} \frac{(n-1)^{r-k}}{n^r} $$
