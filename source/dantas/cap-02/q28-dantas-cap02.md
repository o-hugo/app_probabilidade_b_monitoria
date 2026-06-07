---
id: "q28-dantas-cap02"
titulo: "Questão 28"
topicos: ["04-distribuicao-normal"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Para qualquer valor de $p>1$, seja $c(p)=\sum_{x=1}^{\infty}\frac{1}{x^p}$. Suponha que X é uma variável aleatória discreta com a seguinte distribuição de probabilidade: $f(x)=\frac{1}{c(p)x^p}$, para $x=1,2,\dots$ 
(a) Para qualquer inteiro positivo n, determine a probabilidade de X ser divisível por n. 
(b) A probabilidade de X ser ímpar.

## Solução

A constante $c(p)$ é conhecida como a Função Zeta de Riemann $\zeta(p)$ e serve como fator de normalização, já que a soma de probabilidades em todo o espaço amostral $\{1, 2, 3, \dots\}$ deve ser $1$.

- **(a) Probabilidade de $X$ ser divisível por $n$:**
Dizer que $X$ é divisível por um inteiro $n$ significa que os valores que a variável assume são os múltiplos naturais de $n$, isto é, $X \in \{1n, 2n, 3n, 4n, \dots\}$.
Podemos expressar essa probabilidade como um somatório infinito das probabilidades pontuais nestes múltiplos:
$$ P(X \text{ é mult de } n) = \sum_{k=1}^{\infty} P(X = k\cdot n) $$
Substituindo a expressão de probabilidade fornecida pelo problema:
$$ P(X \text{ é mult de } n) = \sum_{k=1}^{\infty} \frac{1}{c(p) (kn)^p} $$
Usando a propriedade das potências no denominador $((k \cdot n)^p = k^p n^p)$, podemos colocar as constantes em evidência:
$$ P(X \text{ é mult de } n) = \frac{1}{n^p c(p)} \sum_{k=1}^{\infty} \frac{1}{k^p} $$
O somatório restante é exatamente a definição da constante $c(p)$ dada no enunciado. Logo, substituímos e cancelamos:
$$ P(X \text{ é mult de } n) = \frac{1}{n^p c(p)} \cdot c(p) = \frac{1}{n^p} $$

- **(b) Probabilidade de $X$ ser ímpar:**
O evento "$X$ é um número ímpar" é complementar do evento "$X$ é um número par".
Um número é par se, e somente se, for múltiplo (divisível) por $2$.
Pela lei do evento complementar e aproveitando o resultado construído no item anterior com $n=2$:
$$ P(X \text{ é ímpar}) = 1 - P(X \text{ é par}) $$
$$ P(X \text{ é ímpar}) = 1 - P(X \text{ é mult de } 2) $$
$$ P(X \text{ é ímpar}) = 1 - \frac{1}{2^p} $$
