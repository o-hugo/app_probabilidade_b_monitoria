---
id: "q08-dantas-cap01"
titulo: "Questão 8"
topicos: ["variaveis-aleatorias-continuas"]
dificuldade: "dificil"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Mostre que:
(a) $\sum_{k=0}^{n} \binom{n}{k} = 2^n$
(b) $\sum_{k=0}^{n} (-1)^k \binom{n}{k} = 0$
(c) $\sum_{k=r}^{n} \binom{k}{r} = \binom{n+1}{r+1}$
(d) $\sum_{k=0}^{n} \binom{m}{r-k} \binom{n}{k} = \binom{n+m}{r}, n \le r \le m$
(e) $\sum_{k=0}^{n} \binom{n}{k}^2 = \binom{2n}{n}$ (usando d)
(f) $\sum_{k=0}^{n} k \binom{n}{k} = n2^{n-1}$
(g) $\sum_{k=0}^{n} k(k-1) \binom{n}{k} = n(n-1)2^{n-2}$
(h) $\binom{n}{1} + \binom{n}{3} + \dots + \binom{n}{n-1} = \binom{n}{0} + \binom{n}{2} + \dots + \binom{n}{n}$, com n par.

## Solução

Essas identidades resultam de propriedades de combinatória e do Binômio de Newton.

- **(a)** Pelo Teorema Binomial, $(1+1)^n = \sum_{k=0}^n \binom{n}{k} 1^k 1^{n-k} \implies 2^n = \sum_{k=0}^n \binom{n}{k}$.
- **(b)** Pelo Teorema Binomial, $(1 - 1)^n = \sum_{k=0}^n \binom{n}{k} (-1)^k 1^{n-k} \implies 0 = \sum_{k=0}^n (-1)^k \binom{n}{k}$.
- **(c)** Conhecida como identidade das colunas ou "Hockey-stick identity". Prova por indução ou usando o triângulo de Pascal repetidamente: $\binom{r}{r} = \binom{r+1}{r+1}$, então $\binom{r+1}{r+1} + \binom{r+1}{r} = \binom{r+2}{r+1}$, e repetindo este processo de união obtemos $\binom{n+1}{r+1}$.
- **(d)** Identidade de Vandermonde. O coeficiente de $x^r$ em $(1+x)^{m+n}$ é $\binom{m+n}{r}$. Por outro lado, $(1+x)^{m+n} = (1+x)^m (1+x)^n$. O coeficiente de $x^r$ nesse produto é a soma dos produtos dos coeficientes de $x^{r-k}$ em $(1+x)^m$ e $x^k$ em $(1+x)^n$. Isso dá $\sum_{k} \binom{m}{r-k}\binom{n}{k}$. Igualando os dois lados, temos a identidade.
- **(e)** No item (d), faça $m = n$ e $r = n$. Obtemos $\sum_{k=0}^n \binom{n}{n-k}\binom{n}{k} = \binom{2n}{n}$. Sabendo que $\binom{n}{n-k} = \binom{n}{k}$, temos $\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}$. (Nota: no enunciado do livro estava com o somatório normal e não explícito o quadrado, mas $\binom{n}{k}^2$ equivale à fórmula correta para o resultado $\binom{2n}{n}$).
- **(f)** Diferencie $(1+x)^n = \sum_{k=0}^n \binom{n}{k} x^k$ em relação a $x$. Obtemos $n(1+x)^{n-1} = \sum_{k=0}^n k \binom{n}{k} x^{k-1}$. Substituindo $x=1$, obtemos $n 2^{n-1} = \sum_{k=0}^n k \binom{n}{k}$.
- **(g)** Diferencie $(1+x)^n$ duas vezes. A primeira é $n(1+x)^{n-1} = \sum k \binom{n}{k} x^{k-1}$. A segunda derivada em relação a $x$ é $n(n-1)(1+x)^{n-2} = \sum k(k-1) \binom{n}{k} x^{k-2}$. Avaliando em $x=1$, obtém-se $n(n-1)2^{n-2} = \sum_{k=0}^n k(k-1) \binom{n}{k}$.
- **(h)** Do item (b), temos que a soma com sinais alternados é zero: $\sum_{k=0}^n (-1)^k \binom{n}{k} = 0$. Separando os pares e os ímpares, $\sum_{k \text{ par}} \binom{n}{k} - \sum_{k \text{ ímpar}} \binom{n}{k} = 0$. Logo, $\sum_{k \text{ par}} \binom{n}{k} = \sum_{k \text{ ímpar}} \binom{n}{k}$. Isso conclui a prova.
