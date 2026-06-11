---
id: "q07-dantas-cap01"
titulo: "Questão 7"
topicos: ["01-variaveis-aleatorias-continuas"]
dificuldade: "media"
origem: "livro"
solucao_verificada: false
---

## Enunciado
Prove que: 
$$(a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k}$$

## Solução

Esta é a demonstração do **Teorema Binomial**. Podemos prová-lo por indução matemática sobre $n$ ou por um argumento combinatório.

### Prova Combinatória
Considere a expansão do produto de $n$ fatores:
$$ (a+b)^n = (a+b)(a+b)\cdots(a+b) \quad \text{($n$ vezes)} $$
Quando realizamos a multiplicação distributiva, cada termo do produto final é formado escolhendo exatamente um elemento (ou $a$ ou $b$) de cada um dos $n$ parênteses.
Se escolhermos o termo $a$ de exatamente $k$ parênteses, seremos forçados a escolher o termo $b$ dos $n-k$ parênteses restantes. O produto dessas escolhas resultará no termo $a^k b^{n-k}$.
A quantidade de maneiras de escolhermos quais são os $k$ parênteses (dentre os $n$ disponíveis) dos quais tiraremos o $a$ é exatamente o número de combinações de $n$ elementos tomados $k$ a $k$, ou seja, $\binom{n}{k}$.
Logo, ao somarmos os termos iguais, o termo $a^k b^{n-k}$ aparecerá $\binom{n}{k}$ vezes. Somando sobre todos os possíveis valores de $k$ (de 0 até $n$), obtemos:
$$ (a+b)^n = \sum_{k=0}^n \binom{n}{k} a^k b^{n-k} $$

### Prova por Indução
**Base:** Para $n=1$, $(a+b)^1 = a+b$. A fórmula nos dá $\sum_{k=0}^1 \binom{1}{k} a^k b^{1-k} = \binom{1}{0}a^0b^1 + \binom{1}{1}a^1b^0 = b + a = a+b$. A base é verdadeira.

**Passo indutivo:** Suponha que a fórmula vale para $n$. Queremos mostrar que vale para $n+1$.
$$ (a+b)^{n+1} = (a+b)(a+b)^n = (a+b)\sum_{k=0}^n \binom{n}{k} a^k b^{n-k} $$
Distribuindo o $a$ e o $b$:
$$ = \sum_{k=0}^n \binom{n}{k} a^{k+1} b^{n-k} + \sum_{k=0}^n \binom{n}{k} a^k b^{n+1-k} $$
No primeiro somatório, fazemos a mudança de índice $j = k+1$, logo $k = j-1$. Quando $k=0$, $j=1$; quando $k=n$, $j=n+1$.
$$ = \sum_{j=1}^{n+1} \binom{n}{j-1} a^j b^{n-(j-1)} + \sum_{k=0}^n \binom{n}{k} a^k b^{n+1-k} $$
Reescrevendo a variável $j$ como $k$:
$$ = \sum_{k=1}^{n+1} \binom{n}{k-1} a^k b^{n+1-k} + \sum_{k=0}^n \binom{n}{k} a^k b^{n+1-k} $$
Separando o termo de $k=n+1$ do primeiro somatório e o termo de $k=0$ do segundo somatório:
$$ = \binom{n}{n} a^{n+1} b^0 + \sum_{k=1}^n \left[ \binom{n}{k-1} + \binom{n}{k} \right] a^k b^{n+1-k} + \binom{n}{0} a^0 b^{n+1} $$
Usando a Relação de Stifel (Identidade de Pascal) provada anteriormente $\binom{n}{k-1} + \binom{n}{k} = \binom{n+1}{k}$, e sabendo que $\binom{n}{n} = \binom{n+1}{n+1} = 1$ e $\binom{n}{0} = \binom{n+1}{0} = 1$:
$$ = \binom{n+1}{n+1} a^{n+1} + \sum_{k=1}^n \binom{n+1}{k} a^k b^{n+1-k} + \binom{n+1}{0} b^{n+1} $$
$$ = \sum_{k=0}^{n+1} \binom{n+1}{k} a^k b^{n+1-k} $$
Completando a prova por indução.
